import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Welcome to Zulip! This task will help you set up a development
environment, and introduce you to the process of making, testing and
submitting changes to Zulip.

Instructions are at https://github.com/zulip/zulip-gci/blob/master/tasks/welcome-to-zulip.md.
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Intro task, do me first! Set up development environment.',
    description = description,
    status = 1, # 1: draft, 2: published
    max_instances = 200,
    mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
    tags = [], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1],
    time_to_complete_in_days = 3, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/welcome-to-zulip.md",
    private_metadata = "welcome-to-zulip",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
