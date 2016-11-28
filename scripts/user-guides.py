import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

features = [
    # Account Basics
    ("Edit Your Profile", "https://get.slack.help/hc/en-us/articles/204092246-Edit-your-profile"),
    ("Manage Your Password", "https://get.slack.help/hc/en-us/articles/201909068-Manage-your-password"),
    ("Change Your Name", "https://get.slack.help/hc/en-us/articles/216360827-Change-your-username"),
# This feature isn't completed yet
#    ("Change Your Email Address", "https://get.slack.help/hc/en-us/articles/207262907-Change-your-email-address"),
    ("Zulip Glossary", "https://get.slack.help/hc/en-us/articles/213817348-Slack-glossary"),
    ("Sign In", "https://get.slack.help/hc/en-us/articles/212681477-Sign-in-to-Slack"),
    ("Sign Out", "https://get.slack.help/hc/en-us/articles/214613347-Sign-out-of-Slack"),
    # Messages
    ("Change Language", "https://get.slack.help/hc/en-us/articles/215058658-Slack-in-different-languages"),
    ("Format Your Messages", "https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages"),
    ("Emoji and Emoticons", "https://get.slack.help/hc/en-us/articles/202931348-Emoji-and-emoticons"),
    ("Edit Messages", "https://get.slack.help/hc/en-us/articles/202395258-Edit-or-delete-messages"),
    ("Mention a Team Member", "https://get.slack.help/hc/en-us/articles/205240127-Mention-a-team-member"),
    ("Message Display Settings", "https://get.slack.help/hc/en-us/articles/213893898-Change-your-message-display-settings"),
    # Streams & Private Messages
    ("Streams and Private Messages", "https://get.slack.help/hc/en-us/articles/201925108-About-channels-and-direct-messages"),
    ("Browse and Join Streams", "https://get.slack.help/hc/en-us/articles/205239967-Browse-and-join-channels"),
    ("Create a Stream", "https://get.slack.help/hc/en-us/articles/201402297-Create-a-channel"),
    # Files
    ("Upload and Share Files", "https://get.slack.help/hc/en-us/articles/201330736-Upload-and-share-files"),
    # Tools & Customization
    ("Search for Messages", "https://get.slack.help/hc/en-us/articles/202528808-Search-for-messages-and-files"),
    ("Advanced Search", "https://get.slack.help/hc/en-us/articles/213532017-Advanced-search-in-Slack"),
    ("Keyboard Shortcuts", "https://get.slack.help/hc/en-us/articles/201374536-Slack-keyboard-shortcuts"),
]

description = """Good user guides help users and search engines discover Zulip features.
Help write user guides for Zulip!

Instructions for all user documentation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md.

"""

description_A_and_B = description + "For this task, do Task Type A for the **%s** feature.\n" + \
"Slack's guide for this feature is at %s."
description_C = description + "For this task, do **Part 3** for any three features."

for feature, slack_link in features:
    # Part 1
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write a user guide for the %s feature.' % (feature,),
        description = description_A_and_B % (feature, slack_link),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['sonaligpt0@gmail.com', 'christie@authenticengine.com',
                   'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
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

    # # Part 2
    # upload_task(
    #     name = 'Polish an existing user guide for a feature.',
    #     description = description_A_and_B % (2, feature, slack_link),
    #     # Note: this should be released as a draft, and published only after Part 1 is done
    #     status = 1, # 1: draft, 2: published
    #     max_instances = 1,
    #     mentors = ['sonaligpt0@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
    #     tags = ['documentation', 'user guides'], # free text
    #     is_beginner = False,
    #     # 1: Coding, 2: User Interface, 3: Documentation & Training,
    #     # 4: Quality Assurance, 5: Outreach & Research
    #     categories = [3],
    #     time_to_complete_in_days = 3, # must be between 3 and 7
    #     # Field currently not accessible via API. gci-support says it is coming soon.
    #     external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
    #     private_metadata = "user-guides-B",
    #     do_upload = args.force)

# Part 3
# Don't upload yet, wait for some guides to be written
# upload_task(
#     name = 'Test and review user guides.',
#     description = description_C,
#     # Note: these should be released as drafts, and published only as we
#     # get Part 2's completed
#     status = 1, # 1: draft, 2: published
#     max_instances = 10,
#     mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
#     tags = ['documentation', 'user guides'], # free text
#     is_beginner = False,
#     # 1: Coding, 2: User Interface, 3: Documentation & Training,
#     # 4: Quality Assurance, 5: Outreach & Research
#     categories = [3, 4],
#     time_to_complete_in_days = 3, # must be between 3 and 7
#     # Field currently not accessible via API. gci-support says it is coming soon.
#     external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
#     private_metadata = "user-guides-C",
#     do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
