import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

# We can release these later
larger_pep8_rules = [['E261']]

skipped_pep8_rules = [
    # We should maybe release these later. They require more judgement
    ['E251'],  # This one is also larger
    ['E221'],

    # We should definitely not release these
    ['E703'],
    ['E731'],
    ['W503'],
    ['E266'],
    ['E265'],
    ['E402']
]

# These are all ready to go
pep8_rules = [['E128'],
              ['E127'],
              ['E303'],
              ['E301'],
              ['E203'],
              ['E225'],
              ['E122', 'E131'],
              ['E502', 'E129'],
              ['E302', 'E211'],
              ['E124', 'E111'],
              ['E701', 'E222'],
              ['E202', 'E201'],
              ['E231', 'E125']]

description = """Fix the Zulip codebase to follow PEP-8 python style guidelines! This is a
great way to learn the basics of refactoring, git workflow, and good style.

Instructions for PEP-8 tasks are at https://github.com/zulip/zulip-gci/blob/master/tasks/pep8.md.

For this task, fix the errors for the following rule(s): **%s**.
"""

for rules in pep8_rules:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Cleanup Zulip code to follow PEP-8 rule(s) %s' % (", ".join(rules),),
        description = description % ', '.join(rules),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['zev-zuliporg@strangersgate.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'pep8'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/pep8.md",
        private_metadata = "pep8",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
