#GCI Tasks: interactive bots

Zulip [contrib-bots](https://github.com/zulip/zulip/tree/master/contrib_bots/lib) is a boilerplate for creating interactive bots that react to messages sent by users.

The interactive bots live in the `contrib-bots/lib` as `.py` files that define their specific behavior. The `contrib-bots/run.py` file defines common behaviors for the interactive bots that react to messages.

The following tasks will introduce you to using interactive bots and creating simple new bots that react to messages. This group of tasks has a high creative potential, as you can create your own bots that react to specific messages and can be integrated with various APIs.

## Task 0 - Test run the followup bot

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

2. Create a ~/`.zuliprc-local` file with credentials:

  ```
  [api]
  key=<api-key>
  email=iago@zulip.com
  site=http://localhost:9991/
  ```
  replace the placeholder "<api-key>" in the example with your own api-key which can be attained
  from settings and also configure its email properly.
  This is how Zulip knows the request is from an authorized user.

4. Run the server using vagrant - `/srv/zulip/tools/run-dev.py`.


5. Create a `followup` stream.


6. Run the followup bot:

  ```
  cd ~/zulip/contrib_bots
  python run.py lib/followup.py --config-file ~/.zuliprc-local
  ```

7. Test manually that the followup bot is working on the local Zulip instance, by:

  a. sending a few messages starting with `@followup` and `@follow-up` from different streams

  b. checking that the messages showed up in the `followup` stream, prepended by the sender email

## Task 1 - Create a links bot

Follow the tutorial below to create your first simple bot that sends private messages to users.

1. Duplicate the `followup.py` file under `links.py`, to build on existing code.


2. Change the class name to `LinksHandler` and the last line to `handler_class = LinksHandler`.


3. Edit the comments appropriately:

  a. `class LinksHandler(object)`
  > This plugin facilitates creating a list of resources you want to save while using Zulip. It looks for messages starting with "@link" or "@resource".
  > In this example, we send resources to private messages.


  b.  `def usage(self)`
  > This plugin will allow users to flag messages as being resources and store them in private messages with the bot. Users should preface messages with "@link" or "@resource".


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

6. Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of the message

  - it currently posts the message to the followup stream, as the followup bot would


7. Edit the `handle_message`:

  ```
  client.send_message(dict(
      type='private',
      to=original_sender,
      content=new_content,
  ))
  ```

8. Check that the bot is working as expected:

  - it reacts to the `@link` and `@resource` at the beginning of a message

  - it currently sends a private message from the admint account to the author of the original message

[TODO] figure out why some bot credentials don't work locally

## Task 2 - Create your own bots

Some ideas on what the bots could do:

  - post to an issue tracker like GitHub

  - post events to a calendar like Google Calendar

  - send group messages to user groups

  - initiate a timer and post a message after a specific time interval

  - post answers on specific topics - similar to `man` in terminal

For inspiration you can look through the [current issues](https://github.com/zulip/zulip/issues) or ask other users what they might find useful.

[TODO] post additional ideas that are relevant to current issues
