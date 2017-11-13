# GCI Tasks: Incoming Webhook Integrations

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) and
  [intro to Zulip server development](https://codein.withgoogle.com/tasks/4799263762546688/) tasks.

## Background

A [Zulip integration](https://zulipchat.com/integrations/) is a special type
of bot that brings information from the outside world into Zulip. Zulip
integrations allow teams to stay up-to-date on code changes, issue tickets,
build system results, tweets, and more. Zulip currently has over 50
integrations, but there are dozens more that would be valuabled to add.

As an example, see [this commit](https://github.com/zulip/zulip/pull/1759)
for the code that added the Sentry integration.

Task Types B/C/D generally require the previous task for that
particular integration to be completed first.

## Task Descriptions

### Task Type A: Create a personalized integration.

Follow the tutorial below to create a duplicate of our
[HelloWorld integration](http://zulip.readthedocs.io/en/latest/integration-guide.html#hello-world-webhook-walkthrough)
that is named after yourself, and sends a unique message you'd like to share
with the world. As you're going through the tutorial, take notes on where
you got stuck or needed to look up terminology.

#### Start the Zulip server

* Start the server. If using vagrant, you can do this by running `/srv/zulip/tools/run-dev.py`.
  This will start your development server at
  [http://localhost:9991/](http://localhost:9991/)
  or "http://put-your-name-here.zulipdev.org:9991/", depending
  on your configuration.

#### Create a bot.

* Create a bot named "Test van Botten" under the `Your Bots` section
  of your Zulip user’s `Settings` page and copy the API key to a
  text file.

#### Create a test fixture

A "test fixture" is a file with sample data in it.  We will use
this file to test our webhook later.

Notation: Everywhere below, `<yourname>` should be replaced by your name in
lowercase (no spaces or underscores), and `<YourName>` should be replaced by
your name in CamelCase.

* Create a new directory `zerver/fixtures/<yourname>`.

* Add a json file to this directory `zerver/fixtures/<yourname>/<yourname>_hello.json`
  that contains fixtures like:
  ```
    {
      "featured_title":"Harry Potter",
      "featured_url":"https://en.wikipedia.org/wiki/Harry_Potter",
    }
  ```

#### Create the webhook

* Add a new file `zerver/views/webhooks/<yourname>.py`

* Copy the contents of the `helloworld.py` to this file. Replace all instances of `HelloWorld` and `helloworld` with `<YourName>` and `<yourname>`, respectively. Also choose a new topic below (replace `<your_topic>`)
  ```
    def api_<yourname>_webhook(request, user_profile, client,
                               payload=REQ(argument_type='body'),
                               stream=REQ(default='test'),
                               topic=REQ(default='<your_topic>')):
  ```
  and play around with the `body`.

* Open `zerver/lib/integrations.py` and look for the lines beginning with:
  ```
    WEBHOOK_INTEGRATIONS = [
  ```
  At the end of this section, add
  ```
    WebhookIntegration('<yourname>', display_name='<yourname>'),
  ```

#### Test the webhook.

You now have the webhook code written, and you have fixture data
for it in the JSON file you created above.

* Send the fixture message you wrote above! Replace the placeholder
  `<api_key>` in the code below with your real API key and `<yourname>`
  with your name:

```
(zulip-venv)vagrant@vagrant-ubuntu-trusty-64:/srv/zulip$./manage.py send_webhook_fixture_message \
--fixture=zerver/fixtures/<yourname>/<yourname>_hello.json \
--url='http://localhost:9991/api/v1/external/<yourname>?api_key=<api_key>'
```

  Notice that you mustn't include the backslashes `\` if you're typing the
  command manually. Those are to indicate that the line break shown is
  only for more clarity.

#### Take screenshots.

* Take a **screenshot** of the log line you get on the terminal after you
  finish your task. It should look something like:

```
    2016-11-18 15:58:04,600 INFO     127.0.0.1       POST    200 643ms (mem: 34ms/16) (md: 155ms/1) (db: 166ms/15q) (+start: 18ms) /api/v1/external/<yourname> (<bot_name>-bot@zulip.com via Zulip<YourName>Webhook)
```

* On your local server, you will see a new message in the `test`
  stream. Take a **screenshot** of the message.

* Post your notes of where you got stuck or found confusing terminology to the
  "GCI tasks" stream, under the topic "Incoming Webhooks".

### Double check your work and submit.

* Your first screenshot should have "/api/v1/external" and "POST"
  in one of the "INFO" lines.

* Your second screenshot should include a "Harry Potter" link, and
  it should be clear that "Test van Botten" sent it.

* Submit the two screenshots using the GCI tasks interface.


### Task Type B: Research how the integration should work.

Let *integration* be the integration listed in the task that brought
you here.  Follow the tutorial below to test how *integration* works
with Slack, a popular proprietary chat product with many integrations.
In the process will also be generating "webhook fixtures" for
*integration*, i.e. test data sent by the tool being integrated that
we can use to verify whether out integration works.

* Create a test team with [Slack](https://slack.com/). Find *integration* at
  https://slack.com/apps, and add it your Slack team. You will likely have
  to create an account at *integration*'s site as well.

* Figure out how to add a webhook URL to your account on the integration's
  site. Each site will be different, but you can often find how to do this
  by Googling for "*integration* add a webhook". Put in a test URL generated by
  [RequestBin](http://requestb.in/) (click "Create a RequestBin") or a
  similar site, in addition to the Slack webhook URL.

* Play around with the integration to figure out all the different types of
  messages you can generate in Slack, and take screenshots showing them
  (it's fine if multiple of these are in the same screenshot). Make a brief
  note in a file called `notes.md` (.md is the extension used by markdown
  format. It can be edited in any text editor e.g. notepad) about any messages
  you think are possible, but which you are unable to generate (e.g. because
  they are only available to paying customers). Add the screenshots and notes
  in a new folder `webhook-integrations/<integration>` in the zulip/zulip-gci
  respository, where `<integration>` is replaced by *integration* in lowercase.

* Add a commit with the screenshots and notes, and submit a pull request to the
  zulip/zulip-gci repository. Both the commit message and the title of the pull
  request should be `integrations: Add screenshots and notes for *integration*.`

* All these messages should also have been posted to your RequestBin
  URL. Put the webhook payloads generated for your integration in files in
  the zulip/zulip repository (not the zulip/zulip-gci repository) of the
  form `zerver/fixtures/<integration>/<integration>_<message-type>.json`,
  where `<integration>` is replaced by *integration* in lowercase. You can
  look at the other folders under `zerver/fixtures` to get a sense of what
  these should look like and how to name the files. Include exactly one
  payload for each type of message.  When we write the integration in task
  type C, we'll use these "test fixtures" to test our code.

* Add a commit with the webhook payloads, and submit a pull request to the
  zulip/zulip repository. Both the commit message and the title of the pull
  request should be `integrations: Add webhook payloads for *integration*.`

* Include links to both pull requests when you submit your task on
  the GCI website.

Congratulations!  You've done a lot of the hard work involved in
creating an integration.

### Task Type C: Write handlers and tests for an integration.

Let *integration* be the integration listed in the task that brought you
here.

* Make sure you have access to the output of Task Type B for *integration*.

* Skim through
  http://zulip.readthedocs.io/en/latest/integration-guide.html so you
  know roughly what's involved in writing a webhook integration.

* Follow the instructions in Steps 1-3 at
  http://zulip.readthedocs.io/en/latest/integration-guide.html#hello-world-webhook-walkthrough.
  for *integration*. You'll need code paths and tests for each of the
  fixtures; see the Semaphore integration for an example of an integration
  with multiple fixtures.

* Make sure all the tests pass, using `tools/test-all`.

* Add a commit with the changes above, and submit a pull request to the
  zulip/zulip repository. Both the commit message and the title of the pull
  request should be `integrations: Add webhook code, API endpoint, and tests
  for *integration*.` Make sure to add all the files using `git add`, or
  they won't be included in your commit.

* Include a link to the pull request when you submit your task on the GCI
  website.

### Task Type D: Add documentation for an integration.

Let *integration* be the integration listed in the task that brought you
here. All paths in this task refer to the zulip/zulip repository.

* Make sure you have access to the output of Task Type C for *integration*.
  For instance, check that there is something in the file
  `zerver/views/webhooks/*integration*.py`.

* If you didn't do Task Type B for this integration, create an account at
  *integration*'s site.

* Follow the instructions at
  http://zulip.readthedocs.io/en/latest/integration-guide.html#documenting-your-integration
  for *integration*.

* Add a roughly 250x250 pixel logo image for your integration under the
  `static/images/integrations/logos/<integration>.png`, where
  `<integration>` is the name of the integration in lower case.

* Generate a message sent by the integration by giving your test bot a nice
  name like "`<Integration>` Bot", use the project’s logo as the bot’s
  avatar, and take the screenshots showing the stream/topic bar for the
  message, not just the message body, doing something like:

  ```
  ./manage.py send_webhook_fixture_message --
  fixture=zerver/fixtures/<integration>/<integration>_<message_type>.json url=/api/v1/external/<integration>?stream=<stream_name>&api_key=<api_key>'
  ```

  Take a screenshot and save it as
  `/static/images/integrations/<integration>/<number>.png` where `number`
  is something like `001`. See the other folders in `/static/images/integrations/`
  for examples.

* In `templates/zerver/integrations.html`, add an `integration-instructions` class block in
  the alphabetically correct place, explaining all the steps required to
  setup the integration, including screenshots. Search the file for `semaphore` for an example.

* Make sure all the tests pass, using `tools/test-all`.

* Add a commit with the changes above, and submit a pull request to the
  zulip/zulip repository. Both the commit message and the title of the pull
  request should be `integrations: Add documentation for *integration*.`

* Include a link to the pull request when you submit your task on the GCI
  website.

## General notes

If there is an integration Zulip doesn't have that you would like to add,
please let us know on the "webhook integrations" topic on the "GCI task
discussion" stream!
