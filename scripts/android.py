import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()


upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the Chat Box',
description = """Write a detailed description about the chatBox (functioning and 
what each button does) with screenshots.

Checklist:
    Include text about the behavior details about swipe to remove and it 
    automatically goes away when the main recyclerView is scrolled.
    Switching between private and stream mode.""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'
           , 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)

upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the Streams Drawer',
description = """An overview descriptive text/Documentation and compiled like 
https://zulip.readthedocs.io/ describing the streams drawer.

Checklist:
Unread counts (Currently there is a bug which is breaking the unread counts, 
	but I hope it would be fixed soon) and it expands and shows the topics of 
that stream. On clicking the Stream name you can directly narrow to that stream.""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com',
 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)



upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation on some miscellaneous features',
description = """An overview descriptive text/Documentation and compiled like 
https://zulip.readthedocs.io/ describing some features.

Checklist:
Include text about the Day/Night mode 
Filtering messages 
More
""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com',
 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)



upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the Widget',
description = """Descriptive text/Documentation and compiled like 
https://zulip.readthedocs.io/ describing the usage with screenshots of the widget.

Checklist:
Update time of receiving messages. 
Narrowed view in the widget.
""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com',
 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)




upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the menu of long click on message',
description = """ Descriptive text/Documentation and compiled like 
https://zulip.readthedocs.io/ describing the options available when long press the message.
With a screenshot of the popup.

Checklist:
Include about documentation about each of the features.""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com', 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)



upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the API routes used in the project',
description = """Descriptive text/Documentation and compiled like
 https://zulip.readthedocs.io/ describing the API routes by the Application.

You can get the information about these API’s at https://zulip.readthedocs.io/

Checklist:
All the API’s used like get_auth_backends and information about the API’s""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com',
 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)



upload_task(
# https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
name = 'Write documentation for the supported backends',
description = """ An descriptive text/Documentation and compiled like 
https://zulip.readthedocs.io/ describing the implemented backends in the app.

You can get the information about these API’s at https://zulip.readthedocs.io/

Checklist:
Include text about the 3 Authentication login backend’s the project handles 
currently which are Email, Google, DevAuth Backend’s.""",
status = 1, # 1: draft, 2: published
max_instances = 1,
mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com',
 'kunall.gupta17@gmail.com'],
tags = ['documentation', 'user guides', 'android'], # free text
is_beginner = True,
# 1: Coding, 2: User Interface, 3: Documentation & Training,
# 4: Quality Assurance, 5: Outreach & Research
categories = [3, 5],
time_to_complete_in_days = 3, # must be between 3 and 7
# Field currently not accessible via API. gci-support says it is coming soon.
external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/android.md",
private_metadata = "android-A",
do_upload = args.force)






if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
