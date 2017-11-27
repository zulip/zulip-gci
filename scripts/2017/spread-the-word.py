import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Help support Zulip by voting for it in various platforms.

This task will introduce you to some of the tools that engineers use
to make decisions about which technologies to use in their
organization.  The task description is available here:

https://github.com/zulip/zulip-gci/blob/master/tasks/2017/spread-the-word.md
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Spread the word about Zulip',
    description = description,
    status = 2, # 1: draft, 2: published
    max_instances = 100,
    mentors = ['lylafisch@gmail.com', 'rishig@zulipchat.com'],
    tags = ['outreach'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [5],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/spread-the-word.md",
    private_metadata = "spread-the-word",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
