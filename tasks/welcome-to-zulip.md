# GCI Tasks: Welcome to Zulip

To contribute to Zulip you will need a working development environment, and
be able to modify and test Zulip code. If you are new to Zulip, this is the
task for you!

## Create an Account on our Chat Server

Almost all GCI discussion (and discussion of Zulip more generally) happens
on our developers' server, https://chat.zulip.org. Create an account and say
hi on the "introductions" topic of the "GCI general" stream!

Important streams:
* GCI announce: Messages from the Zulip GCI mentors.
* GCI task discussion: Task-specific discussion or help.
* GCI help: Any questions (about code or otherwise) not related to a specific task.
* GCI general: General discussion, feedback, questions, and so on.
* GCI chatter: Use it for anything you want :).

A few notes:
* If you see a question you can answer (on any of the streams), please do!
* Please adhere to our
  [community code of conduct](https://zulip.readthedocs.io/en/latest/code-of-conduct.html).

A few non-obvious things that help keep the server manageable:
* All test messages should go to the `test here` stream.
* Please always use a topic!

If you have questions at any point during this task, send us a message on
the "welcome to zulip" topic in the "GCI task discussion" stream!

## Set Up Your Development Environment

#### OSX and Linux

We recommend running the Zulip environment locally, in a Vagrant development
environment. See the
[Vagrant environment setup tutorial](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html).

Important: In "Step 2: Get Zulip Code", visit
`https://github.com/zulip/gci-submissions` instead of
`https://github.com/zulip/zulip`, and clone using
`git clone git@github.com:YOURUSERNAME/gci-submissions.git`.

There is also documentation for using Docker or installing directly on
Ubuntu. We don't recommend either of those methods unless you have a
specific reason to prefer them.

#### Windows

We recommend running development [remotely](#remote).

You can use
[Vagrant](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html), but
we have found getting the setup on Windows to be tricky.

#### Remote

Zulip has partnered with Digital Ocean to provide VMs for GCI participants
to develop Zulip. We recommend using a VM if you are using Windows, have
limited connection to the internet, or are only planning on submitting 1 or
2 tasks.

To get a VM, send us a message on the "vm request" topic in the "GCI task
discussion" stream.  TODO fill in Digital Ocean specific setup details.

Once you have your VM running, TODO: need next steps, e.g. how to set up an
ssh key and ssh in from windows, how to start the server, are we setting up
port forwarding, which editor to use on windows / how to set up Unison.

Maybe useful:
https://zulip.readthedocs.io/en/latest/dev-remote.html#editing-code-on-the-remote-machine


## Practice Running Zulip

Run your zulip server using
```
tools/run-dev.py
```
Go to http://localhost:9991, and verify that you can log in by clicking on
one of the accounts.  Take a screenshot, and add it to a new directory
`gci/welcome-to-zulip/<username>/`, where <username> is your name.


## Make a Change.

Find the `check_send_message` function by going to the `zulip/` directory
and entering `git grep 'def check_send_message'`.

Modify `check_send_message` so that anytime a user sends a message which says
"Nanananana" the message becomes "Nanananana Batman!"

Test that your change works in the browser.


## Add Some Tests

Add some tests to the bottom of `zerver/tests/test_messages.py` to make sure
we do not accidentally break this behavior in the future.

```
class BatmanTest(ZulipTestCase):
    def test_add_batman_to_nanana_message(self):
        # type: () -> None
        sender = get_user_profile_by_email('othello@zulip.com')
        client = make_client(name="test suite")
        message_id = check_send_message(sender, client, "stream", ["Verona"], "Batman test", "Nanananana")
        self.assertEqual(Message.objects.values_list("content", flat=True).get(id=message_id),
                         "Nanananana Batman!")

    def test_do_not_add_batman_to_normal_message(self):
        # type: () -> None
        sender = get_user_profile_by_email('othello@zulip.com')
        client = make_client(name="test suite")
        message_id = check_send_message(sender, client, "stream", ["Verona"], "Batman test", "Hi there")
        self.assertEqual(Message.objects.values_list("content", flat=True).get(id=message_id),
                         "Hi there")
```

Then run
```
tools/test-backend zerver/tests/test_messages.BatmanTest
```
to make sure your code passes the tests you just added. If it doesn't,
fix any brokenness in your code until it does. Take a screenshot of
your terminal, and add it to `gci/welcome-to-zulip/<username>/`.

Run
```
./tools/test-all
```
to verify that your code still passes the entire test suite.

`tools/test-all` is a suite of several tests, and can take a while to run. For
interactive debugging, one often wants to just run a single test in the suite. Run
```
cat tools/test-all
```
and figure out how to run just the lint tests and do so (there should be no
output). Add an extra space to the beginning of any line of code and run the
lint tests again. You should see a bunch of output in red. Take a screenshot of
your terminal, and add it to `gci/welcome-to-zulip/<username>/`.


## Contributing to Zulip

Please skim or read the following. These will be helpful for contributing
to Zulip and will be good to refer back to in the future:
* [Git Guide](https://zulip.readthedocs.io/en/latest/git-guide.html)
* [Version Control Style](https://zulip.readthedocs.io/en/latest/version-control.html)
* [Coding Style](https://zulip.readthedocs.io/en/latest/code-style.html)
* [Testing](https://zulip.readthedocs.io/en/latest/testing.html)

## Submit

Create a commit with the code changes and three screenshots, with commit
message `welcome task: Add tutorial changes for <username>.`

Create a pull request in the `zulip/gci-submissions` repository, with title
`welcome to zulip: <username>`.
