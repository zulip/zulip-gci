import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """This task is about adding tests for Zulip's custom linter rules.

Instructions for this task are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/linter-rules.md

For this task, update the linter rule {}.
"""

linter_rules_uploaded = [
    ("groups trailing_whitespace_rule, whitespace_rules, markdown_whitespace_rules, markdown_rules, help_markdown_rules, and prose_style_rules", ['markdown']),
    ("group js_rules", ['javascript']),
    ("group python_rules", ['python']),
    ("groups bash_rules, handlebars_rules and jinja2_rules", []),
    ("groups css_rules and html_rules", ['html', 'css']),
]

linter_rules = []

for task, tags in linter_rules:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = "Write tests for Zulip's code linter",
        description = description.format(task),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['robhoenig@gmail.com'],
        tags = ['linting', 'testing'] + tags, # free text
        is_beginner = True,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/linter-rules.md",
        private_metadata = "linter-rules",
        do_upload = args.force)

if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
