import os
import sys

task_uploader_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(task_uploader_path)
from task_uploader.client import GCIAPIClient

# Information about the fields is available at
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
# One field is missing in the documentation and in the argument list below: external_url.
# gci-support says it is coming soon.
def upload_task(name, description, status, max_instances, mentors, tags, is_beginner,
                categories, time_to_complete_in_days, private_metadata, do_upload = False):
    task = locals()
    del task['do_upload']
    try:
        homedir = os.path.expanduser("~")
        with open(os.path.join(homedir, '.GCI_API_KEY')) as api_key_file:
            API_KEY = api_key_file.readline().strip()
    except IOError:
        print("Please put your GCI API key at ~/.GCI_API_KEY.")
        print("You can get your key from https://codein.withgoogle.com/dashboard/profile/.")
        exit(1)

    if do_upload:
        GCIAPIClient(API_KEY).create_new_task(task)
        print("Task created at https://codein.withgoogle.com/dashboard/tasks/")
    else:
        print("Dry run, printing task below.")
        print(task)
