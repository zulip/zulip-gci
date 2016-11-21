import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """Zulip allows users to create custom bots and integrations, and those bots need avatars to help make the product more fun! Zulip would like to provide a library of cute custom avatars that users can choose from when creating a new bot. Our non-custom avatars look like https://chat.zulip.org/integrations/, basically the logos of products that Zulip integrates with.

The avatars should look good at the 50x50px size at which the user avatars are displayed in the Zulip web application. Use your creativity! For example, an avatar for a bot for logging software could be designed based on either its function or a pun around the word “logging”, e.g.:

    An image of a few lines of log text
    A pile of wooden logs
    A cute robot with all its limbs made of logs

"""
description_part_1 = description + "For this task, find a list of online repositories of cute bot images with a clear open source license, such as Creative Commons. Pick out 5-10 images from each that you think might be a good fit for a Zulip bot."

description_part_2 = description + """For this task, design 3-5 avatar images that fit together thematically (e.g. similar visual style), inspired by some of the potential bot cases listed at [1]. They should look good at 50x50px size. It's okay for these to be quick prototypes; it makes sense to spend a lot of time making them really good once you've gotten feedback on which design directions others like.

[1]: https://github.com/zulip/zulip-gci/blob/bfad3be590380573743d0ddb3b9e918aba36fc0f/tasks/bot-avatars.md#example-bots"""

description_part_3 = description + """For this task, Refine one collection of avatar images that you or another contributor have contributed to the project and add touches to make it look really nice. The goal here is to take a set of prototype avatars that you’ve gotten feedback on and then make it look really good so that we can include it in the project.

Please note: Do not submit images found on the Internet for this; you must design the image yourself, unless those images have a clear open source license.

Please design your avatar logos using a file format such as .svg that supports being arbitrarily resized; while avatars will be displayed at 50x50px size in most machines, we will likely want to have a way to see a high-resolution version of the avatar. If your avatar is not conducive to a svg format, a 300x300px bitmap is also fine.
"""

for feature in features:
    # Part 1
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Find open source images that can be used as a bot avatar',
        description = description_part_1,
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['arpith@feedreader.co', 'niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['outreach', 'research'], # free text
        is_beginner = True,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "bot-avatars",
        do_upload = args.force)

    # Part 2
    upload_task(
        name = 'Design prototype bot avatars'
        description = description_parts_2,
        # Note: this should be released as a draft, and published only after Part 1 is done
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['arpith@feedreader.co', 'niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['user interface'], # free text
        is_beginner = True,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [2],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "bot-avatars",
        do_upload = args.force)

# Part 3
for i in range(10):
    upload_task(
        name = 'Refine bot avatars',
        description = description_part_3,
        # Note: these should be released as drafts, and published only as we
        # get Part 2's completed
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['arpith@feedreader.co', 'niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['user interface'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [2],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "bot-avatars",
        do_upload = args.force)


if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
