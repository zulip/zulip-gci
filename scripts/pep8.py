import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

pep8_rules = ['E251', 'E261', 'E128', 'E402', 'E221', 'E265', 'E127', 'E303',
              'E266', 'E301', 'W503', 'E203', 'E731', 'E225', 'E122', 'E502',
              'E129', 'E703', 'E302', 'E211', 'E131', 'E124', 'E111', 'E701',
              'E222', 'E202', 'E201', 'E231', 'E125']

beginner_rules = frozenset(['E211', 'E131', 'E124', 'E111', 'E701', 'E222',
                            'E202', 'E201', 'E231', 'E125'])

description = """Fix the Zulip codebase to follow PEP-8 python style guidelines! This is a
great way to learn the basics of refactoring, git workflow, and good style.

Instructions for PEP-8 tasks are at https://[TODO].

For this task, fix the errors for rule **%s**.
"""

for rule in ["E261"]:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Cleanup Zulip code to follow PEP-8 style standards',
        description = description % rule,
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'pep8'], # free text
        is_beginner = rule in beginner_rules,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "PEP8",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
