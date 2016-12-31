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
]

uploaded_issues = [
    # Batch 3
    (2996, ['shell']),
    (2991, ['python']),
    (2989, ['javascript']),
    (2932, ['javascript']),
    (2967, ['python']),
    # Batch 2
    (2713, ['python', 'javascript']),
    (2668, ['documentation']),
    (2659, ['javascript']),
    (2640, ['python', 'javascript']),
    (2629, ['javascript']),
    (2628, ['javascript']),
    (2713, ['python', 'javascript']),
    (2431, ['python', 'javascript']),
    (2419, ['python', 'shell']),
    (2281, ['javascript']),
    (2270, ['html', 'css']),
    (2058, ['python', 'HTML']),
    (1996, ['javascript']),
    (1734, ['javascript']),
    (1276, ['python', 'testing']),
    (215, ['python']),
    # Batch 1
    (2657, ['python', 'javascript']),
    (2560, ['documentation']),
    (2527, ['javascript']),
    (2465, ['python']),
    (2464, ['javascript']),
    (2448, ['javascript']),
    (2435, ['python']),
    (2430, ['python']),
    (2426, ['python']),
    (2427, ['python']),
    (2423, ['npm', 'node']),
    (2422, ['documentation']),
    (2396, ['python']),
    (2357, ['javascript']),
    (2355, ['javascript']),
    (2350, ['python']),
    (2327, ['python', 'bots']),
    (2321, ['node', 'testing']),
    (2287, ['python', 'javascript']),
    (2247, ['python', 'javascript']),
    (2239, ['python', 'test mocking']),
    (2058, ['html']),
    (2008, ['javascript', 'autocomplete']),
    (1969, ['emoji']),
    (1663, ['javascript']),
    (1528, ['python']),
]

head_description = """Your task is to solve an open bug or missing feature in the Zulip
server project. Here is the issue:

"""

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
        description = head_description + description + tail_description,
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['issues'] + tags, # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        private_metadata = "issues",
        do_upload = args.force)


if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
