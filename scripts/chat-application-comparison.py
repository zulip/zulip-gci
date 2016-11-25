import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

chat_applications_names = ["Slack", "HipChat", "Microsoft for Teams", "Mattermost", "RocketChat"]
task_sets = ["a", "b", "c", "d", "e"]

task_name = 'Identify which features are present in %s: Set %s'

task_description = """"Help us prepare the comparison page between Zulip and other chat tools,
with a matrix of which features each product has or doesn't have.  Your task is to test
**%s** and figure out which all features are present in it. See %s to see the features you
have to test and the output format"""

for chat_application_name in chat_applications_names:
    for set in task_sets:
        url = "https://github.com/hackerkid/zulip-gci/blob/master/tasks/chat-application-comparison.md#set-%s" % set
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = task_name % (chat_application_name, set.upper()),
            description = task_description % (chat_application_name, url),
            status = 1, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['tabbott@zulipchat.com', 'rishig@zulipchat.com', 'niftynei@gmail.com', 'yo@vishnuks.com'],
            tags = ['user research'], # free text
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [2, 5],
            time_to_complete_in_days = 3, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "TODO",
            private_metadata = "chat-application-comparison",
            do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
