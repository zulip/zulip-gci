import argparse
from upload import upload_task

import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

issues = [2990, 3067, 3143, 3013, 3057, 3141, 3134, 2767, 3071, 3126, 3117,
          3131, 2919, 2831, 2809, 3035, 2447, 2740, 2833, 2917, 3038, 3086,
          3140, 3171, 3062]

issues = []

description = """This task is for posting or resolving
the Github issue or pull request referenced in the title.
"""

# Task Type A
for issue in issues:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Special task for #%s' % (issue,),
        description = description,
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['issues'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        private_metadata = "issues",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
