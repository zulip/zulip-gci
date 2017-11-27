import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

integrations = [
#  These are new integrations for GCI 2017.
    ('Rollbar', 'provides real-time error alerting and debugging tools for developers'),
    ('StatusPage.io', 'notifies teams when a status page of their app or website has changed'),
    ('Runscope', 'alerts teams when their APIs are broken or slow'),
    ('Honeybadger', 'provides exception and uptime monitoring for Ruby apps'),
    ('Raygun', 'an error and performance monitoring tool for web and mobile apps'),
    ('Opbeat', 'a performance monitoring tool for JavaScript developers'),
    ('Insping', 'monitors websites for downtime and alerts teams when websites go down'),
    #  ('Mailchimp', 'an email marketing tool'),  # Hubot integration exists in main repo
    # ('Zeplin', 'design collaboration')  # couldn't find public API
    # ('InVision', 'a collaborative prototyping app'),  # no API yet: https://support.invisionapp.com/hc/en-us/articles/203730795-Does-InVision-have-an-API-for-integration
    # ('Review Bot', 'an on-line review monitoring tool'),  # contacted for API support; response: integrates through Zapier
]

integrations_uploaded = [
    ('Facebook', "the biggest social media and networking platform; "
                 "use Facebook's graph API to build a webhoook"),
    ('Groove', 'a customer support tool for personal support of each customer'),
    ('Intercom', 'helps businesses track how users are interacting with their software'),
]

description = """A [Zulip integration](https://zulipchat.com/integrations/) is a special
type of bot that brings information from the outside world into Zulip. Help
add integrations to Zulip!

Instructions for all integrations tasks are at
https://github.com/zulip/zulip-gci/blob/master/tasks/webhook-integrations.md.

"""

description_A = description + "For this task, do **Task Type A**."
description_BCD = description + "For this task, do **Task Type %(type)s** for " + \
                  "the **%(integration)s** integration (%(desc)s)."
description_E = description + "For this task, do **Task Type E** for " + \
                "the webhook integrations {webhooks[0]}, {webhooks[1]} and {webhooks[2]}."

# This task has already been uploaded for 2017
if False:
    # Task Type A
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Learn how Zulip integrations work.',
        description = description_A,
        status = 2, # 1: draft, 2: published
        max_instances = 100,
        mentors = ['jerryguitarist@gmail.com', 'robhoenig@gmail.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 3, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/webhook-integrations.md",
        private_metadata = "webhook-integrations-A",
        do_upload = args.force)

for integration, desc in integrations:
    # Task Type B
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Investigate how the %s integration should work.' % (integration,),
        description = description_BCD % {'type': 'B', 'integration': integration, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['jerryguitarist@gmail.com', 'robhoenig@gmail.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [5],
        time_to_complete_in_days = 3, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/webhook-integrations.md",
        private_metadata = "webhook-integrations-B",
        do_upload = args.force)

    # Task Type C
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Write code to add a %s integration to Zulip.' % (integration,),
        description = description_BCD % {'type': 'C', 'integration': integration, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['jerryguitarist@gmail.com', 'robhoenig@gmail.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 5, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/webhook-integrations.md",
        private_metadata = "webhook-integrations-C",
        do_upload = args.force)

    # Task Type D
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Add user documentation for the %s integration.' % (integration,),
        description = description_BCD % {'type': 'D', 'integration': integration, 'desc': desc},
        status = 2, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['jerryguitarist@gmail.com', 'robhoenig@gmail.com'],
        tags = ['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [3],
        time_to_complete_in_days = 3, # must be between 3 and 7
        external_url = "https://github.com/zulip/zulip-gci/blob/master/tasks/2017/webhook-integrations.md",
        private_metadata = "webhook-integrations-D",
        do_upload = args.force)

webhook_docs_uploaded = [
    ('airbrake', 'appfollow', 'basecamp'),
    ('bitbucket', 'bitbucket2', 'circleci'),
    ('codeship', 'crashlytics', 'delighted'),
    ('gci', 'github', 'gitlab'),
    ('gogs', 'gosquared', 'greenhouse'),
    ('hellosign', 'helloworld', 'heroku'),
    ('homeassistant', 'ifttt', 'jira'),
    ('librato', 'mention', 'newrelic'),
    ('opsgenie', 'pagerduty', 'papertrail'),
    ('pingdom', 'pivotal', 'semaphore'),
    ('sentry', 'slack', 'solano'),
    ('splunk', 'stripe', 'taiga'),
    ('teamcity', 'transifex', 'travis'),
    ('trello', 'updown', 'yo'),
    ('wordpress', 'zapier', 'zendesk'),
]

webhook_docs = []

# Task Type E
for webhooks in webhook_docs:
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name='Organize docs into numbered steps for the webhooks {webhooks[0]}, {webhooks[1]}, and {webhooks[2]}'.format(
            webhooks=webhooks),
        description=description_E.format(webhooks=webhooks),
        status=2, # 1: draft, 2: published
        max_instances=1,
        mentors=['jerryguitarist@gmail.com', 'robhoenig@gmail.com'],
        tags=['python', 'integrations'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories=[3],
        time_to_complete_in_days=3, # must be between 3 and 7
        external_url="https://github.com/zulip/zulip-gci/blob/master/tasks/2017/webhook-integrations.md",
        private_metadata="webhook-integrations-E",
        do_upload=args.force
    )

if not args.force:
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
