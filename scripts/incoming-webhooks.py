import argparse
from upload import upload_task

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--force', dest='force', action="store_true", default=False)
args = parser.parse_args()

integration_list = ['HelloSign', 'AppFollow', 'Mention', 'GoSquared', 'Mailchimp', 'InVision', 'Heroku', 'Stripe', 'Papertrail', 'Zeplin']
 
description = { 'T0' : """Start with this task to add a personlized integration. 

This is a great way to learn the basics of python, git workflow and good style and understand how the integrations work with Zulip. You will also research and explore new things!
 
Instructions for integration tasks are at https://[TODO].""" ,
   
               'T1' : """Start with this task to play around your favorite integration. 
               
This is a great way to learn the how your integration works!
         
Instructions for integration tasks are at https://[TODO].""" ,
               
               'T2' : """Understand how the integrations work with Zulip by adding tests and handlers for your integration. 
 
This is a great way to learn the basics of testing, git workflow and good style. 
 
Instructions for integration tasks are at https://[TODO].""" ,
               
               'T3' : """ Add your integration to Zulip and make a mark. . 
               
This is a great way to learn how to write good documentation and understand the basics of git workflow.

Instructions for integration tasks are at https://[TODO]."""
              }

for integration in integration_list:
   # Task 0 
   upload_task(
       # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
       name = 'Create a personalized integration',
       description = description['T0'],
       status = 1, # 1: draft, 2: published
       max_instances = 1,
       mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
       tags = ['python', 'integration'], # free text
       is_beginner = True,
       # 1: Coding, 2: User Interface, 3: Documentation & Training,
       # 4: Quality Assurance, 5: Outreach & Research
       categories = [1, 4],
       time_to_complete_in_days = 3, # must be between 3 and 7
       # Field currently not accessible via API. gci-support says it is coming soon.
       # external_url = "TODO",
       private_metadata = "integration",
       do_upload = args.force)
    
    # Task 1
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Test integration with Slack',
        description = description['T1'],
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'integration'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [5],
        time_to_complete_in_days = 4, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "integration",
        do_upload = args.force)
        
    # Task 2 
    upload_task(
        # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
        name = 'Handlers and tests for your integration',
        description = description['T2'],
        status = 1, # 1: draft, 2: published
        max_instances = 1,
        mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
        tags = ['python', 'integration'], # free text
        is_beginner = False,
        # 1: Coding, 2: User Interface, 3: Documentation & Training,
        # 4: Quality Assurance, 5: Outreach & Research
        categories = [1],
        time_to_complete_in_days = 6, # must be between 3 and 7
        # Field currently not accessible via API. gci-support says it is coming soon.
        # external_url = "TODO",
        private_metadata = "integration",
        do_upload = args.force)
        
    # Task 3  
    upload_task(
         # https://developers.google.com/open-source/gci/resources/downloads/TaskAPISpec.pdf
         name = 'Document and add your integration',
         description = description['T3'],
         status = 1, # 1: draft, 2: published
         max_instances = 1,
         mentors = ['niftynei@gmail.com', 'rishig@zulipchat.com', 'tabbott@zulipchat.com'],
         tags = ['python', 'integration'], # free text
         is_beginner = False,
         # 1: Coding, 2: User Interface, 3: Documentation & Training,
         # 4: Quality Assurance, 5: Outreach & Research
         categories = [3,4],
         time_to_complete_in_days = 4, # must be between 3 and 7
         # Field currently not accessible via API. gci-support says it is coming soon.
         # external_url = "TODO",
         private_metadata = "integration",
         do_upload = args.force)

if not args.force:
    print
    print("No tasks uploaded. Add a -f argument to upload tasks to the GCI website.")
    print("This is not idempotent. Running this twice with -f will create two sets of tasks.")
