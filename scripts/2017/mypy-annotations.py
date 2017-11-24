import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

tasks_A = [
    ["zerver/lib/test_runner.py", "zerver/views/zephyr.py", "zerver/webhooks/beanstalk/tests.py", "zerver/lib/upload.py"],
    ["zerver/lib/soft_deactivation.py", "zerver/webhooks/papertrail/view.py", "zerver/webhooks/bitbucket2/view.py",
     "zerver/webhooks/basecamp/view.py", "zerver/views/invite.py", "zerver/webhooks/jira/view.py",
     "analytics/management/commands/populate_analytics_db.py", "analytics/tests/test_counts.py", "zerver/webhooks/teamcity/view.py"],
    ["zerver/views/messages.py", "zerver/webhooks/semaphore/view.py"],
    ["zerver/webhooks/travis/view.py", "zerver/lib/create_user.py", "zerver/webhooks/mention/view.py", "zerver/lib/events.py",
     "zerver/webhooks/airbrake/view.py", "zerver/webhooks/yo/view.py", "zerver/webhooks/sentry/view.py"],
    ["zilencer/views.py", "zerver/views/auth.py", "zerver/tests/test_home.py", "zerver/lib/webhooks/git.py", "zerver/lib/request.py"],
    ["zerver/webhooks/zendesk/view.py", "zerver/webhooks/codeship/view.py", "zerver/webhooks/github_webhook/view.py",
     "zerver/webhooks/deskdotcom/view.py", "zerver/webhooks/librato/view.py", "tools/lib/test_server.py", "scripts/lib/node_cache.py",
     "zerver/webhooks/delighted/view.py", "zerver/models.py"],
    ["zerver/webhooks/bitbucket2/tests.py", "zerver/tornado/event_queue.py", "zerver/tests/test_events.py"],
    ["zerver/views/streams.py", "zerver/middleware.py"],
    ["zerver/tests/test_decorators.py", "zerver/webhooks/slack/view.py", "zerver/webhooks/splunk/view.py", "zerver/lib/send_email.py",
     "zerver/views/custom_profile_fields.py", "zerver/tests/test_messages.py", "zerver/webhooks/solano/view.py"],
    ["zerver/webhooks/gogs/tests.py", "zerver/views/users.py", "zerver/webhooks/gitlab/view.py",
     "zerver/management/commands/send_password_reset_email.py", "zerver/webhooks/bitbucket/tests.py"],
    ["zerver/tests/test_management_commands.py", "zerver/views/email_mirror.py", "zerver/views/push_notifications.py",
     "zerver/webhooks/gosquared/view.py", "zerver/lib/test_fixtures.py", "zerver/webhooks/taiga/view.py",
     "analytics/views.py", "zerver/webhooks/helloworld/view.py", "zerver/views/alert_words.py"],
    ["zerver/webhooks/appfollow/view.py", "zerver/webhooks/opsgenie/view.py", "zerver/webhooks/gogs/view.py",
     "zerver/webhooks/ifttt/view.py", "zerver/tests/test_subdomains.py", "zerver/views/typing.py",
     "zerver/webhooks/pingdom/view.py", "zerver/lib/avatar.py", "zerver/webhooks/greenhouse/view.py", "zerver/webhooks/beanstalk/view.py"],
    ["zerver/forms.py", "zerver/webhooks/circleci/view.py", "zerver/webhooks/transifex/view.py",
     "zerver/lib/export.py", "zerver/lib/integrations.py", "zerver/webhooks/bitbucket/view.py"],
    ["zerver/webhooks/homeassistant/view.py", "zerver/webhooks/freshdesk/view.py", "zerver/lib/test_classes.py",
     "tools/lister.py", "zerver/webhooks/newrelic/view.py"],
    ["zerver/decorator.py", "zerver/views/pointer.py", "zerver/tests/test_auth_backends.py"],
    ["zerver/views/user_settings.py", "zerver/webhooks/stripe/view.py", "zerver/webhooks/gitlab/tests.py",
     "zerver/webhooks/crashlytics/view.py", "zerver/webhooks/wordpress/view.py"],
    ["zerver/webhooks/trello/tests.py", "zerver/tests/test_docs.py", "zerver/views/realm_filters.py",
     "zerver/tests/test_subs.py", "zerver/tornado/websocket_client.py", "zerver/tests/test_user_groups.py"],
    ["analytics/lib/fixtures.py", "zerver/views/tutorial.py", "zerver/lib/bugdown/__init__.py", "zproject/backends.py",
     "zerver/webhooks/heroku/view.py", "zerver/webhooks/gci/view.py", "zerver/webhooks/zapier/view.py", "zerver/views/realm.py"]
]

description_A = """Help convert mypy annotations to the Python 3 syntax in the Zulip codebase!
This is a great way to practice git, git grep, and efficiently using a powerful editor.

Instructions for mypy annotation task are at
https://github.com/zulip/zulip-gci/blob/master/tasks/2017/mypy-annotations.md.

For this task, do **Task Type A** for the following set of files:

%s
"""

for files in tasks_A:
    file_list = "\n".join([("* " + file_name) for file_name in files]),
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Update mypy annotations to Python 3 syntax',
        description = description_A % file_list,
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'mypy'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/mypy-annotations.md",
        private_metadata = "mypy-annotations-A",
        do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
