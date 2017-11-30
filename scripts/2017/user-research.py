import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """\
This task teaches two skills important in developing almost any product:
user research, and sales. The task description is available here:

https://github.com/zulip/zulip-gci/blob/master/tasks/2017/user-research.md
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Learn about sales by doing user interviews',
    description = description,
    status = 2, # 1: draft, 2: published
    max_instances = 30,
    mentors = ['lylafisch@gmail.com', 'rishig@zulipchat.com'],
    tags = ['outreach'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [5],
    time_to_complete_in_days = 7, # must be between 3 and 7
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/user-research.md",
    private_metadata = "user-research",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
