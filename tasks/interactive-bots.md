#GCI Tasks: interactive bots

## Prerequisites

* A working Zulip development environment. See
  https://github.com/zulip/zulip-gci/blob/master/README.md for instructions on
  how to set one up.

* You need to know how to create a GitHub pull request. Check out the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/tasks/6541581402243072/)
  task if you aren't sure how to do this, or read through the task description
  [here](https://github.com/zulip/zulip-gci/blob/master/tasks/submit-a-pull-request.md).

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

## Background

Zulip [contrib-bots](https://github.com/zulip/zulip/tree/master/contrib_bots/lib)
is a boilerplate for creating interactive bots that react to messages sent
by users.

The interactive bots live in the `contrib-bots/lib` as `.py` files that define
their specific behavior. The `contrib-bots/run.py` file defines common behaviors
for the interactive bots that react to messages.

The following tasks will introduce you to using interactive bots and creating
simple new bots that react to messages. This group of tasks has a high creative
potential, as you can create your own bots that react to specific messages and
can be integrated with various APIs.

## Task Descriptions

There are three types of task in this category, each corresponding to one of the
 Task Types below.

### Task Type A: Run the followup bot

Follow the tutorial below to test run the followup bot on your local instance.

* Create a `~/.zuliprc-local` file with credentials:

  ```
  [api]
  key=<api-key>
  email=<email>
  site=http://localhost:9991/
  ```

  Replace the placeholder `<api-key>` in the example with an existing user API
  key and placeholder `<email>` with the user email. You can get API keys
  just below the bots section in the settings page. This is how Zulip knows the
  request is from an authorized user.

  You can also create a new bot for a user in settings - it will have its own
  api key and email. Remember to subscribe it to the streams you want to use the
   bot in.

* Run the Zulip server.


* Create a `followup` stream.


* Run the followup bot:

  ```
  cd ~/zulip/contrib_bots
  python run.py lib/followup.py --config-file ~/.zuliprc-local
  ```

* Test manually that the followup bot is working on the local Zulip instance,
by:

  a. sending a few messages starting with `@followup` and `@follow-up` from
  different streams

  b. checking that the messages showed up in the `followup` stream, prepended by
  the sender email

* Take screenshots showing that the bot is working, i.a. your terminal window
with the bot working, messages sent by the bot in the followup stream. Add the
screenshots to `interactive-bots/followup/<username>/`.

* Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/followup/<username>/`.

* Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the followup bot for <username>.`.

* Create a pull request in the `zulip/zulip-gci` repository, with title
`interactive bots: Run the followup bot for <username>`.

*Completion criteria:* Mentors will check that the followup bot was properly
set up.

### Task Type B: Create a links bot

Follow the tutorial below to create your first simple bot that sends private
messages to users.

* Duplicate the `followup.py` file under `links.py`, to build on existing code.


* Change the class name to `LinksHandler` and the last line to `handler_class
= LinksHandler`.


* Edit the comments appropriately:

  a. `class LinksHandler(object)`
  > This plugin facilitates creating a list of resources you want to save while
  using Zulip. It looks for messages starting with "@link" or "@resource".
  > In this example, we send resources to private messages.


  b.  `def usage(self)`
  > This plugin will allow users to flag messages as being resources and store
  them in private messages with the bot. Users should preface messages with
  "@link" or "@resource".


* Edit the `triage_message`:

  ```
  if message['display_recipient'] == 'links':
      return False
  is_link = (original_content.startswith('@link') or
             original_content.startswith('@resource'))

  return is_link
  ```

  The bot now responds to `@link` and `@resource`.


* Edit the `handle_message`:

  ```
  if original_content.startswith('@link'):
      new_content = original_content.replace('@link',
                                         'from %s:' % (original_sender,))
  else:
      new_content = original_content.replace('@resource',
                                         'from %s:' % (original_sender,))
  ```

* Create a links bot in settings for an existing user. Use its credentials in
`~/.zuliprc-local`. Remember to subscribe the bot to the streams you want to use
 it in.

* Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of a message

  - it currently posts the message to the followup stream, as the followup bot
  would

* Edit the `handle_message`:

  ```
  client.send_message(dict(
      type='private',
      to=original_sender,
      content=new_content,
  ))
  ```

* Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of a message

  - it sends a private message to the author of the original message

* Take screenshots showing that the bot is working, i.a. your terminal window
with the bot working, messages sent by the bot to the users. Add the screenshots
 to `interactive-bots/links/<username>/`.

* Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/links/<username>/`.

* Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the links bot for <username>.`.

* Create a pull request in the `zulip/zulip-gci` repository, with title
`interactive bots: Run the links bot for <username>`.

*Completion criteria:* Mentors will check that the links bot was properly set up.

### Task Type C: Create an interactive bot

Let *feature* be the feature mentioned in the task that brought you here.

* Make sure you understand what is expected of the *feature* - what messages
should the bot react to, what should it do with the message content and where
should it post any output. Should you have any doubts, discuss them in the Zulip
`GCI tasks` stream.

* Create the interactive bot at `~/zulip/contrib_bots/lib/<feature>` as a
`<feature>.py` file. Make sure it fulfills the requirements.

* Test your bot manually, check that:

  * The bot is reacting to the appropriate messages.
  * The bot uses the content from the messages properly.
  * The bot posts the expected output.

* Create a commit with your bot, with commit message `interactive bots: Create
*feature* bot.`.

* Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create *feature* bot.`.

*Completion criteria:* Mentors will check if the new bot fulfills the feature
requirements.

### Task Type D: Create your own bot

* Come up with an idea for your own interactive bot that would improve Zulip.
Make sure to make clear what would be expected of the bot -  what messages
should it react to, what should it do with the message content and where should
it post any output.

* Present your idea for an interactive bot on the `interactive bots` topic on
the `GCI tasks` stream. Consult with mentors and make sure your idea was approved
 before you start coding.

* Create your interactive bot at `~/zulip/contrib_bots/lib/<bot_name>` as a
`<bot_name>.py` file. Make sure it fulfills the requirements.

* Test your bot manually, check that:

  * The bot is reacting to the appropriate messages.
  * The bot uses the content from the messages properly.
  * The bot posts the expected output.

* Document your interactive bot at `~/zulip/contrib_bots/lib/<bot_name>` in a
`docs.md`. Add any relevant screenshots that will help understand how the bot
works.

* Create a commit with your bot, with commit message `interactive bots: Create
<bot_name> bot.`.

* Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create <bot_name> bot by <username>.`.

*Completion criteria:* Mentors will check if the new bot fulfills the feature
requirements.
