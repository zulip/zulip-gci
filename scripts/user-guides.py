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

features = [
    # Account Basics
    'Change your avatar', 'Change the date and time format',
    'Join a Zulip organization', 'Sign in to Zulip', 'Deactivate your account',
    # Messages - Sending
    'Send a stream message', 'Send a private message', 'Preview your message before sending',
    'Attach a file to a message', 'Restore the last unsent message',
    'Automatically link to an external issue tracker',
    'Add a link preview', 'Enable or disable pressing enter to send',
    'Verify that your message has been successfully sent',
    'What to do if the server returns an error', 'Send a status message',
    'Make an announcement', 'Send a message in a different language', 'Reply to a message',
    # Messages - Reading
    'View the Markdown source of a message', 'View the exact time a message was sent',
    'View information about the message sender', 'View an image at full size',
    'Collapse a message', 'Star a message', 'Share a message or conversation',
    # Messages - Editing
    'Edit or delete a message', 'Change the topic of a message',
    'Change the topic of a group of messages',
    # People
    'See whether someone is here or away', 'Invite a friend to Zulip',
    'Send someone a private message', 'Send a group of people a private message',
    # Streams & Topics
    'About streams and topics', 'Browse and join streams',
    'View your current stream subscriptions', 'View messages from a stream',
    'The #announce stream', 'Add or invite someone to a stream',
    'Change the stream description', 'Rename a stream', 'Preview a stream',
    'Unsubscribe from a stream', 'Change who can join a stream', 'Pin a stream',
    'Change the color of a stream', 'Send an email to a stream', 'Remove someone from a stream',
    'Delete a stream',
    # Apps
    'Use Zulip on Mac OS', 'Use Zulip on Linux', 'Use Zulip on Windows', 'Use Zulip on Android',
    'Use Zulip on iOS', 'Use Zulip in a terminal',
]

# Posted Dec 13 (then unposted)
# features_round2 = [
#     # Account Basics
#     ("Join a Zulip Organization", "https://get.slack.help/hc/en-us/articles/212675257-Join-a-Slack-team"),
#     ("Learn about Away Statuses", "https://get.slack.help/hc/en-us/articles/201864558-Set-your-Slack-status"),
#     # Messages
#     ("Send and Read Messages", "https://get.slack.help/hc/en-us/articles/201457107-Send-and-read-messages"),
#     ("Make an Announcement", "https://get.slack.help/hc/en-us/articles/202009646-Make-an-announcement"),
#     # Streams & Private Messages
#     ("Private Messages and Group PMs", "https://get.slack.help/hc/en-us/articles/212281468-Direct-messages-and-group-DMs"),
#     ("The #announce Stream", "https://get.slack.help/hc/en-us/articles/220105027-The-general-channel"),
#     ("Organize your Streams", "https://get.slack.help/hc/en-us/articles/212596808-Organize-your-channels-and-direct-messages"),
#     ("Invite Members to a Stream", "https://get.slack.help/hc/en-us/articles/201980108-Invite-team-members-to-a-channel"),
#     ("Set a Stream Description", "https://get.slack.help/hc/en-us/articles/201654083-Set-a-channel-topic-or-purpose"),
#     ("Unsubscribe from a Stream", "https://get.slack.help/hc/en-us/articles/201375146-Leave-a-channel"),
#     # Notifications
#     ("Set up Zulip Notifications", "https://get.slack.help/hc/en-us/articles/201895138-Set-up-Slack-notifications"),
#     ("Mute a Stream", "https://get.slack.help/hc/en-us/articles/201563847-Archive-a-channel"),
#     ("Add a Custom Alert Word" , "https://get.slack.help/hc/en-us/articles/201398467-Highlight-word-notifications"),
# ]



description = """Good user guides help users and search engines discover Zulip features.
Help write user guides for Zulip!

Instructions for all user documentation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md.

"""

description_A_and_B = description + "For this task, do Task Type A for the **%s** feature."
description_C = description + "For this task, do **Part 3** for any three features."

for feature in features:
    # Part 1
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write a user guide for the %s feature.' % (feature,),
        description = description_A_and_B % (feature,),
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
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
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
    #     # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
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
#     # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
#     private_metadata = "user-guides-C",
#     do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
