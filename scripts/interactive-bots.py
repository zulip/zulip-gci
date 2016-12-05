import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

bots = [
    ('Wikipedia', 'returns a link to the top Wikipedia article for the search term'),
    ('GitHub issue', 'opens a new GitHub issue with the message content'),
    ('GitHub issue comment', 'posts a comment on a GitHub issue'),
    ('Google', 'returns a top Google search result for a given keyword'),
    ('Alert', """messages a user or group at a scheduled time -
    [#585](https://github.com/zulip/zulip/issues/585)"""),
    ('Giphy', """displays gifs from Giphy site -
    [#839](https://github.com/zulip/zulip/issues/839)"""),
    ('Calendar', 'adds events to an external calendar, like Google Calendar'),
]

description = """Zulip
[contrib-bots](https://github.com/zulip/zulip/tree/master/contrib_bots/lib)
is a boilerplate for creating interactive bots that react to messages sent
by users.

The interactive bots live in the `contrib-bots/lib` as `.py` files that define
their specific behavior. The `contrib-bots/run.py` file defines common behaviors
for the interactive bots that react to messages.

The following tasks will introduce you to using interactive bots and creating
simple new bots that react to messages. This group of tasks has a high creative
potential, as you can create your own bots that react to specific messages and
can be integrated with various APIs.

"""

description_ABD = description + "For this task, do **Task Type %(type)s**."
description_C = description + "For this task, do **Task Type C** for " + \
                  "the **%(bot)s** bot (%(desc)s)."

# Task Type A
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Run the followup bot.',
    description = description_ABD,
    status = 2, # 1: draft, 2: published
    max_instances = 10,
    mentors = ['alicja.raszkowska@gmail.com'],
    tags = ['python', 'bots'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
    private_metadata = "interactive-bots-A",
    do_upload = args.force)

# Task Type B
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Create a links bot.',
    description = description_ABD,
    status = 2, # 1: draft, 2: published
    max_instances = 10,
    mentors = ['alicja.raszkowska@gmail.com'],
    tags = ['python', 'bots'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
    private_metadata = "interactive-bots-B",
    do_upload = args.force)

for bot, desc in bots:
    # Task Type C
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Create your %s own bot.' % (bot,),
        description = description_C % {'bot': bot, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['alicja.raszkowska@gmail.com', 'tabbott@zulipchat.com']
        tags = ['python', 'bots'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
        private_metadata = "interactive-bots-C",
        do_upload = args.force)

# Task Type D
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Create your own bot.',
    description = description_ABD,
    status = 2, # 1: draft, 2: published
    max_instances = 20,
    mentors = ['alicja.raszkowska@gmail.com', 'tabbott@zulipchat.com'],
    tags = ['python', 'bots', 'creative'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 5, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
    private_metadata = "interactive-bots-D",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
