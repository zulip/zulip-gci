import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Zulip allows users to create custom bots and integrations,
and those bots need avatars to help make the product more fun! Zulip would like
to provide a library of cute custom avatars that users can choose from
when creating a new bot.

Instructions for bot avatars tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/bot-avatars.md

For this task, do any one of the listed Task Types.
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Design or find avatars for Zulip bots',
    description = description,
    status = 1, # 1: draft, 2: published
    max_instances = 30,
    mentors = ['arpith@feedreader.co', 'niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
    tags = ['design', 'bots', 'avatars'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [2, 5],
    time_to_complete_in_days = 7, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/bot-avatars.md",
    private_metadata = "bot-avatars",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
