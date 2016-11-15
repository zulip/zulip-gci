"""Script that shows the basics of uploading tasks via the GCI API.
The example below is for the PEP8 category of tasks."""

import json
import os
import requests
import sys

try:
    homedir = os.path.expanduser("~")
    API_KEY = file(homedir + '/.GCI_API_KEY').readline().strip()
except IOError:
    print("Please put your GCI API key at ~/.GCI_API_KEY.")
    print("You can get your key from https://codein.withgoogle.com/dashboard/profile/.")
    exit(1)

headers = {
    'Authorization': 'Bearer %s' % API_KEY,
    'Content-Type': 'application/json'}
url = 'https://codein.withgoogle.com/api/program/current/tasks/'

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

# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
task = {}
task['name'] = 'Cleanup Zulip code to follow PEP-8 style standards'
task['status'] = 1 # 1: draft, 2: published
task['max_instances'] = 1
task['mentors'] = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com']
task['tags'] = ['python', 'pep8']
# 1: Coding, 2: User Interface, 3: Documentation & Training, 4: Quality Assurance, 5: Outreach & Research
task['categories'] = [1, 4]
task['time_to_complete_in_days'] = 3 # must be between 3 and 7
task['external_url'] = 'https://[TODO]'
task['private_metadata'] = 'PEP8'

# Not idempotent. Running this script twice will create two sets of tasks.
print("Exiting .. remove these lines if you intended to actually upload these tasks.")
exit(1)

for rule in pep8_rules:
    task['is_beginner'] = rule in beginner_rules
    task['description'] = description % rule
    r = requests.post(url, headers=headers, data=json.dumps(task))
    r.raise_for_status()
    print(r) # 201 means task created
