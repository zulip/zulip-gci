#GCI Tasks: interactive bots

## Prerequisites

* A working Zulip development environment. See https://github.com/zulip/zulip-gci/blob/master/README.md for instructions on how to set one up.

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

1. Virtual environment setup:

  a. move to the local Zulip repository

  b. check out master branch in the local repository

  c. pull the upstream master branch (upstream is the Zulip GitHub repository)

  d. run the virtual machine using vagrant (up and provision)

  e. ssh into the virtual machine

  f. run migrations

  ```
  cd ~/Zulip/
  git checkout master
  git pull upstream master
  vagrant up
  vagrant provision
  vagrant ssh
  cd zulip
  python manage.py migrate
  ```

2. Create a `~/.zuliprc-local` file with credentials:

  ```
  [api]
  key=<api-key>
  email=<email>
  site=http://localhost:9991/
  ```

  Replace the placeholder `<api-key>` in the example with an existing user API
  key and placeholder `<email>` with appropriate email. You can get API keys
  just below the bots section in the settings page. This is how Zulip knows the
  request is from an authorized user.

  You can also create a new bot for a user in settings - it will have its own
  api key and email. Remember to subscribe it to the streams you want to use the
   bot in.

4. Run the server using vagrant - `/srv/zulip/tools/run-dev.py`.


5. Create a `followup` stream.


6. Run the followup bot:

  ```
  cd ~/zulip/contrib_bots
  python run.py lib/followup.py --config-file ~/.zuliprc-local
  ```

7. Test manually that the followup bot is working on the local Zulip instance,
by:

  a. sending a few messages starting with `@followup` and `@follow-up` from
  different streams

  b. checking that the messages showed up in the `followup` stream, prepended by
   the sender email

8. Take screenshots showing that the bot is working, i.a. your terminal window
with the bot working, messages sent by the bot in the followup stream. Add the
screenshots to `interactive-bots/followup/<username>/`.

9. Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/followup/<username>/`.

10. Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the followup bot for <username>.`.

11. Create a pull request in the `zulip/zulip-gci` repository, with title
`interactive bots: Run the followup bot for <username>`.

*Completion criteria:* Mentors will check that the followup bot was properly
set up.

### Task Type B: Create a links bot

Follow the tutorial below to create your first simple bot that sends private
messages to users.

1. Duplicate the `followup.py` file under `links.py`, to build on existing code.


2. Change the class name to `LinksHandler` and the last line to `handler_class
= LinksHandler`.


3. Edit the comments appropriately:

  a. `class LinksHandler(object)`
  > This plugin facilitates creating a list of resources you want to save while
  using Zulip. It looks for messages starting with "@link" or "@resource".
  > In this example, we send resources to private messages.


  b.  `def usage(self)`
  > This plugin will allow users to flag messages as being resources and store
  them in private messages with the bot. Users should preface messages with
  "@link" or "@resource".


4. Edit the `triage_message`:

  ```
  if message['display_recipient'] == 'links':
      return False
  is_link = (original_content.startswith('@link') or
             original_content.startswith('@resource'))

  return is_link
  ```

  The bot now responds to `@link` and `@resource`.


5. Edit the `handle_message`:

  ```
  if original_content.startswith('@link'):
      new_content = original_content.replace('@link',
                                         'from %s:' % (original_sender,))
  else:
      new_content = original_content.replace('@resource',
                                         'from %s:' % (original_sender,))
  ```

6. Create a links bot in settings for an existing user. Use its credentials in
`~/.zuliprc-local`. Remember to subscribe the bot to the streams you want to use
 it in.

7. Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of a message

  - it currently posts the message to the followup stream, as the followup bot
  would

8. Edit the `handle_message`:

  ```
  client.send_message(dict(
      type='private',
      to=original_sender,
      content=new_content,
  ))
  ```

10. Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of a message

  - it sends a private message to the author of the original message

11. Take screenshots showing that the bot is working, i.a. your terminal window
with the bot working, messages sent by the bot to the users. Add the screenshots
 to `interactive-bots/links/<username>/`.

12. Note down any places you got stuck, problems or errors you ran into while
doing this setup process. Add your notes as a `notes.md` file to
`interactive-bots/links/<username>/`.

13. Create a commit with the screenshots and notes, with commit message
`interactive bots: Run the links bot for <username>.`.

14. Create a pull request in the `zulip/zulip-gci` repository, with title
`interactive bots: Run the links bot for <username>`.

*Completion criteria:* Mentors will check that the links bot was properly set up.

### Task Type C: Create an interactive bot

Let *feature* be the feature mentioned in the task that brought you here.

1. Make sure you understand what is expected of the *feature* - what messages
should the bot react to, what should it do with the message content and where
should it post any output.

2. Create the interactive bot at `~/zulip/contrib_bots/lib` as a `.py` file.
Make sure it fulfills the requirements.

3. Make sure all the tests pass, using `tools/test-all`.

4. Create a commit with your bot, with commit message `interactive bots: Create
*feature* bot.`.

5. Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create *feature* bot.`.

*Completion criteria:* Mentors will check if the new bot fulfills the feature
requirements.

### Task Type D: Create your own bot

1. Come up with an idea for your own interactive bot that would improve Zulip.
Make sure to make clear what would be expected of the bot -  what messages
should it react to, what should it do with the message content and where should
it post any output.

2. Present your idea for an interactive bot on the `interactive bots` topic on
the `GCI tasks` stream. Consult with mentors and make sure your idea was approved
 before you start coding.

3. Create your interactive bot at `~/zulip/contrib_bots/lib` as a `.py` file.
Make sure it fulfills the requirements.

4. Make sure all the tests pass, using `tools/test-all`.

5. Create a commit with your bot, with commit message `interactive bots: Create
<bot_name> bot.`.

6. Create a pull request in the `zulip/zulip` repository, with title
`interactive bots: Create <bot_name> bot by <username>.`.

*Completion criteria:* Mentors will check if the new bot fulfills the feature
requirements.
