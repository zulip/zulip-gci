import argparse
from upload import upload_task

import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

urls = [
    ("json/make_stream_public and json/make_stream_private", "Make an argument to PATCH streams/(?P<stream_name>.*)"),
# Commented since plan is to delete
#    ("json/subscriptions/exists", "Replace with existing HEAD streams/(?P<stream_name>.*)"),
    ("json/subscriptions/remove", "Replace with existing DELETE streams/(?P<stream_ID>.*)"),
    ("json/get_subscribers", "Replace with existing GET streams/(?P<stream_ID>.*)/members"),
    ("json/set_avatar", "Move to PUT /users/me/avatar"),
    ("json/time_setting", "Replace with PATCH /settings/display"),
    ("json/language_settings", "Replace with PATCH /settings/display"),
    ("json/left_side_userlist", "Replace with PATCH /settings/display"),
    ("json/notify_settings/change", "Move to PATCH /settings/notifications"),
    ("json/ui_settings/change", "Move to PATCH /settings/ui"),
    ("json/ui_settings/change", "Move to PATCH /users/me/settings/ui"),
    ("json/fetch_raw_message", "Move to GET /messages/(?P<id>)"),
    ("json/update_message", "Move to PATCH /messages/(?P<id>)"),
]

description = """Zulip has a number of "legacy" API URLs that are not properly
available via the Zulip REST API, which are present in
`zproject/legacy_urls.py` in the main Zulip project.  A detailed
descripton of how to do this sort of migraiton is available here:
https://github.com/zulip/zulip-gci/blob/master/tasks/legacy_urls.md.

The URLs you are to migrate for this task are %s; you should migrate
them in the following fashion:

%s.

"""

# Task Type A
for (url, solution) in urls:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Eliminate legacy %s URL.' % (url,),
        description = description % (url, solution),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['showell@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['refactoring', "python"], # free text
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
