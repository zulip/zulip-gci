import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Review Slack integrations! This is a great way to get an understanding
of the different types of integrations and the enormous range of them.

Instructions for these tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/review-slack-integrations.md

For this task, review rows **%s** through **%s** in the spreadsheet.
"""

for n in range(5, 806, 30):
    low = n
    high = max(n + 29, 806)
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Analyze Slack integrations: rows {} to {}'.format(low, high),
        description = description % (low, high),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['michael.cordover@gmail.com', 'tomasz-kolek@o2.pl', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['integrations', 'research'], # free text
        is_beginner = True
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/eslint.md",
        private_metadata = "slack",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
