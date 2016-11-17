# Beginner - GCI Tasks: Setting up Your Development Environment

To contribute to Zulip you will need a working development environment, and be
able to modify and test Zulip code. This task is designed to help you
familiarize yourself with doing this.

## Set Up Your Development Environment

#### OSX and Linux

We recommend running the Zulip environment locally, in a Vagrant development environment. See the using
[Vagrant](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html) tutorial.

There is also documentation for using
[Docker](https://zulip.readthedocs.io/en/latest/install-docker-dev.html), installing
[directly on Ubuntu](https://zulip.readthedocs.io/en/latest/install-ubuntu-without-vagrant-dev.html),
or using a [remote](#remote) machine.

#### Windows

We recommend running development [remotely](#remote).

You can use
[Vagrant](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html), but
we have found getting the setup on windows tricky.

#### Remote

Zulip has partnered with Digital Ocean to provide VMs for GCI participants to develop Zulip.

TODO fill in Digital Ocean specific setup details.

Once you have setup your VM running see the [remote development tutorial](https://zulip.readthedocs.io/en/latest/dev-remote.html)


## Practice Running Zulip

Run your zulip server using
```
tools/run-dev.py
```
Go to http://localhost:9991, and verify that you can log in by clicking on one of the accounts. Take a screenshot.


## Make a Change.

Find the check_send_message function by going to the `zulip/` directory and entering `git grep 'def check_send_message'`.

Modify check_send_message so that anytime a user sends a message which says
"Nanananana" the message becomes "Nanananana Batman!"

Test your change works in the browser.


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
your terminal.

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
lint tests again. You should see a bunch of output in red. Take a screenshot.


## Contributing to Zulip

Please skim or read the following. These will be helpful for contributing
to Zulip and will be good to refer back to in the future:
* [Git Guide](https://zulip.readthedocs.io/en/latest/git-guide.html)
* [Version Control Sytle](https://zulip.readthedocs.io/en/latest/version-control.html)
* [Coding Style](https://zulip.readthedocs.io/en/latest/code-style.html)
* [Testing](https://zulip.readthedocs.io/en/latest/testing.html)
* [Python Static Checker (mypy)](https://zulip.readthedocs.io/en/latest/mypy.html)

Additionally the following guides exist for contributing to zulip:
* [Writing Integrations](https://zulip.readthedocs.io/en/latest/integration-guide.html)
* [Writing New Features](https://zulip.readthedocs.io/en/latest/new-feature-tutorial.html)
* [Writing Views](https://zulip.readthedocs.io/en/latest/writing-views.html)
* [Writing Documentation](https://zulip.readthedocs.io/en/latest/README.html)


## Submit

Submit your code for check_send_message and the three screenshots you took above.
