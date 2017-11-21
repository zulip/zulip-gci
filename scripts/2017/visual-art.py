import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

description = """As a group chat app, Zulip uses visual art in many ways - users
can add their own avatars, use emoji reactions, and upload images, videos and
GIFs.

This group of tasks has a high creative potential, as it is all about creating
visual art. You can create your own art in a variety of ways:
- using any editor you already used for creating art on your computer
- using a graphics editor such as [Krita](https://krita.org/en/)
- using a vector art editor such as [Vectr](https://vectr.com/)
- using a pixel art editor such as [Piskel](https://www.piskelapp.com/)
- using an image editor such as [GIMP](https://www.gimp.org/)

Choose a tool that works best for you!

For this task, do **Task Type %(type)s**.
"""

# Task Type A
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Draw user avatars.',
    description = description % {'type': 'A' },
    status = 2, # 1: draft, 2: published
    max_instances = 20,
    mentors = ['rishig@zulipchat.com', 'malavarena@gmail.com'],
    tags = ['art', 'avatars'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [2],
    time_to_complete_in_days = 3, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/visual-art.md",
    private_metadata = "visual-art-A",
    do_upload = args.force)

# Task Type B
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Generate identicons for user avatars.',
    description = description % {'type': 'B' },
    status = 2, # 1: draft, 2: published
    max_instances = 20,
    mentors = ['rishig@zulipchat.com', 'malavarena@gmail.com'],
    tags = ['art', 'avatars', 'python'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1, 2],
    time_to_complete_in_days = 5, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/visual-art.md",
    private_metadata = "visual-art-B",
    do_upload = args.force)

# Task Type C
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Create a custom animated reaction',
    description = description % {'type': 'C' },
    status = 2, # 1: draft, 2: published
    max_instances = 50,
    mentors = ['rishig@zulipchat.com', 'malavarena@gmail.com'],
    tags = ['art', 'GIF', 'animation'], # free text
    is_beginner = True,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [2],
    time_to_complete_in_days = 3, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/visual-art.md",
    private_metadata = "visual-art-C",
    do_upload = args.force)

# Task Type D
upload_task(
    # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
    name = 'Create a standalone animation',
    description = description % {'type': 'D' },
    status = 2, # 1: draft, 2: published
    max_instances = 20,
    mentors = ['rishig@zulipchat.com', 'malavarena@gmail.com'],
    tags = ['art', 'CSS', 'SVG', 'animation'], # free text
    is_beginner = False,
    # 1: Coding, 2: User Interface, 3: Documentation & Training,
    # 4: Quality Assurance, 5: Outreach & Research
    categories = [1, 2],
    time_to_complete_in_days = 5, # must be between 3 and 7
    external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/visual-art.md",
    private_metadata = "visual-art-D",
    do_upload = args.force)


if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
