import argparse
from upload import upload_task

import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

# (Issue number, tags)
# Catagory assumed to be coding
issues = [
    (2442, ['html', 'javascript']),
]

tail_description = """

Instructions for all issue tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/issues.md.
"""

# Task Type A
for (issue, tags) in issues:
    issue_data = json.loads(requests.get("https://api.github.com/repos/zulip/zulip/issues/" + str(issue)).content)
    title = issue_data['title']
    url = issue_data['html_url']
    description = 'Issue [#{0}]({1}) {2}'.format(issue, url, title)
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Issue #{0} {1}'.format(issue, title),
        description = description + tail_description,
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['issues'] + tags, # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = url,
        private_metadata = "issues",
        do_upload = args.force)


if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
