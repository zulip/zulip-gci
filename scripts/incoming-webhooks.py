import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

integrations = [
    ('HelloSign', 'an E-signing tool'),
    ('AppFollow', 'monitors appstore activity')
    ('Mention', 'a media monitoring tool'),
    ('GoSquared', 'real time analytics'),
    ('Mailchimp', 'an email marketing tool'),
    ('InVision', 'a collaborative prototyping app'),
    ('Heroku', 'cloud hosting and deployment'),
    ('Stripe', 'online payments'),
    ('Papertrail', 'a log management tool'),
    ('Zeplin', 'design collaboration'),
]

description = """A [Zulip integration](https://zulipchat.com/integrations/) is a special
type of bot that brings information from the outside world into Zulip. Help
add integrations to Zulip!

Instructions for all integrations tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md.

"""

description_A = description + "For this task, do **Task Type A**."
description_BCD = description + "For this task, do **Task Type %(type)s** for " + \
                  "the **%(integration)s** integration (%(desc)s)."

# Task Type A
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Learn how Zulip integrations work.',
    description = description_A,
    status = 1, # 1: draft, 2: published
    max_instances = 20,
    mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
    tags = ['python', 'integrations'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
    private_metadata = "webhook-integrations-A",
    do_upload = args.force)

for integration, desc in integrations:
    # Task Type B
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Learn how an integration works in Slack.',
        description = description_BCD % {'type': 'B', 'integration': integration, 'desc': desc},
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = True,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
        private_metadata = "webhook-integrations-B",
        do_upload = args.force)

    # Task Type C
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write code to add an integration to Zulip.',
        description = description_BCD % {'type': 'C', 'integration': integration, 'desc': desc},
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
        private_metadata = "webhook-integrations-C",
        do_upload = args.force)

    # Task Type D
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Add user documentation for a Zulip integration.',
        description = description_BCD % {'type': 'D', 'integration': integration, 'desc': desc},
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
        private_metadata = "webhook-integrations-D",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
