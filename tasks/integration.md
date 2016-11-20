# GCI Tasks: Incoming Webhook Integrations

A [Zulip integration](https://zulipchat.com/integrations/) is a special type of bot that brings information from the outside world into Zulip. Zulip integration allows teams to stay up-to-date on code changes, issue tickets, build system results, tweets, and more. Zulip currently has over 50 integrations (example: Twitter , GitHub). It would be fun to add more as there are at least 50 more remaining to be written.

The instructions given below will guide you how to play around with some cool integrations. Feel free to choose any integration that you find particularly interesting (scroll down to find a list of possible new integrations). The tasks given below must be done in the same order. 

See [this](https://github.com/zulip/zulip/pull/324/files) for an **example**.

## Task 0  - Create a personalized integration 
Follow the tutorial below to create a duplicate of our [HelloWorld integration](http://zulip.readthedocs.io/en/latest/integration-guide.html#hello-world-webhook-walkthrough) that is named after yourself, and sends a unique message you’d like to share with the world. As you’re going through the tutorial, take notes on where you got stuck or needed to look up terminology. 
### Instructions

* Set up your virtual development environment
  
  [TODO] Add instructions for the quick new setup here.
* Create a new directory `zerver/fixtures/<your_name>`. Replace the placeholder `<your_name>` with your own name here
* Add a json file to this directory `zerver/fixtures/<your_name>/<your_name>_hello.json`  that contains fixtures like:
  ```
    {
      "featured_title":"Harry Potter",
      "featured_url":"https://en.wikipedia.org/wiki/Harry_Potter",
    }
  ```

* Add a new file `zerver/views/webhooks/<your_name>.py` 
* Copy the contents of the `helloworld.py` to this file. Edit some sections:
  ```
    # First alphabet in <your_name> should be capitalized.
    @api_key_only_webhook_view('<your_name>') 
  ```
  ```
    # Replace <your_name> in function name with your name having the first alphabet in lowercase.
    def api_<your_name>_webhook(request, user_profile, client,
                               payload=REQ(argument_type='body'),
                               stream=REQ(default='test'),
                               topic=REQ(default='<your_own_topic')): #Edit topic here.
  ```
  Play around with the `body` of the message. This is the message that you will send out

* Open `zerver/lib/integrations.py` and look for the lines beginning with:
  ```
    WEBHOOK_INTEGRATIONS = [
  ```
  At the end of this section, add
  ```
    WebhookIntegration('<your_name>', display_name='<your_name>'),  
  ```

* Run the server using vagrant - `/srv/zulip/tools/run-dev.py` . This will start your development server at     
  [http://localhost:9991/](http://localhost:9991/)
  
  [TODO] Update instructions on how to run the server.  
* Create a bot under `Your Bots` section of your Zulip user’s `Settings` page and copy the API key. Replace the placeholder  `<api_key>` in the code below with your real API key and `<your_name>` with your own name

  ```
  (zulip-venv)vagrant@vagrant-ubuntu-trusty-64:/srv/zulip$./manage.py send_webhook_fixture_message --    
  fixture=zerver/fixtures/<your_name>/<your_name>_hello.json '--url=http://localhost:9991/api/v1/external/<your_name>   
  api_key=<api_key>'   
 ``` 

### Submit

* Two screenshots:
 * Take a screenshot of the message you will get on the terminal after you finish your task. It should look something like:
 ``` 
    2016-11-18 15:58:04,600 INFO     127.0.0.1       POST    200 643ms (mem: 34ms/16) (md: 155ms/1) (db: 166ms/15q) (+start: 18ms) /api/v1/external/<your_name> (<bot_name>-bot@zulip.com via Zulip<your_name>Webhook)
```
 * On your local server, you will see a new message in the `test` stream. Take a screenshot of the message.
* Notes on where you got stuck or were confused as well as a link to your cool new integration!

### Type 
Quality assurance, Coding
### Level 
Beginner

## Task 1 - Test integration with Slack
Follow the tutorial below to test how the integration that you intend to add works with Slack. You will also debug the webhook requests and generate payloads.

### Instructions
* Create a test team with [Slack](https://slack.com/) by filling out all the required fields
* Select the integration that you wish to add to Zulip and create a test account at the integration site. [ Note: Choose an   integration from the list provided. In case, you wish to add an integration of your own choice, make sure you confirm with   the mentors once before starting.]
* Add this integration to your Slack account, and play around with it to figure out what information is getting posted
* Take screenshots of all the different types of messages you can generate. Make a brief note about any messages you think     are possible, but which you are unable to generate (e.g. because they are only available to paying customers)
* Under the API section on your integration’s site, you will find an account callback where you can enter the test URL and     get the webhook payloads (i.e. the actual data that the webhook posts to the provided URL) generated for all the message     types above. Use [RequestBin](http://requestb.in/) or a similar site to generate the test URL. If using RequestBin, you     will see something like:

 ![picture alt](http://i1376.photobucket.com/albums/ah27/reyhav/GCI-ss01_zpse7ypdjrr.png "Title is optional")

  Extract the required information from the payloads generated

* Put the webhook payloads generated for your integration in files having some illustrative names under    `zerver/fixtures/<integration_name>/`, where the placeholder `<integration_name>` should be replaced by the actual name   of your integration
* Open a pull request to add files to the zulip-gci project

### Submit

* Minimum three screenshots for the messages generated. Place the screenshots and notes in a new GitHub issue at               https://github.com/zulip/zulip-gci/issues/new
* Link to the pull request containing the required changes should be present here - https://github.com/zulip/zulip-gci/pulls

### Type
Outreach/Research
### Level
Intermediate

## Task 2 - Handlers and tests for your integration
Follow the tutorial below to write and test webhook handlers and tests for the integration using the webhook payloads capture while testing the integration with Slack.

### Instructions
* As you complete Task 1, make sure you have your development environment running and webhook payloads already saved
* Create file(s) `zerver/fixtures/<integration_name>/<integration_name>_<message_type>.json` to create a set of test           fixtures for your integration by using the captured payloads. Replace the placeholder `<integration_name>` by the actual       name and `<message_type>` by the message type you are creating the test fixture for
* Scrum through the files containing fixtures and handlers for existing integrations like `stash.py` or `zendesk.py` to       understand how to link your fixtures to handlers.
* Write a webhook handler for the integration in a file `zerver/views/webhooks/<integration_name>.py` 
* Open `zerver/lib/integrations.py` and look for the lines beginning with:
  
  ```
    WEBHOOK_INTEGRATIONS = [
  ```
  
  In this section, add yours in the alphabetically correct place like: 
  
  ```
    WebhookIntegration('<integration_name>', display_name='<integration_name>'),  
  ```
  
* Test the handler by doing something like:
  
  ```
    (zulip-venv)vagrant@vagrant-ubuntu-trusty-64:/srv/zulip$
    ./manage.py send_webhook_fixture_message --                     
     fixture=zerver/fixtures/<integration_name>/<integration_name>_<message_type>.json '--
     url=http://localhost:9991/api/v1/external/<integration_name>?api_key=<api_key>'
  ```
  
  Replace the placeholder `<api_key>` with the real API key of the bot you create on the local development server (like in       Task 0)
* Take the screenshot of the output message obtained on the local development server and the terminal
* Follow this [guide](http://zulip.readthedocs.io/en/latest/testing-with-django.html) to write tests for your fixtures in a   new file called `zerver/tests/webhooks/test_<integration_name>.py` 
* Once you have written tests, you can run just these new tests from within the Zulip dev environment with this command:
  
  ```
  (zulip-venv)vagrant@vagrant-ubuntu-trusty-64:/srv/zulip$ ./tools/test-backend               
  zerver.tests.webhooks.test_<integration_name>
  ```
  
* Take a screenshot if all your tests pass and your terminal says something like:
  
  ```
  Running zerver.tests.webhooks.test_<integration_name>.<integration_name>Tests.test_<test_1>
  Running zerver.tests.webhooks.test_<integration_name>.<integration_name>Tests.test_<test_2>
  ....
  DONE!
  ```

### Submit

Three screenshots:
*  two for the webhook handlers (described in step 7)
*  one indicating that the tests run fine (described in step 10)

### Type
Coding
### Level
Advanced 

## Task 3 - Document and add your integration
Follow this tutorial to add an end-user documentation for your new webhook integration and submit a pull request.

### Instructions 
* Add a logo image for your integration under the `static/images/integrations/logos/<integration_name>.png`, where    
  `<integration_name>` is the name of the integration, all in lower case
* Generate a message sent by the integration(same as step 6 of Task 2) by giving your test bot a nice name like       
  “`<integration_name>` Bot”, use the project’s logo as the bot’s avatar, and take the screenshots showing the stream/topic   bar for the message, not just the message body, doing something like:
  
  ```
  ./manage.py send_webhook_fixture_message --     
  fixture=zerver/fixtures/<integration_name>/<integration_name>_<message_type>.json url=/api/v1/external/<integration_name>?   stream=<stream_name>&api_key=<api_key>'
  ```
  
  Take a **screenshot** and save it as `/static/images/integrations/<integration_name>/<name>.png` where `name` could be any   name you want to give to your screenshot

* Open the file `templates/zerver/integrations.html` . Read through the contents and try to understand how the page, that is   displayed for your webhook from the Integrations page, is being generated (e.g https://zulipchat.com/integrations/)
* In this file, now add an `integration-instructions` class block also in the alphabetically correct place, explaining all     the steps required to setup the integration, including what URLs to use, etc. like:
  ```
    <div id="<integration_name>" class="integration-instructions">
    
        <p>Learn how Zulip integrations work with this example!</p>
    
        <p>The  webhook will use the <code>test<code> stream, which is
        created by default in the Zulip dev environment. If you are running
        Zulip in production, you should make sure this stream exists.</p>
        ...
        ...
     <!-- ADD MORE DETAILS. See example: http://zulip.readthedocs.io/en/latest/integration-guide.html#step-4-create-documentation -->
        ...
        ...
        <img class="screenshot" src="/static/images/integrations/<integration_name>/<name>.png" />
    </div>
  ```
  The image source in the above section should link the screenshot taken in step 2
* Run all the tests once to verify that everything is working fine by doing `./tools/test-all` 
* Take a look through your code to verify that it follows Zulip’s [Code styles and conventions](http://zulip.readthedocs.io/en/latest/code-style.html)
* Open a pull request to add files to the zulip-gci project

### Submit

Link to the pull request containing all the required changes should be present here - https://github.com/zulip/zulip-gci/pulls

### Type
Documentation , Quality assurance
### Level
Intermediate 

## Possible new integrations

Here is the list of some popular webhooks:

* HelloSign:  E-signing tool
* AppFollow: Monitors appstore activity
* Mention: Media monitoring tool
* GoSquared: Real time analytics
* Mailchimp: Email marketing
* InVision: Collaborative prototyping app
* Heroku: Cloud hosting and deployment
* Stripe: Online payments
* Papertrail: Log management
* Zeplin: Design collaboration

Want to explore more? You can check out hundreds of integrations available [here](http://www.slack.com/apps). Before deciding to work on any of these, please ensure that we intend to add your chosen integration to Zulip. You can then start working to add your favorite one.

[TODO] Update the list regularly as the contest goes on. 

## General Notes

* Try to follow these tasks in proper order
* Remember to change the integration’s name in the instructions above wherever required  
* Read out the comments for all the code sections present in the instructions carefully
* Express interest in one or more integrations either through GitHub comments or on the Zulip chat before taking it up just to ensure that no two participants work on the same task at a given time
* The commit with the changes should have no other cleanup. If you end up making other code changes while doing this task, please put it in a separate commit
* You are advised not to use abbreviations and follow professional language throughout

## Resources

* More **examples** (such as GitLab, Librato etc.) can be found [here](https://github.com/zulip/zulip/pulls?q=is%3Apr+Add+integration+is%3Aclosed+author%3ATomaszKolek)
* Webhook Integration Guide - http://zulip.readthedocs.io/en/latest/integration-guide.html#writing-a-new-integration
* Git and GitHub Guide - http://zulip-ck.readthedocs.io/en/1754-docs-add-git-workflow/git-guide.html
* Documentation Guide - http://zulip.readthedocs.io/en/latest/integration-guide.html#documenting-your-integration
