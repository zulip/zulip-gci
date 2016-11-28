import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

features = [
    ("Edit Messages", "https://get.slack.help/hc/en-us/articles/202395258-Edit-or-delete-messages"),
    ("Mention a Team Member", "https://get.slack.help/hc/en-us/articles/205240127-Mention-a-team-member"),
    ("Change Language", "https://get.slack.help/hc/en-us/articles/215058658-Slack-in-different-languages"),
    ("Message Display Settings", "https://get.slack.help/hc/en-us/articles/213893898-Change-your-message-display-settings"),
    ("Browse and Join Streams", "https://get.slack.help/hc/en-us/articles/205239967-Browse-and-join-channels"),
]

description = """Good user guides help users and search engines discover Zulip features.
Help write user guides for Zulip!

Instructions for all user documentation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md.

"""

description_A_and_B = description + "For this task, do **Part %s** for the **%s** feature.\n" + \
"Slack's guide for this feature is at %s."
description_C = description + "For this task, do **Part 3** for any three features."

for feature, slack_link in features:
    # Part 1
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write a rough user guide for a feature.',
        description = description_A_and_B % (1, feature, slack_link),
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3, 5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
        private_metadata = "user-guides-A",
        do_upload = args.force)

    # Part 2
    upload_task(
        name = 'Polish an existing user guide for a feature.',
        description = description_A_and_B % (2, feature, slack_link),
        # Note: this should be released as a draft, and published only after Part 1 is done
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
        private_metadata = "user-guides-B",
        do_upload = args.force)

# Part 3
for i in range(10):
    upload_task(
        name = 'Test and review user guides.',
        description = description_C,
        # Note: these should be released as drafts, and published only as we
        # get Part 2's completed
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
        private_metadata = "user-guides-C",
        do_upload = args.force)


if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
