import json
import os
import requests

# Information about the fields is available at
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
# One field is missing in the documentation and in the argument list below: external_url.
# gci-support says it is coming soon.
def upload_task(name, description, status, max_instances, mentors, tags, is_beginner,
                categories, time_to_complete_in_days, private_metadata):
    task = locals()
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

    r = requests.post(url, headers=headers, data=json.dumps(task))
    r.raise_for_status()
    if (r.status_code != 201):
        raise Exception("Task not created. Something went wrong.")
    print("Task created at https://codein.withgoogle.com/dashboard/tasks/")
