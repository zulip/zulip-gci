import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

A_tasks = [['zerver/tests/'], ['zerver/views/webhooks/'],
           ['analytics/', 'scripts/', 'tools/', 'zerver/management/', 'zilencer/', 'zproject/'],
           ['zerver/lib/bugdown/', 'zerver/lib/webhooks/']]

B_tasks = [
    'api/zulip/__init__.py',
    'bots/gcal-bot',
    'bots/githook-post-receive',
    'bots/jabber_mirror_backend.py',
    'bots/zephyr_mirror_backend.py',
    'puppet/zulip_ops',
    'tools/deprecated/generate-activity-metrics.py',
    'tools/deprecated/inject-messages/inject-messages',
    'zerver/tests/test_decorators.py',
    'zerver/tests/test_narrow.py']

description = """Help add mypy annotations to the Zulip codebase! This is a
great way to practice git, git grep, and efficiently using a powerful editor.

Instructions for mypy annotation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/mypy-annotations.md.

"""

description_A = description + "For this task, do **Task Type A** for the following set of directories: **%s**."
description_B = description + "For this task, do **Task Type B** for the following file: **%s**."

for directory_set in A_tasks:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Update mypy annotations in the Zulip codebase',
        description = description_A % directory_set,
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'mypy'], # free text
        is_beginner = True,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/mypy-annotations.md",
        private_metadata = "mypy-annotations-A",
        do_upload = args.force)

for filename in B_tasks:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Add mypy annotations to the Zulip codebase',
        description = description_B % filename,
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'mypy'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/mypy-annotations.md",
        private_metadata = "mypy-annotations-B",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
