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
    'About streams and topics', 'View your current stream subscriptions',
    'View messages from a stream', 'The #announce stream', 'Add or invite someone to a stream',
    'Change the stream description', 'Rename a stream', 'Preview a stream',
    'Unsubscribe from a stream', 'Change who can join a stream', 'Pin a stream',
    'Change the color of a stream', 'Message a stream by email', 'Remove someone from a stream',
    'Delete a stream',
    # Apps
    'Use Zulip on Mac OS', 'Use Zulip on Linux', 'Use Zulip on Windows', 'Use Zulip on Android',
    'Use Zulip on iOS', 'Use Zulip in a terminal',
]

features = [
    # Notifications
    'Mute a stream', 'Mute a topic', 'Set notifications for a single stream',
    'Configure desktop notifications', 'Configure audible notifications',
    'Configure email notifications', 'Configure mobile push notifications',
    'Add an alert word',
    # Tools & Customization
    'Keyboard shortcuts', 'Add a bot or integration',
    # Administration - Organization Settings
    "Change your organizations name", 'Restrict user email addresses to certain domains',
    'Allow anyone to join without an invitation', 'Only allow admins to invite new users',
    'Only allow admins to create new streams', 'Restrict editing of old messages and topics',
    'Change the default language', 'Add custom emoji', 'Configure authentication methods',
    'Add a custom linkification filter',
    # Administration - Users & Bots
    'Deactivate or reactivate a user', 'Deactivate or reactivate a bot',
    'Make a user an administrator', "Change a users name", 'View the list of installed bots',
    # Administration - Streams
    'Delete a stream', 'Set default streams for new users', 'Rename a stream',
    "Change a streams description", 'Make a public stream private',
    'Add or remove users from a stream',
]

features = []

features_review = [("Account Basics, Part 1", ["Change your name", "Change your password",
                                               "Change your settings", "Change your avatar",
                                               "Change your language"]),
                   ("Account Basics, Part 2", ["Change the date and time format",
                                               "Move the users list to the left sidebar",
                                               "Signing in", "Signing out",
                                               "Deactivate your account"]),
                   ("Sending Messages, Part 1", ["Send a stream message", "Send a private message",
                                                 "Format your message using Markdown"]),
                   ("Sending Messages, Part 2", ["Preview your message before sending",
                                                 "Add emoji", "Upload and share files"]),
                   ("Sending Messages, Part 3", ["Restore the last unsent message",
                                                 "Enable or disable pressing enter to send",
                                                 "@-mention a team member",
                                                 "Reply to a message"]),
                   ("Reading Messages", ["View the Markdown source of a message",
                                         "View information about a message",
                                         "View the exact time a message was sent",
                                         "View an image at full size",
                                         "Collapse a message", "Star a message"]),
                   ("Editing and Searching Messages", ["Edit or delete a message",
                                                       "Change the topic of a message",
                                                       "Search messages", "Advanced search for messages"]),
                   ("People", ["Invite a friend to Zulip", "Send a group of people a private message"]),
                   ("Streams & Topics, Part 1", ["About streams and topics", "Browse and join streams",
                                                 "Create a stream"]),
                   ("Streams & Topics, Part 2", ["View your current stream subscriptions",
                                                 "View messages from a stream", "The #announce stream"]),
                   ("Streams & Topics, Part 3", ["Add or invite someone to a stream",
                                                 "Change the stream description", "Rename a stream"]),
                   ("Streams & Topics, Part 4", ["Unsubscribe from a stream",
                                                 "Change who can join a stream", "Pin a stream"]),
                   ("Streams & Topics, Part 5", ["Change the color of a stream",
                                                 "Remove someone from a stream", "Delete a stream"]),
                   ("Notifications", ["Mute a stream", "Mute a topic", "Configure desktop notifications",
                                      "Add an alert word"]),
                   ("Organization Settings, Part 1", ["Change your organization's name",
                                                      "Allow anyone to join without an invitation",
                                                      "Only allow admins to invite new users",
                                                      "Restrict editing of old messages and topics"]),
                   ("Organization Settings, Part 2", ["Change the default language for realm",
                                                      "Add custom emoji",
                                                      "Add a custom linkification filter"]),
                   ("Users & Bots", ["Deactivate or reactivate a user", "Deactivate or reactivate a bot",
                                     "Make a user an administrator", "Change a user's name"]),
                   ("Streams", ["Delete a stream", "Set default streams for new users",
                                "Rename a stream", "Make a public stream private"])
]

description = """Good user guides help users and search engines discover Zulip features.
Help write and edit user guides for Zulip!

Instructions for all user documentation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md.

"""

description_A = description + "For this task, do Task Type A for the **%s** feature."
description_B = description + "For this task, do Task Type B for the following features: **%s**."

# Task Type A
for feature in features:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write a user guide for the %s feature.' % (feature,),
        description = description_A % (feature,),
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

# Task Type B
for name, features in features_review:
    upload_task(
        name = 'Review user guides: %s.' % name,
        description = description_B % ', '.join(features),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/user-guides.md",
        private_metadata = "user-guides-B",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
