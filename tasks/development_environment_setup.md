# Beginner - GCI Tasks: Setting up Your Development Environment

To contribute to Zulip you will need a working development environment and be
familiar with running zulip, testing code, building documentation, etc. This
task is designed to help you familiarize youself with doing this.

## Setting Up Your Development Environment.

#### OSX and Linux

We recomend running the zulip environment locally. See the using
[Vagrant](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html) tutorial.

There is also documentation for using
[Docker](https://zulip.readthedocs.io/en/latest/install-docker-dev.html), installing
[locally on Ubuntu](https://zulip.readthedocs.io/en/latest/install-ubuntu-without-vagrant-dev.html),
or [remotely](#remote).

#### Windows

We recomend running development [remotely](#remote)

You can use
[Vagrant](https://zulip.readthedocs.io/en/latest/dev-env-first-time-contributors.html) but
we have found getting the setup on windows tricky.

#### Remote

Zulip has partnered with Digital Ocean to provide VMs for GCI participants to develop Zulip.

TODO fill in Digital Ocean specific setup details.

Once you have setup your VM running see the [remote development tutorial](https://zulip.readthedocs.io/en/latest/dev-remote.html)


## Contributing to Zulip

Once you have setup your development environment please skim or read the following.
These will be helpful for contributing to Zulip and will be good to refer back
to in the future:
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

## Practice Running Zulip

Run your zulip server using

```
tools/run-dev.py
```

and verify that you can log in to your test instance.

#### Task

Modify check_send_message so that anytime a user sends a message which says
'Nanananana' the message becomes 'Nanananana Batman!'

Then add a test to verify this behavior.

#### Testing

Test your change works in the browser. Take a screenshot.

Then run
```
./tools/test-all
```
to verify that your code still passes tests. If it doesn't, fix any brokenness in the tests or your code.

Those tests took a while to pass. Run
```
cat tools/test-all
```
and figure out how to run just the lint tests and do so.

Take a screenshot and submit the two screenshots.
