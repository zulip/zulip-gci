# GCI Tasks: Interactive bots

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for
  instructions on how to set one up.

* You need to know how to create a GitHub pull request. Check out the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/tasks/6541581402243072/)(TODO: Need to update this link with the new one)
  task if you aren't sure how to do this, or read through the task
  description [here](https://github.com/zulip/zulip-gci/tree/master/submit-a-pull-request).

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../../before-every-task.md).

## Background

[Zulip bots](https://github.com/zulip/python-zulip-api/tree/master/zulip_bots)
is a boilerplate for creating interactive bots that react to messages sent
by users.

The interactive bots live in the [`zulip_bots/bots/`](https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots) directory with a sub-directory for each bot.
Each bot directory has python files ('.py') that define their specific behavior,
automated tests and documentation. The overall directory structure of zulip bots can be seen
[here](https://github.com/zulip/python-zulip-api/tree/master/zulip_bots#directory-structure).

The following tasks will introduce you to using interactive bots and creating
simple new bots that react to messages. This group of tasks has a high
creative potential, as you can create your own bots that react to specific
messages and can be integrated with various APIs.

## Task Descriptions

There are four types of tasks in this category, each corresponding to one of
the Task Types below.

### Task Type A: Learn about interactive bots by running the helloworld bot

Follow the tutorial below to test run the helloworld bot on your Zulip
instance (either local or in your droplet).  As you're going through the tutorial,
take notes on where you got stuck or needed to look up terminology.

Refer to the detailed description on how to [run a zulip bot](https://chat.zulip.org/api/running-bots).

Follow the steps below to run helloworld bot:

* Create a bot with the name `<your-name>_helloworld_bot`.
(For details refer to the second step [here](https://chat.zulip.org/api/running-bots))

* Since we aim to run a helloworld bot, replace <my_bot> with helloworld while [running a bot](https://chat.zulip.org/api/running-bots).

* Test manually that the helloworld bot is working on the local Zulip instance,
by:

 - sending a few messages starting with `@<your-name>_helloworld_bot` from
 the stream "Verona".

 - checking that the bot is replying with `beep boop` each time.

* Take screenshots showing that the bot is working, make sure to have
screenshots of:

 - your terminal window with the bot running, including the command you used
 to run the bot and the output with the bot description
 - messages sent by you to the bot in "Verona" stream
 - messages sent by the bot in the same stream
 - any other screenshots you find relevant

  Add the screenshots to `interactive-bots/helloworld/<username>/`. Make sure
  your filenames do not have white-spaces. Instead, use dashes (`-`).

* Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/helloworld/<username>/`.

* Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the helloworld bot for <username>.`.

* Create a pull request in the `zulip/zulip-gci-submissions` repository, with title
`interactive bots: Run the helloworld bot for <username>`. Link to your GCI
task in comment section.

*Completion criteria:* Mentors will check that the helloworld bot was properly
set up.

### Task Type B: Learn about interactive bots by creating a message info bot

We recommend completing **Task Type A** before doing this task.

Follow the tutorial below to create your first simple bot. It will analyze a
message that @-mentions the bot and count its words for word count. The gathered
information will then be sent to a private conversation with the message author.

* Make a copy of the helloworld bot
[python-zulip-api/zulip_bots/zulip_bots/bots/helloworld](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots/helloworld)
and name it `message_info`, to build on existing code.
  ```shell
  cp -r helloworld message_info
  ```

* Rename `helloworld.py` to `message_info.py`. In `message_info.py`,
change the class name to `MessageInfoHandler` and the last line to
`handler_class = MessageInfoHandler`.

* Edit the return statement in `def usage(self)`:

  > This bot will allow users to analyze a message for letter count
  and word count. The gathered information will then be sent to a private
  conversation with the user. Users should @-mention the bot in the
  beginning of a message.

* Edit the code of `handle_message()`:
  ```python
  words_in_message = message['content'].split()
  content = "You sent a message with {} words.".format(len(words_in_message))
  ```

* Create a new bot in your development server's settings. Use "Message info bot"
as the bot's full name, and "message-info" as its username. Run your bot
like in **Task Type A**.

* Check that the bot is working as expected:

  - it replies to messages that @-mention the bot with the word count of that message
  - it currently replies to a message in the same stream, as the helloworld
  bot did

* Edit the code of `handle_message()` once again:

  ```python
  original_sender = message['sender_email']
  bot_handler.send_message(dict(
      type='private',
      to=original_sender,
      content=content,
  ))
  ```

* Check that the bot is working as expected:

  - it responds to messages that @-mention the bot with the word count of that message
  - it responds with a private message to the sender of the original message

* Rename `test_helloworld.py` to `test_message_info.py` and edit the file:

  ```python
  bot_name = 'message_info'
  ```

* Edit the bot's unit tests. Our bot is expected to respond with a private
message, so we need slightly more complicated testing methods:

  ```python
  message = "this should be five words"
  response = {'type': 'private',
              'to': 'foo_sender@zulip.com',
              'content': 'You sent a message with 5 words.'}
  expected_conversation = [
      (message, response)
  ]
  self.check_expected_responses(expected_conversation, expected_method='send_message')
  ```

* Test your new unit test for your bot. Run `tools/test-bots message_info` in your
  `python-zulip-api` repo.

* Take screenshots showing that the bot is working, make sure to have
screenshots of:

  - your terminal window with the bot running, including the command you used
  to run the bot and the output with the bot description
  - messages sent by you to the bot in the `Verona` stream
  - messages sent by the bot in the private messages to the author
  - your successful unit test
  - any other screenshots you find relevant

* Add the screenshots to `interactive-bots/message_info/<username>/`. Make sure your
filenames do not have white spaces. Instead, use dashes (`-`).

  - Note down any places you got stuck, problems or errors you ran into while
  doing this setup process. Add your notes as a `notes.md` file to
  `interactive-bots/message_info/<username>/`.

  - Create a commit with the screenshots and notes, with commit message
  `interactive bots: Run the message_info bot for <username>.`

  - Create a pull request in the [zulip/zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) repository, with title
  `interactive bots: Run the message_info bot for <username>`. Link to your GCI task
  in comment section.

*Completion criteria:* Mentors will check that the message info bot was properly
set up.

### Task Type C: Create an interactive bot

We recommend claiming this task type after completing Task Type A
and Task Type B.

Let *feature* be the feature mentioned in the task that brought you here.

* Make sure you understand what is expected of the *feature* - what messages
should the bot react to, what should it do with the message content and
where should it post any output. Should you have any doubts, discuss them in
the Zulip `GCI tasks` stream.

* Create the interactive bot at `~/zulip/contrib_bots/lib/<feature>` as a
`<feature>.py` file. Make sure it fulfills the requirements.

* Test your bot manually, check that:

  * The bot is reacting to the appropriate messages.
  * The bot uses the content from the messages properly.
  * The bot posts the expected output.

* Create a commit with your bot, with commit message `interactive bots:
Create *feature* bot.`.

* Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create *feature* bot.`. Link to your GCI task in
the comment section on GitHub.

*Completion criteria:* Mentors will check if the new bot fulfills the
feature requirements.

### Task Type D: Create your own bot

We recommend claiming this task type after completing Task Type A and Task
Type B.

* Come up with an idea for your own interactive bot that would improve Zulip.
Make sure to make clear what would be expected of the bot - the kind of
messages it should react to, what it should do with the message content and
where it should post any output.

* Present your idea for an interactive bot on the `interactive bots` topic
on the `GCI tasks` stream. Consult with mentors and make sure your idea is
approved before you start coding.

* Create your interactive bot at `~/zulip/contrib_bots/lib/<bot_name>` as a
`<bot_name>.py` file. Make sure it fulfills the requirements.

* Test your bot manually, check that:

  * The bot is reacting to the appropriate messages.
  * The bot uses the content from the messages properly.
  * The bot posts the expected output.

* Document your interactive bot at `~/zulip/contrib_bots/lib/<bot_name>` in
a `docs.md` (about the bot, how the bot works, what the bot does, etc.). Add
any relevant screenshots that will help understand how the bot works.

* Create a commit with your bot, with commit message `interactive bots:
Create <bot_name> bot.`.

* Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create <bot_name> bot by <username>.`. Link to your GCI
task in the comment section on GitHub.

*Completion criteria:* Mentors will check if the new bot fulfills the feature
requirements.
