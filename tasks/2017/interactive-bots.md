# GCI Tasks: Interactive bots

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for
  instructions on how to set one up.

* Basic knowledge of git. We **strongly suggest** you finish the
  [Get Comfortable With Git](https://codein.withgoogle.com/dashboard/tasks/5415336817983488/)
  task first before attempting this.

* You need to know how to create a GitHub pull request. Check out the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/dashboard/tasks/4884433561714688/)
  task if you aren't sure how to do this, or read through the task
  description [here](https://github.com/zulip/zulip-gci/tree/master/submit-a-pull-request).

* Update your working copy of Zulip. [Learn how](../../before-every-task.md).

* **Update your working copy of the `python-zulip-api` repository and then create a feature branch.**

* **A working Zulip bots development environment. See [here](
  https://zulipchat.com/api/writing-bots#installing-a-development-version-of-the-zulip-bots-package)
  for instructions on how to set one up.**
  * If you are using a droplet, make sure that you **do not**
    set up the bots development environment inside the droplet.
    Instead, clone the `python-zulip-api` repository to your
    local computer and set up the development environment there.

* Python 3.

## Background

Zulip supports interactive bots. Bots are little programs that have limited
access to a Zulip server. They can receive messages @-mentioning them and
respond with useful information, jokes, etc.

Zulip's bot infrastructure lives in the [`zulip_bots`](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots)
Python package. The bots themselves can be found in [zulip_bots/zulip_bots/bots](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots).
Each bot resides in its own directory that contains the bot's code, tests, and
documentation.

The following tasks will introduce you to using interactive bots and creating
simple new bots that react to messages. This group of tasks has a high
creative potential, as you can create your own bots that react to specific
messages and can be integrated with various APIs.

## Task Descriptions

There are four types of tasks in this category, each corresponding to one of
the Task Types below.

### Task Type A: Learn about interactive bots by running the helloworld bot

Follow the tutorial below to test run the helloworld bot on your Zulip
instance (either local or in your droplet).  As you're going through the tutorial,
take notes on where you got stuck or needed to look up terminology.

Follow the steps below to run the helloworld bot:

* Go through the steps outlined in the [Running a bot guide](
https://zulipchat.com/api/running-bots#running-a-bot).

  - [Use your own Zulip development server](
  https://github.com/zulip/zulip-gci/blob/master/tasks/2017/intro-to-zulip-server.md#practice-running-zulip)
  for testing.
  - In step 2, use `<your-name>_helloworld_bot` for the bot's full name,
  and `helloworld` for its username.
  - In step 4, substitute `<bot-name>` with `helloworld`.

* Test manually that the helloworld bot is working on the local Zulip instance,
by:

 - sending a few messages starting with `@**<your-name>_helloworld_bot**` in
 the stream "Verona".

 - checking that the bot is replying with `beep boop` each time.

* Take screenshots showing that the bot is working, make sure to have
screenshots of:

  - your terminal window with the bot running, including the command you used
  to run the bot and the output with the bot description
  - messages sent by you to the bot in the stream "Verona"
  - messages sent by the bot in the same stream
  - any other screenshots you find relevant

  Add the screenshots to `interactive-bots/helloworld/<username>/` in the [zulip/zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) repository. Make sure
  your filenames do not have white-spaces, since those often cause trouble
  with file systems. Instead, use dashes (`-`).

* Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/helloworld/<username>/` in the [zulip/zulip-gci-submissions](
https://github.com/zulip/zulip-gci-submissions) repository.

* Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the helloworld bot for <username>.`.

* Create a pull request in the [zulip/zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) repository, with
  title `interactive bots: Run the helloworld bot for
  <username>`. Link to your GCI task in comment section.

*Completion criteria:* Mentors will check that the helloworld bot was properly
set up.

### Task Type B: Learn about interactive bots by creating a message info bot

We recommend completing **Task Type A** before doing this task.

Follow the tutorial below to create your first simple bot. It will analyze a
message that @-mentions the bot and count its words for word count. The gathered
information will then be sent to a private conversation with the message author.

* Read through the [Running bots](https://zulipchat.com/api/running-bots#running-a-bot)
and [Writing bots](https://www.zulipchat.com/api/writing-bots) guides.

* Make a copy of the helloworld bot
[python-zulip-api/zulip_bots/zulip_bots/bots/helloworld](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots/helloworld)
and name it `message_info`, to build on existing code.
  ```shell
  cp -r helloworld message_info
  ```

* Rename `helloworld.py` to `message_info.py`. In `message_info.py`,
change the class name to `MessageInfoHandler` and the last line to
`handler_class = MessageInfoHandler`.

* Edit the return statement in `def usage(self)`:

  > This bot will allow users to analyze a message for word count.
  The gathered information will then be sent to a private
  conversation with the user. Users should @-mention the bot in the
  beginning of a message.

* Insert the following into the code of `handle_message()`, leaving the 
existing `bot_handler.send_reply(message, content)` line in place:
  ```python
  words_in_message = message['content'].split()
  content = "You sent a message with {} words.".format(len(words_in_message))
  ```

* Create a new bot in your development server's settings. Use "Message info bot"
as the bot's full name, and "message-info" as its username. Run your bot 
like in **Task Type A**. For `<bot-name>` in the `zulip-run-bot` command, use
`message_info`.

* Check that the bot is working as expected:

  - it replies to messages that @-mention the bot with the word count of that message
  - it currently replies to a message in the same stream, as the helloworld
  bot did

* Navigate back to the python file. In `handle_message()`, replace the `send_reply()` call
  with this code:
  ```python
  original_sender = message['sender_email']
  bot_handler.send_message(dict(
      type='private',
      to=original_sender,
      content=content,
  ))
  ```

* Check that the bot is working as expected:

  - it responds to messages that @-mention the bot with the word count of that message
  - it responds with a private message to the sender of the original message

* Rename `test_helloworld.py` to `test_message_info.py`. Edit the file and write tests
  for the `message_info` bot.
  * Update the line assigning the `bot_name` variable.
  * Rewrite the existing unit test. It should simulate sending a message to a stream,
  and verify that the bot replies with a private message to the sender with a correct
  response. You can base your testing code on the [first followup bot unit test](
  https://github.com/zulip/python-zulip-api/blob/master/zulip_bots/zulip_bots/bots/followup/test_followup.py#L13).

* Test your new unit test for your bot. Run `tools/test-bots message_info` in your
  `python-zulip-api` repo.

* Take screenshots showing that the bot is working, make sure to have
screenshots of:

  - your terminal window with the bot running, including the command you used
  to run the bot and the output with the bot description
  - messages sent by you to the bot in the `Verona` stream
  - messages sent by the bot in the private messages to the author
  - your successful unit test
  - the code you wrote for your unit test
  - any other screenshots you find relevant

* Add the screenshots to `interactive-bots/message_info/<username>/`. Make sure your
filenames do not have white spaces, since those often cause trouble
with file systems. Instead, use dashes (`-`).

  - Note down any places you got stuck, problems or errors you ran into while
  doing this setup process. Add your notes as a `notes.md` file to
  `interactive-bots/message_info/<username>/`.

  - Create a commit with the screenshots and notes, with commit message
  `interactive bots: Run the message_info bot for <username>.`

  - Create a pull request in the [zulip/zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) repository, with title
  `interactive bots: Run the message_info bot for <username>`. Link to your GCI task
  in comment section.

*Completion criteria:* Mentors will check that the message info bot was properly
set up.

### Task Type C: Create an interactive bot

We recommend claiming this task type after completing **Task Type A**
and **Task Type B**.

Let *feature* be the feature mentioned in the task that brought you here.

* Read through the [Running bots](https://zulipchat.com/api/running-bots#running-a-bot)
and [Writing bots](https://www.zulipchat.com/api/writing-bots) guides.

* Make sure you understand what is expected of *feature* - what messages
should the bot react to, what should it do with the message content and
where should it post any output. Should you have any doubts, discuss them in
the Zulip `GCI tasks` stream.

* Create the interactive bot at
`python-zulip-api/zulip_bots/zulip_bots/bots/<feature>/`.

* Test your bot manually, check that:

  * Your bot is reacting to the appropriate messages.
  * Your bot responds with the expected output.

* Verify that your bot follows the [directory structure for Zulip bots](
https://www.zulipchat.com/api/writing-bots#adding-a-bot-to-zulip).
You can use the [GIPHY bot](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots/giphy)
as an orientation. In particular, check that:

  * Your bot comes with unit tests.
  * Your bot comes with a documentation.

* Create a commit with your bot, with commit message `interactive bots:
Create <feature> bot.`.

* Create a pull request in the [zulip/python-zulip-api](
https://github.com/zulip/python-zulip-api) repository, with title
`interactive bots: Create <feature> bot.`. Link to your GCI task in
the comment section on GitHub.

*Completion criteria:* Mentors will check if the new bot fulfills the
feature requirements and follows the proper directory structure.

### Task Type D: Improve an existing bot

We recommend claiming this task type after completing **Task Type A**
and **Task Type B**.

Let *bot* and \<bot\> be the bot mentioned in the task that brought you here.

* Locate *bot*. It can be either in [python-zulip-api/zulip_bots/zulip_bots/bots](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots/),
or in [python-zulip-api/zulip_bots/zulip_bots/bots_unmaintained](
https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots_unmaintained/).
If it is in `bots_unmaintained`, move it to `bots`.

* Try to run *bot*. Fix any bugs you notice.
  - Does *bot* start?
  - Does *bot* respond as expected?
  - Does *bot* crash on any input?

* Check the structure of *bot*. Fix any inconsistencies you notice.
  - Is the directory of *bot* properly structured?
  - Are the files in *bot*'s directory named correctly? Are they complete? If
  a bot requires a configuration file, the directory should contain a template `<bot>.conf`.
  - You can look up the proper directory structure and filenames in our
  [Writing bots guide](https://www.zulipchat.com/api/writing-bots#adding-a-bot-to-zulip).

* Read through the documentation of *bot*. Fix any inconsistencies you notice.
  - Does the documentation describe the purpose of *bot*?
  - Does the documentation give instructions for setting up and using *bot*?
  - Is the documentation properly structured? It should have a quick introductory
  paragraph under the main header, followed by sections "Setup" and "Usage".

* Add and run tests for *bot*. Fix any bugs you notice and aim for 100% test coverage.
  - If *bot* already has unit tests (these are in a file named `test_<bot>.py`):
    - In the development environment in your python-zulip-api repo, run
      ```
      tools/test-bots <bot> --coverage
      ```
      This will run the unit tests for *bot* and verify that it responds correctly to
      messages. Additionally, it will create a folder `htmlcov`.
    - Open `htmlcov/index.html` and click on `zulip_bots/zulip_bots/bots/<bot>/<bot>.py`.
    You will see the file, with some lines marked in green, and some in red. Green lines
    are covered by the test. This means that during the unit test, these lines got executed
    at some point. Lines marked in red have never been executed.
    - Add tests for all the remaining red lines.

  - If *bot* does not have unit tests:
    - Add unit tests for *bot* in a new file `test_<bot>.py`. Getting 100% test coverage
    is a nice-to-have, but not required when there are no existing tests.

  - `zulip_bots` has an extensive test helper library that simplifies testing bots with
  configuration files, internet queries, etc. Use tests for other bots as an orientation.
  In particular, check out the tests for the [GIPHY bot](
  https://github.com/zulip/python-zulip-api/tree/master/zulip_bots/zulip_bots/bots/giphy).
  [Testing with mocks](
  http://zulip.readthedocs.io/en/latest/testing/testing-with-django.html#testing-with-mocks)
  is a guide that will further prep your testing skills.

  - Think of corner cases when adding tests. Test messages you wouldn't expect a user to
  send, and try to break *bot* (just like manual testing).

* Create a commit with the updated bot, with commit message `interactive bots:
Improve *bot* bot.`.

* Create a pull request in the [zulip/python-zulip-api](
https://github.com/zulip/python-zulip-api) repository, with title
`interactive bots: Improve <bot> bot.`. Link to your GCI task in
the comment section on GitHub.

*Completion criteria:* Mentors will check that the improved bot works,
is structured properly, has a comprehensive documentation and passes all tests.

## General notes

* If there is an integration Zulip doesn't have that you would like to add,
please let us know on the `bot proposals` topic in the `GCI tasks` stream.
We can then discuss adding a **Task Type C** for creating that bot. Good
sources of inspiration are the integrations and bots present in [Hubot](
https://hubot.github.com/), [Errbot](http://errbot.io/en/latest/), [Slack](
https://slack.com/apps), and [Telegram](https://storebot.me/).

* If you want to test bots on [chat.zulip.org](chat.zulip.org), please use the
[#bot testing](https://chat.zulip.org/#narrow/stream/bot.20testing) stream.
