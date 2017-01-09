'''
This is an exploration of tic-tac-toe, where I try
to program the game using simple Python data structures.

Let's start with the board.  We'll represent it like
this:

1 2 3
4 5 6
7 8 9

You could say that square 5 has coordinates (1, 1), but
we don't need that complication yet.

The two players are X and O.  Let's represent the progress
of a game as simply and clearly as we can:

[
    ('X', 5),
    ('Y', 1),
    ('X', 2),
]

Before we do anything, it's gonna be extremely useful to
be able to visualize any game.  We'll make it somewhat compact:

YX-
-X-
---

Let's write the code...
'''

SQUARES = {1, 2, 3, 4, 5, 6, 7, 8, 9}
CORNERS = {1, 3, 7, 9}
OPEN = '-'

def board_display(moves):
    squares = {s: OPEN for s in SQUARES}
    for player, square in moves:
        squares[square] = player
    display = ''.join([
        squares[1], squares[2], squares[3], '\n',
        squares[4], squares[5], squares[6], '\n',
        squares[7], squares[8], squares[9],
    ])
    return display

# Next, test it...

def clean_ws(s):
    return s.replace(' ', '').replace('\n', '')

def test_display():
    moves = [
        ('X', 5),
        ('Y', 1),
        ('X', 2),
    ]

    disp = board_display(moves)

    expected = """
        YX-
        -X-
        ---
        """

    assert clean_ws(disp) == clean_ws(expected)

test_display()


'''
So far I feel pretty good about the game.  I haven't had
to do too much serious thinking yet about the game, and
I can at least visualize moves that are input to me.

Let me see if I can figure out if a game is over.  I'll
borrow an idea from Maydha and have a simple data structure
to represent the geometry of the game:
'''

TRIPLETS = dict(
    row1 = {1, 2, 3},
    row2 = {4, 5, 6},
    row3 = {7, 8, 9},

    col1 = {1, 4, 7},
    col2 = {2, 5, 8},
    col3 = {3, 6, 9},

    diag1 = {1, 5, 9},
    diag2 = {3, 5, 7},
)

'''
For any game I want to determine the winner, so I will have
a function that returns 'X' or 'O', or, if the game is not
yet done, then None.
'''

def winner(moves):
    for player in 'XO':
        my_moves = {square for p, square in moves
            if p == player}
        for squares in TRIPLETS.values():
            if squares.issubset(my_moves):
                return player # they won!
    return None

'''
The above code seems reasonable enough.  Before I test it,
I want a little helper function for testing.

This is a decent way to represent moves internally:

    [('X', 5), ('O', 3]]

It's awkward to type, though, so I want a new notation:

    X5O3

I can make that work!
'''

def expand(s):
    def moves():
        it = iter(s)
        while it:
            yield (next(it), int(next(it)))
    return list(moves())

assert expand('') == []
assert expand('X5') == [('X', 5)]
assert expand('X5O1') == [('X', 5), ('O', 1)]

# Ok, back to testing our winner function!

assert winner(expand('')) is None
assert winner(expand('X5')) is None
assert winner(expand('X5O1X4O2X6')) is 'X'
assert winner(expand('X5O1X4O2X9')) is None


'''
Let's take stock of what we have so far:

    - We have two simple ways to represent the moves
      in the game--one that's easy to program with
      and one that's easy to type.

    - We can display the board.

    - We can tell when somebody has won.

Let's make some other building blocks:

    whose_turn(moves)
    claimed_squares(moves, player)
    open_squares(moves)
'''

def whose_turn(moves):
    return 'XO'[len(moves) % 2]

assert whose_turn(expand('')) == 'X'
assert whose_turn(expand('X5')) == 'O'
assert whose_turn(expand('X5O3X2')) == 'O'

def claimed_squares(moves, player):
    return {square for p, square in moves
        if p == player}

assert claimed_squares(expand('X5O4X3'), 'X') == {5, 3}
assert claimed_squares(expand('X5O4X3'), 'O') == {4}

def open_squares(moves):
    claimed = {square for _, square in moves}
    return SQUARES - claimed

assert open_squares(expand('X5O4X3')) == {1, 2, 6, 7, 8, 9}

'''
Ok, now let's start getting into real analysis of a tic tac toe
game.  A typical opening sequence goes like this:

    X5O1X2

    OX-
    -X-
    ---

We can tell a few things here:
    - row1 is a stalemate
    - col1 is in O's favor at the moment
    - col2 is a THREAT for O
    - nobody's won yet

Let's see if we can build a game_state data structure that looks
something like this:

    dict(
        row1 = {'X': 1, 'O': 1},
        row2 = {'X': 1, 'O': 0},
        ...
        diag2 = {'X': 1, 'O': 0},
    )

We'll build it from the bottom up...
'''

def triplet_status(triplet_name, moves):
    squares = TRIPLETS[triplet_name]
    def count(player):
        return len(claimed_squares(moves, player).intersection(squares))

    return {player: count(player) for player in 'XO'}

assert triplet_status('row1', expand('X5O1X2')) == {'X': 1, 'O': 1}
assert triplet_status('row2', expand('X5O1X2')) == {'X': 1, 'O': 0}
assert triplet_status('col2', expand('X5O1X2')) == {'X': 2, 'O': 0}

def game_status(moves):
    return {
        triplet_name: triplet_status(triplet_name, moves)
        for triplet_name in TRIPLETS
    }

assert game_status(expand('X5O1X2')) == dict(
    row1 = dict(X=1, O=1),
    row2 = dict(X=1, O=0),
    row3 = dict(X=0, O=0),
    col1 = dict(X=0, O=1),
    col2 = dict(X=2, O=0),
    col3 = dict(X=0, O=0),
    diag1 = dict(X=1, O=1),
    diag2 = dict(X=1, O=0),
)

'''
Now let's put ourselves in X's shoes.  For the opening move,
X wants to move in the center, because then they will have
"representation" in four different triplets: row2, col2,
diag1, and diag2.

Let's write a function for that.
'''

def triplets_represented(moves, player):
    return {
        triplet_name
        for triplet_name in TRIPLETS
        if triplet_status(triplet_name, moves)[player] > 0
    }

assert triplets_represented(expand('X5'), 'X') == \
    {'row2', 'col2', 'diag1', 'diag2'}


'''
Let's start off by saying that player O wants to use the same
strategy, which is basically to maximize the number of triplets
that they "represent" on the board.

Let's write a little one-off analysis function for this...
'''

def analyze_options(prior_moves, player):
    def outcome_for_square(square):
        moves = prior_moves + [(player, square)]
        return len(triplets_represented(moves, player))

    squares = open_squares(prior_moves)
    return {
        square: outcome_for_square(square)
        for square in squares
    }

assert analyze_options(expand('X5'), 'O') == {
    1: 3, 2: 2, 3: 3,
    4: 2,       6: 2,
    7: 3, 8: 2, 9: 3,
}

'''
The assert statement above is a little hard to read,
but it basically demonstrates this to "O":

    - if they move on a corner, they represent on 3 triplets
    - if they move on an edge, they only get 2 triplets

Let's implement a greedy strategy, where O simply
maximizes their representation.  Since O is gonna have
four equally good choices after X moves in the center,
we'll break the tie by picking the square with largest
number, so O will move to square 9, the bottom right
corner.
'''

def decide_move_greedily(prior_moves, player):
    def outcome_for_square(square):
        moves = prior_moves + [(player, square)]
        score = len(triplets_represented(moves, player))
        # to break ties, we'll return a tuple, where
        # the second element is the number of the square
        return (score, square)

    squares = open_squares(prior_moves)
    return max(squares, key = outcome_for_square)

assert decide_move_greedily(expand('X5'), 'O') == 9

'''
The strategy we chose for O seems to make sense, so
let's simulate a game!
'''

def simulate_game_with_greedy_strategy():
    moves = []
    while open_squares(moves):
        player = whose_turn(moves)
        square = decide_move_greedily(moves, player)
        moves.append((player, square))
        if winner(moves):
            break
    return moves

assert simulate_game_with_greedy_strategy() == \
    [('X', 5), ('O', 9), ('X', 7), ('O', 4), ('X', 3)]

'''
We can start to see the folly of O's strategy.  They are
trying to be on as many triplets as possible, but they're
not playing any defense.

Let's create a new strategy for O.  We need a "threat" metric.
We need a player to know if they are leaving their opponent
with a 2-0 advantage on some triplet, which means imminent
defeat.

Let's code!
'''

def opponent(player):
    return {'X': 'O', 'O': 'X'}[player]

assert opponent('X') == 'O'
assert opponent('O') == 'X'

def opponent_threats(moves, player):
    return {
        triplet_name
        for triplet_name, status in game_status(moves).items()
        if status[opponent(player)] == 2 and status[player] == 0
    }

assert opponent_threats(expand('X1O5X3'), 'O') == {'row1'}
assert opponent_threats(expand('X1O5X3O2'), 'O') == set()

def decide_move_wisely(prior_moves, player):
    def outcome_for_square(square):
        moves = prior_moves + [(player, square)]
        if winner(moves) == player:
            score = 1000
        elif opponent_threats(moves, player):
            score = -1000
        else:
            score = len(triplets_represented(moves, player))

        # to break ties, we'll return a tuple, where
        # the second element is the number of the square
        return (score, square)

    squares = open_squares(prior_moves)
    return max(squares, key = outcome_for_square)

assert decide_move_wisely(expand('X1O9X2'), 'O') == 3

'''
So we now a have decide function that accounts for end game
scenarios.  Let's simulate a game where X plays greedily but
O plays more wisely.
'''

def simulate2():
    moves = []
    while open_squares(moves):
        player = whose_turn(moves)
        if player == 'X':
            square = decide_move_greedily(moves, player)
        else:
            square = decide_move_wisely(moves, player)
        moves.append((player, square))
        print('\n')
        print(board_display(moves))

'''
So I ran the above code, and O fights X to a draw.  I pasted
the output into here and added commentary.


---
-X- strong move by X
---


---
-X-
--O strong move by O


---
-X-
X-O dubious move by X


--O O had to block
-X-
X-O


--O
-XX X had to block
X-O


--O
OXX O had to block
X-O


-XO good move by X if O does something stupid
OXX
X-O


-XO
OXX
XOO O blocks


XXO the game is over, but X fills in the last square anyway :)
OXX
XOO

So after all this, we see that O has learned to play reasonably well
against an opponent who only made one possible blunder.

What happens if X moves wisely too?
'''

# So I decided when X played greedily, their bad move was
# responding to O9 with X7.  Before going too far, I believe
# X will make the same move even with the so-called "wise"
# strategy.  Here is my assertion:
assert decide_move_wisely(expand('X5O9'), 'X') == 7

'''
The assertion passes, so now I know that X needs to be more
clever to beat O.  But let's not be clever.  Let's use brute
force to simulate a bunch of random games and see if X stumbles
on a winning strategy.
'''

import random
def simulate_many_random_games(o_decide):
    random.seed(42) # be deterministic
    num_simulations = 10000
    x_wins = 0
    for i in range(num_simulations):
        moves = []
        while open_squares(moves):
            player = whose_turn(moves)
            if player == 'X':
                square = random.choice(list(open_squares(moves)))
            else:
                square = o_decide(moves, player)
            moves.append((player, square))
            the_winner = winner(moves)
            if the_winner == 'O':
                break
            elif the_winner == 'X':
                x_wins += 1
                break
    return x_wins

assert simulate_many_random_games(o_decide=decide_move_wisely) > 200

'''
It turns out that X will beat O over 2% of the time
by playing randomly!  That's not a lot, but clearly there is
a hole in O's strategy.  Let's make O smarter.

Let's do some work...
'''

def in_an_xox_diag_attack(moves):
    squares = [square for _, square in moves]
    return squares in [
        [1, 5, 9],
        [9, 5, 1],
        [7, 5, 3],
        [3, 5, 7],
    ]

def square_value(moves, player, square):
    statuses = [
        status
        for triplet_name, status in game_status(moves).items()
        if square in TRIPLETS[triplet_name]
    ]
    opp = opponent(player)

    value_matrix = {
        0: {0:    1,    1: 100,     2: 800},
        1: {0:   50,    1:   0},
        2: {0: 3000},
    }

    value = 0
    for status in statuses:
        my_count = status[player]
        opp_count = status[opp]
        value += value_matrix[my_count][opp_count]

    if in_an_xox_diag_attack(moves) and square in CORNERS:
        return 0

    return value

def decide_with_the_matrix(prior_moves, player):
    def outcome_for_square(square):
        score = square_value(prior_moves, player, square)
        return (score, square)

    squares = open_squares(prior_moves)
    return max(squares, key = outcome_for_square)

assert simulate_many_random_games(o_decide=decide_with_the_matrix) == 0


'''
And that's it for now!  We have given O the perfect defensive strategy.
It requires no lookahead at X's moves, but it does require knowing one
opening.  Otherwise, it's just evaluating the current board.
'''
