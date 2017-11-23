import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Find new bugs in Zulip!

Instructions for this task are at
https://github.com/zulip/zulip-gci/blob/master/tasks/quality-assurance.md.
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Find and report bugs in Zulip (backend, web, desktop, mobile, bots, or anywhere else!)',
    description = description,
    status = 2, # 1: draft, 2: published
    max_instances = 40,
    mentors = ['lylafisch@gmail.com'],
    tags = ['bug squashing', 'internationalization', 'mobile', 'frontend', 'real-time sync'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [2, 4],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/quality-assurance.md",
    private_metadata = "quality-assurance",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
