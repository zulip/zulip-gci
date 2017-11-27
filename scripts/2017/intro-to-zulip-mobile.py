import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """This task will introduce you to the process of setting up the Zulip React Native mobile app's development environment and playing with it.

Instructions for this task are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/intro-to-zulip-mobile.md
"""

upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Intro to Zulip mobile development',
    description = description,
    status = 2, # 1: draft, 2: published
    max_instances = 50,
    mentors = ['borisyankov@gmail.com', 'jainkuniya@gmail.com',
               'kunall.gupta17@gmail.com'],
    tags = ['intro', 'dev environment', 'react-native'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1, 3],
    time_to_complete_in_days = 5, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/intro-to-zulip-mobile.md",
    private_metadata = "intro-to-zulip-mobile",
    do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
