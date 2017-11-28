import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

files_uploaded = [
    ('narrow_state.js', ['exports.is_for_stream_id']),
    ('stream_data.js',  ['exports.name_in_home_view', 'exports.notifications_in_home_view']),
    ('user_groups.js',  ['exports.get_user_group_from_id'])
    ('user_groups.js', ['exports.get_user_group_from_name']),
    ('user_groups.js', ['exports.initialize']),
    ('stream_data.js', ['exports.get_newbie_stream']),
    ('stream_data.js', ['exports.initialize_from_page_params']),
    ('stream_data.js', ['exports.receives_desktop_notifications', 'exports.receives_audible_notifications']),
    ('stream_data.js', ['exports.delete_sub', 'exports.invite_streams']),
    ('stream_data.js', ['exports.get_subscriber_count', 'exports.render_stream_description', 'exports.canonicalized_name']),
    ('stream_data.js', ['exports.get_default_status']),
    ('stream_data.js', ['exports.remove_subscriber', 'exports.user_is_subscribed']),
    ('stream_data.js', ['exports.create_sub_from_server_data']),
    ('stream_data.js', ['exports.remove_default_stream']),
    ('narrow_state.js', ['exports.stream', 'exports.topic']),
    ('narrow_state.js', ['exports.operators', 'collect_single']),
    ('narrow_state.js', ['exports.set_compose_defaults'])
]

files = [
]

description = """Unit tests ensure the quality and correctness of your code, especially when doing
large code refactorings, and prevent regressions. Zulip uses node to unit test its
150+ JavaScript files. Help add test coverage to Zulip!

Instructions for this task are at https://github.com/zulip/zulip-gci/blob/master/tasks/2017/node-coverage.md

"""

description_ext = description + "For this task, you will be testing the file `%(file)s`." + \
                                " The functions that require coverage are:\n\n"

def create_list(bullets):
    markdown = ''
    for bullet in bullets:
        markdown += '* `' + bullet + '`\n'
    return markdown

# **%(bot)s** bot (%(desc)s)."

for file, functions in files:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Increase node coverage for %s.' % (file,),
        description = description_ext % {'file': file} + create_list(functions),
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['joshuapan8@gmail.com'],
        tags = ['testing', 'node', 'javascript'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/node-coverage.md",
        private_metadata = "node-coverage",
        do_upload = args.force)

if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
