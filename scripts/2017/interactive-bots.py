import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

bots_to_create = [
    ('baremetrics', 'gives companies real-time updates about customer behavior and financial performance'),
    ('Chess', 'lets you play chess against the computer or other people on Zulip; '
              'use an existing chess engine for this'),
    ('Dialogflow', 'allows users to quickly build bots that converse in natural language;'
                   'use https://github.com/dialogflow/dialogflow-python-client for building the integration'),
    ('Four in a row', 'lets you play "Four in a row" against the computer or other people on Zulip; '
                      'use an existing "Four in a row" engine for this'),
    ('Google Hangouts', 'posts a link to a Hangouts call.'),
    ('Google Translate', 'provides machine translations'),
    ('i done this', 'provides work status updates for teams; '
                    'use https://i-done-this.readme.io/docs/ for building the integration'),
    ('Intercom', 'helps businesses track how users are interacting with their software;'
                 'use https://github.com/jkeyes/python-intercom for building the integration'),
    ('lunch', 'lets users create and join lunch events;'
              'use hubot-lunchbot as an orientation'),
    ('mention', 'crawls the web for product mentions; '
                'use https://dev.mention.com/current/ for building the integration'),
    ('Merels', 'lets you play merels against the computer or other people on Zulip; '
               'use an existing merels engine for this'),
    ('monkeytest.it', 'scans websites for bugs and broken links'),
    ('URL shortener', 'takes a link and sends back a shortened version using a shortener service'),
    ('wit.ai', 'integrates Zulip with wit.ai bots that interact based on natural language; '
               'use https://github.com/wit-ai/pywit for building the integration'),
]

bots_to_improve = [
    ('googlesearch', 'returns a top Google search result for the search term'),
    ('tictactoe', 'lets you play Tic-tac-toe against the computer'),
    ('wikipedia', 'returns a link to the top Wikipedia article for the search term'),
    ('youtube', 'returns the top Youtube video for the search term'),
]

description = """Zulip supports interactive bots. Bots are little programs that have
limited access to a Zulip server. They can receive messages @-mentioning them and
respond with useful information, jokes, etc.

The following tasks will introduce you to using interactive bots and creating
simple new bots that react to messages. This group of tasks has a high creative
potential, as you can create your own bots that react to specific messages and
can be integrated with various APIs.

"""

description_AB = description + "For this task, do **Task Type %(type)s**."
description_C = description + "For this task, do **Task Type C** for creating a " + \
                              "**%(bot)s** bot (%(desc)s)."
description_D = description + "For this task, do **Task Type d** for improving " + \
                               "the **%(bot)s** bot (%(desc)s)."

# Task Type A
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Learn about interactive bots, pt 1: running the helloworld bot.',
    description = description_AB % {'type': 'A' },
    status = 2, # 1: draft, 2: published
    max_instances = 100,
    mentors = ['robhoenig@gmail.com'],
    tags = ['python', 'bots'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/interactive-bots.md",
    private_metadata = "interactive-bots-A",
    do_upload = args.force)

# Task Type B
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Learn about interactive bots, pt 2: creating a message info bot.',
    description = description_AB % {'type': 'B' },
    status = 2, # 1: draft, 2: published
    max_instances = 100,
    mentors = ['robhoenig@gmail.com'],
    tags = ['python', 'bots'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/interactive-bots.md",
    private_metadata = "interactive-bots-B",
    do_upload = args.force)

for bot, desc in bots_to_create:
    # Task Type C
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Create your own %s bot.' % (bot,),
        description = description_C % {'bot': bot, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['robhoenig@gmail.com'],
        tags = ['python', 'bots'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/interactive-bots.md",
        private_metadata = "interactive-bots-C",
        do_upload = args.force)

for bot, desc in bots_to_improve:
    # Task Type D
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Improve the %s bot.' % (bot,),
        description = description_D % {'bot': bot, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['robhoenig@gmail.com'],
        tags = ['python', 'bots', 'creative'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1, 4],
        time_to_complete_in_days = 5, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/interactive-bots.md",
        private_metadata = "interactive-bots-D",
        do_upload = args.force)

if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
