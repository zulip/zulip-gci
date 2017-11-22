import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """This task will introduce you to the process of making and
testing changes to Zulip.

Instructions for this task are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/intro-to-zulip-server.md
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Intro to Zulip server development',
    description = description,
    status = 2, # 1: draft, 2: published
    max_instances = 100,
    mentors = ['lylafisch@gmail.com', 'joshuapan8@gmail.com',
               'hkmp7tommy@gmail.com', 'yo@vishnuks.com'],
    tags = ['intro', 'vagrant', 'dev environment', 'vagrant'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1, 3],
    time_to_complete_in_days = 5, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/intro-to-zulip-server.md",
    private_metadata = "intro-to-zulip-server",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
