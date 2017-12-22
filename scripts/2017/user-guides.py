import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

def create_list(bullets):
    markdown = ''
    for bullet in bullets:
        markdown += '* ' + bullet + '\n'
    return markdown

features = [
    'Add a link preview',
    'Configure authentication methods',
]

features = []

features_review = [
    ("Guides", ["Getting started with Zulip", "Setting up your organization"]),
    ("Account Basics, Part 1", ["Change your name", "Change your email address", "Manage your password", "Edit your settings",
                                "Set your avatar", "Change your default language", "Use 24-hour time"]),
    ("Account Basics, Part 2", ["Joining an organization", "Signing in", "Signing out", "Keyboard shortcuts", "Deactivate your account", "Zulip glossary", "The Zulip browser window"]),
    ("Sending Messages, Part 1", ["Send a stream message", "Private messages", "Send a private message", "Group private messages", "Format your message using Markdown",
                                  "Preview your message before sending", "Message drafts"]),
    ("Sending Messages, Part 2", ["Emoji", "Video calls", "Share and upload files", "Manage your uploaded files", "Enable pressing Enter to send", "Verify a message was sent", "Status messages"]),
    ("Sending Messages, Part 3", ["@-mention a user", "Make an announcement", "Write in a different language", "Reply to a message", "Edit or delete a message",
                                  "Edit the topic of a message", "Message a stream by email"]),
    ("Reading Messages, Part 1", ["Navigation and unread counts", "View the Markdown source of a message", "View the exact time a message was sent", "View an image at full size",
                                  "Collapse a message", "Star a message", "Emoji reactions"]),
    ("Reading Messages, Part 2", ["Share a message or conversation", "Advanced search", "View a message's edit history", "View messages from a stream", "View messages from a topic",
                                  "View messages from a user", "View messages containing files or links"]),
    ("People", ["Check whether someone is on-line", "Invite another user"]),
    ("Streams & topics, Part 1", ["About streams and topics", "Browse and subscribe to streams", "Create a stream", "View your stream subscriptions", "Add someone to a stream",
                                  "Change the stream description", "Rename a stream"]),
    ("Streams & topics, Part 2", ["Unsubscribe from a stream", "Change the privacy of a stream", "Organize the Streams sidebar", "Pin a stream", "Change the color of a stream",
                                  "Message a stream by email"]),
    ("Notifications, Part 1", ["Mute a stream", "Mute a topic", "Set notifications for a single stream", "Desktop notifications", "Audible notifications"]),
    ("Notifications, Part 2", ["Email notifications", "Mobile notifications", "Digest emails", "Add an alert word"]),
    ("Tools & customization", ["Bots and integrations", "Enable high contrast mode", "Display the buddy list on narrow screens", "View organization statistics"]),
    ("Apps", ["Installation guides", "Tips for Zulip on Windows", "Tips for Zulip on Android"]),
    ("Organization basics, Part 1", ["Change your organization name", "Change your organization description", "Change your organization avatar", "Update your organization's settings",
                                     "Link to your Zulip from the web"]),
    ("Organization basics, Part 2", ["Import users and channels from Slack", "Restrict new users by email domain", "Allow joining without an invitation", "Manage who can send invitations",
                                     "Set the default language for new users"]),
    ("Organization settings, Part 1", ["Restrict stream creation", "Change who can add custom emoji", "Block image and link previews", "Prevent users from changing their name",
                                       "Prevent users from changing their email"]),
    ("Organization settings, Part 2", ["Disable message edit history", "Manage editing of old messages", "Require topics in stream messages", "Add custom emoji", "Add a custom linkification filter"]),
    ("Users & bots", ["Deactivate or reactivate a user", "Deactivate or reactivate a bot", "Make a user an administrator", "Change a user's name", "View all bots in your organization"]),
    ("Streams management", ["Delete a stream", "Set default streams for new users", "Rename a stream", "Change a stream's description", "Change the privacy of a stream", "Add someone to a stream",
                            "Remove someone from a stream"]),
]

features_review = []

description = """Good user guides help users and search engines discover Zulip features.
Help write and edit user guides for Zulip!

Instructions for all user documentation tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/user-guides.md.

"""

description_A = description + "For this task, do Task Type A for the **%s** feature."
description_B = description + "For this task, do Task Type B for the following features:\n"

# Task Type A
for feature in features:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write a user guide for the * %s * feature.' % (feature,),
        description = description_A % (feature,),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['joshuapan8@gmail.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3, 5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        private_metadata = "user-guides-A",
        do_upload = args.force)

# Task Type B
for name, features in features_review:
    upload_task(
        name = 'Review user guides: %s.' % name,
        description = description_B + create_list(features),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['joshuapan8@gmail.com'],
        tags = ['documentation', 'user guides'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3, 4],
        time_to_complete_in_days = 3, # must be between 3 and 7
        private_metadata = "user-guides-B",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
