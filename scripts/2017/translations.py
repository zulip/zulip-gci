import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

# Add customized task for Japanese and Korean, as these are mostly fully translated,
# but have no style guides.
languages_tasks = [
    ('Arabic', ['A', 'B',]),
    ('French', ['D',]),
    ('Hungarian', ['A', 'B', 'C',]),
    ('Italian', ['A', 'B', 'C',]),
    ('Malayalam', ['A', 'B', 'C',]),
    ('Polish', ['A', 'D',]),
    ('Portuguese', ['B', 'C',]),
    ('Russian', ['A', 'D']),
    ('Serbian', ['A', 'B', 'C',]),
    ('Turkish', ['A', 'B', 'C',]),
]

description = """Help translate Zulip into another language!

Instructions for translations tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/translations.md

"""

description_ABCD = description + "For this task, do **Task Type %(type)s** for " + \
                  "**%(language)s**"
description_E = description + """If you are a native speaker of a language that
does not have a style guide yet and there is no translation task for it, feel
free to propose a language for translation tasks!

Before you claim this task, ask on Zulip `GCI tasks` stream to check that an
appropriate task does not already exist.

Once you get confirmation, claim the task and do **Task Type E**.
"""

for language_tasks in languages_tasks:
    language = language_tasks[0]
    tasks = language_tasks[1]
    if 'A' in tasks:
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = '%s: Research web application translations' % (language),
            description = description_ABCD % {'type': 'A', 'language': language},
            status = 2, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['robhoenig@gmail.com'],
            tags = ['translation'], # free text
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [3, 5],
            time_to_complete_in_days = 5, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
            private_metadata = "translations-A",
            do_upload = args.force)

    if 'B' in tasks:
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = '%s: Write general translation rules' % (language),
            description = description_ABCD % {'type': 'B', 'language': language},
            status = 2, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['robhoenig@gmail.com'],
            tags = ['translation'], # free text
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [3],
            time_to_complete_in_days = 5, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
            private_metadata = "translations-B",
            do_upload = args.force)

    if 'C' in tasks:
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = '%s: Translate special terms used in Zulip' % (language),
            description = description_ABCD % {'type': 'C', 'language': language},
            status = 2, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['robhoenig@gmail.com'],
            tags = ['translation'], # free text
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [3],
            time_to_complete_in_days = 5, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
            private_metadata = "translations-C",
            do_upload = args.force)

    if 'D' in tasks:
        upload_task(
            # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
            name = '%s: Improve style guide' % (language),
            description = description_ABCD % {'type': 'D', 'language': language},
            status = 2, # 1: draft, 2: published
            max_instances = 1,
            mentors = ['robhoenig@gmail.com'],
            tags = ['translation'], # free text
            is_beginner = False,
            # 1: Coding, 2: User Interface, 3: Documentation & Training,
            # 4: Quality Assurance, 5: Outreach & Research
            categories = [3],
            time_to_complete_in_days = 5, # must be between 3 and 7
            # Field currently not accessible via API. gci-support says it is coming soon.
            # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
            private_metadata = "translations-D",
            do_upload = args.force)

# Task Type E
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Translations: Propose a language',
    description = description_E,
    status = 2, # 1: draft, 2: published
    max_instances = 10,
    mentors = ['robhoenig@gmail.com'],
    tags = ['translation'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [3],
    time_to_complete_in_days = 5, # must be between 3 and 7
    # Field currently not accessible via API. gci-support says it is coming soon.
    # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md",
    private_metadata = "translations-E",
    do_upload = args.force)

if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
