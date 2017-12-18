import argparse
from upload import upload_task

import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

# (Issue number, tags)
# Category of issue assumed to be coding
zulip_issues = [
    #(3055, ['javascript', 'html']),
]

zulip_mobile_issues = []

zulip_electron_issues = []

python_zulip_api_issues = []

zulipbot_issues = [
    (134, ['javascript', 'node.js', 'github api']),
    (135, ['javascript', 'node.js', 'github api']),
    (136, ['javascript', 'node.js', 'github api']),
    (137, ['javascript', 'node.js', 'github api']),
    (138, ['javascript', 'node.js', 'github api']),
    (139, ['javascript', 'node.js', 'github api']),
    (140, ['javascript', 'node.js', 'github api']),
]

zulipbot_issues = []

# See https://paper.dropbox.com/doc/Issues-for-GCI-Students-3jpXd8i4Y3YbpTMdphQ1u
# for list of uploaded tasks

def create_tasks_from_issues(issues, repo_name, mentors):
    head_description = """Your task is to solve an open bug or missing feature in the
{} repository. Here is the issue:

""".format(repo_name)

    tail_description = """

Instructions for all issue tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/issues.md
"""

    # Task Type A
    for (issue, tags) in issues:
        issue_url = "https://api.github.com/repos/zulip/{}/issues/{}".format(repo_name, str(issue))
        issue_data = json.loads(requests.get(issue_url).content.decode('utf-8'))
        title = issue_data['title']
        url = issue_data['html_url']
        description = 'Issue [#{0}]({1}) {2}'.format(issue, url, title)
        print(head_description + description + tail_description)
        print("")
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = 'Issue #{0} {1}'.format(issue, title),
            description = head_description + description + tail_description,
            status = 2, # 1: draft, 2: published
            max_instances = 1,
            mentors = mentors,
            tags = ['issues'] + tags, # free text, maximum 5 tags
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [1],
            time_to_complete_in_days = 5, # must be between 3 and 7
            # external_url=url,
            private_metadata = "issues",
            do_upload = args.force)

create_tasks_from_issues(zulip_issues, "zulip", ['lylafisch@gmail.com', 'rishig@zulipchat.com', 'malavarena@gmail.com',
                                                 'harshitbansal2015@gmail.com', 'cjl2625@gmail.com'])
create_tasks_from_issues(zulip_mobile_issues, "zulip-mobile", ["jainkuniya@gmail.com", "saumya.bhatnagar.sb@gmail.com", "cdikibo@alumni.nd.edu"])
create_tasks_from_issues(zulip_electron_issues, "zulip-electron", ["akash@zulipchat.com"])
create_tasks_from_issues(python_zulip_api_issues, "python-zulip-api", ["robhoenig@gmail.com", "volkova.ag@gmail.com",
                                                                       "jerryguitarist@gmail.com", "abhijeetkaur96@gmail.com"])
create_tasks_from_issues(zulipbot_issues, "zulipbot", ["joshuapan8@gmail.com"])

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
