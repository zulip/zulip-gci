import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

eslint_rules = ['new-cap', 'no-empty', 'space-before-blocks', 'yoda',
              'brace-style', 'keyword-spacing', 'one-var', 'no-else-return',
              'no-plusplus', 'no-shadow', 'max-len', 'quote-props',
              'no-unused-vars', 'comma-dangle']

description = """Fix the Zulip JavaScript code style! This is a great way to 
learn the basics of refactoring, git workflow, and good style.

Instructions for eslint tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/eslint.md

For this task, fix the errors for rule **%s**.
"""

for rules in eslint_rules:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Cleanup Zulip JavaScript code: eslint %s' % (rules,),
        description = description % ', '.join(rules),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['arpith@feedreader.co', 'brock@zulipchat.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['javascript', 'eslint'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/eslint.md",
        private_metadata = "eslint",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
