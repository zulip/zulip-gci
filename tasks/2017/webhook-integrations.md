# GCI Tasks: Incoming Webhook Integrations

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md#setting-up-the-zulip-development-environment)
  for instructions on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) and
  [intro to Zulip server development](https://codein.withgoogle.com/tasks/4799263762546688/) tasks.

## Background

A [Zulip integration](https://zulipchat.com/integrations/) is a special type
of bot that brings information from the outside world into Zulip. Zulip
integrations allow teams to stay up-to-date on code changes, issue tickets,
build system results, tweets, and more. Zulip currently has over 60
integrations, but there are dozens more that are valuable to add.

As an example, see [this commit](https://github.com/zulip/zulip/pull/1759)
for the code that added the Sentry integration.

Task Types C and D generally require the previous task for that
particular integration to be completed first.

## Task Descriptions

### Task Type A: Create a personalized integration.

Follow the tutorial below to create a duplicate of our
[HelloWorld integration](https://zulipchat.com/integrations/doc/helloworld)
that is named after yourself, and sends a unique message you'd like to share
with the world. As you're going through the tutorial, take notes on where
you got stuck or needed to look up terminology.

Notation: Everywhere below, `<yourname>` should be replaced by your name in
lowercase (no spaces or underscores), and `<YourName>` should be replaced by
your name in CamelCase.

* Read through the [Integrations guide](https://zulipchat.com/api/integration-guide)
  to get an understanding of what integrations are and how Zulip uses them. We will
  be creating a "Webhook integration".

* [Start your Zulip development server](./intro-to-zulip-server.md#practice-running-zulip).
You will test your integration on this server.

* Create a bot under the `Your Bots` section of your Zulip user’s `Settings` page.
  Use `<yourname>_helloworld_integration` for the bot's full name, and
  `helloworld-integration` for its username. Set its type to "Incoming webhook".
  Keep the bot's API key around. Your new bot will be used by the integration service to
  communicate with your Zulip server.

* Create a new directory `zerver/webhooks/<yourname>`. This is the main directory for your
  integration. You will store the integration's code and test fixtures here.

* Create a test fixture. A test fixture is a file with sample data in it. In our case, the
  sample data is the payload from HTTP requests the integrated service send to our Zulip
  server. Usually, we have to capture this payload with special tools. Right now though, we
  will pretend a very simply  We will use the test fixture to test our webhook later.
  * Add a json file `zerver/webhooks/<yourname>/fixtures/hello.json`
    that contains this fixture:
    ```
    {
      "featured_title":"Harry Potter",
      "featured_url":"https://en.wikipedia.org/wiki/Harry_Potter",
    }
    ```
    (In the "real world", this fixture could have been sent for example by a service that posts an interesting
    Wikipedia article every week.)

* Add the integration code.
  * Add a new file `zerver/views/webhooks/<yourname>.py`
  * Copy the contents of the `helloworld.py` to this file. Replace all instances of `HelloWorld`
  and `helloworld` with `<YourName>` and `<yourname>`, respectively. Also choose a new topic below
  (replace `<your_topic>`).
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
      WebhookIntegration('<yourname>', categories=['misc'], display_name='<yourname>'),
    ```

You now have the webhook code written, and you have fixture data to test it.

* Test your webhook.
  * Send the fixture message you wrote above! In your vagrant development environment,
    run the command below. Replace `<api_key>` with the bot's API key and `<yourname>`
    with your name:
    ```
    ./manage.py send_webhook_fixture_message \
    --fixture=zerver/webhooks/<yourname>/fixtures/hello.json \
    --url='http://localhost:9991/api/v1/external/<yourname>?api_key=<api_key>&stream=Verona'
    ```
  Note that you mustn't include the backslashes `\` displayed in the command above.
  Their purpose is to indicate that a line is continued in the next next line, meaning
  that a line-break should be ignored.

* Take a **screenshot** of the log line you get on the terminal after you
  finish your task. It should look something like:
  ```
      2016-11-18 15:58:04,600 INFO     127.0.0.1       POST    200 643ms (mem: 34ms/16) (md: 155ms/1) (db: 166ms/15q) (+start: 18ms) /api/v1/external/<yourname> (<bot_name>-bot@zulip.com via Zulip<YourName>Webhook)
  ```

* On your local server, you will see a new message in the `Verona`
  stream. Take a **screenshot** of the message.

* Post your notes of where you got stuck or found confusing terminology in the
  "GCI tasks" stream, on the topic "Incoming Webhooks".

* Submit the two screenshots using the GCI tasks interface.
  * Your first screenshot should have "/api/v1/external" and "POST"
    in one of the "INFO" lines.

  * Your second screenshot should include a "Harry Potter" link, and
    it should be clear that "<yourname>_helloworld_integration" sent it.

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
  by googling for "*integration* add a webhook". Put in a test URL generated by
  [RequestBin](https://requestb.in/) (click "Create a RequestBin") or a
  similar site, in addition to the Slack webhook URL.

* Play around with the integration to figure out all the different types of
  messages you can generate in Slack, and take screenshots showing them
  (it's fine if multiple of these are in the same screenshot). Make a brief
  note in a file called `notes.md` about any messages you think are possible,
  but which you are unable to generate (e.g. because they are only available
  to paying customers). Add the screenshots and notes in a new folder
  `webhook-integrations/<integration>` in the [zulip/zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) respository, where
  `<integration>` is replaced by *integration* in lowercase.

* Add a commit with the screenshots and notes, and submit a pull request to the
  [zulip/zulip-gci-submissions](https://github.com/zulip/zulip-gci-submissions)
  repository. Both the commit message and the title of the pull request should
  be `integrations: Add screenshots and notes for *integration*.`

* All these messages should also have been posted to your RequestBin
  URL. Put the webhook payloads generated for your integration in files in
  the [zulip/zulip](https://github.com/zulip/zulip) repository as
  `zerver/webhooks/<integration>/fixtures/<message_type>.json`,
  where `<integration>` is replaced by *integration* in lowercase. You can
  look at fixture folders of other integrations in `zerver/webhooks` to
  get a sense of what these should look like and how to name the files. Include
  exactly one payload for each type of message.  When we write the integration
  in task type C, we'll use these "test fixtures" to test our code.

* Add a commit with the webhook payloads, and submit a pull request to the
  [zulip/zulip](https://github.com/zulip/zulip) repository. Both the commit
  message and the title of the pull request should be `integrations: Add
  webhook payloads for *integration*.`

* Include links to both pull requests when you submit your task on
  the GCI website.

Congratulations!  You've done a lot of the hard work involved in
creating an integration.

### Task Type C: Write handlers and tests for an integration.

Let *integration* be the integration listed in the task that brought you
here.

* Make sure you have access to the output of Task Type B for *integration*.

* Skim through the [integration guide](https://zulipchat.com/api/integration-guide)
  so you know roughly what's involved in writing a webhook integration.

* Follow Steps 1-4 in the [webhook walkthrough](
  https://zulipchat.com/api/webhook-walkthrough) for *integration*. You'll
  need code paths and tests for each of the fixtures; see the Semaphore
  integration for an example of an integration with multiple fixtures.

* Make sure all the tests pass, using
  ```
  tools/test-all
  ```
  If there are errors with your webhook tests, you don't have to run all tests
  again. Instead, you can run only your webhook tests with
  ```
  tools/test-backend zerver.webhooks.<integration>
  ```

* Add a commit with the changes above, and submit a pull request to the
  [zulip/zulip](https://github.com/zulip/zulip) repository. Both the commit
  message and the title of the pull request should be `integrations: Add webhook
  code, API endpoint, and tests for *integration*.` Make sure to add all the files
  using `git add`, or they won't be included in your commit.

* Include a link to the pull request when you submit your task on the GCI
  website.

### Task Type D: Add documentation for an integration.

Let *integration* be the integration listed in the task that brought you
here. All paths in this task refer to the [zulip/zulip](
https://github.com/zulip/zulip) repository.

* Make sure you have access to the output of Task Type C for *integration*.
  For instance, check that there is something in the file
  `zerver/webhooks/<integration>/view.py`.

* If you didn't do Task Type B for this integration, create an account at
  *integration*'s site.

* Follow the instructions in the [Documenting an integration guide](
  https://zulipchat.com/api/integration-docs-guide) for *integration*.

* Make sure all the tests pass, using `tools/test-all`.

* Add a commit with the changes above, and submit a pull request to the
  [zulip/zulip](https://github.com/zulip/zulip) repository. Both the commit
  message and the title of the pull request should be
  `integrations: Add documentation for *integration*.`

* Include a link to the pull request when you submit your task on the GCI
  website.

## General notes

If there is an integration Zulip doesn't have that you would like to add,
please let us know on the "webhook integrations" topic in the [GCI tasks](
https://chat.zulip.org/#narrow/stream/GCI.20tasks) stream!
