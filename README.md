# Zulip Google Code-In repository

Welcome to the Zulip GCI landing page!

This page has information on [joining the developers' chat server](#community)
and [setting up a development
environment](#setting-up-the-zulip-development-environment).

Once you're done, we recommend browsing through Zulip's [extensive
documentation](https://zulip.readthedocs.io/en/latest/readme-symlink.html) about
its code and community. If you're planning on submitting a lot of code, we
particularly recommend the guides to
[git](https://zulip.readthedocs.io/en/latest/contributing/git-guide.html), [version
control](https://zulip.readthedocs.io/en/latest/contributing/version-control.html), [coding
style](https://zulip.readthedocs.io/en/latest/contributing/code-style.html), and
[testing](https://zulip.readthedocs.io/en/latest/testing/index.html).

## Community

Almost all GCI discussion (and discussion of Zulip more generally) happens
on our developers' server, https://chat.zulip.org. Create an account
and say hi on the "introductions" topic of the "GCI general" stream! When
signing up, check the box that says you are a GCI student.
This will subscribe you to the following streams (among others):

* [#GCI announce](https://chat.zulip.org/#narrow/stream/GCI.20announce):
Messages from the Zulip GCI mentors.
* [#GCI tasks](https://chat.zulip.org/#narrow/stream/GCI.20tasks): Task-specific
discussion or help.
* [#GCI help](https://chat.zulip.org/#narrow/stream/GCI.20help): Questions
(about code or otherwise) not related to a specific task.
* [#GCI general](https://chat.zulip.org/#narrow/stream/GCI.20general): General
discussion, feedback, questions, or anything you want!
* [#test here](https://chat.zulip.org/#narrow/stream/test.20here): Used for
sending test messages.

There are at least a dozen other active streams on the server; go to
https://chat.zulip.org/#streams/all to check them out.

Participating in an open source community is about more than just 
contributing code. It is about helping your fellow contributors with their
contributions as well. As such, one of the major considerations for the
competition winners will be how active you are in helping your fellow 
students. You can do this in two ways:
* Answer questions in any of the streams
* Help people during code review, so that by the time a mentor looks at the 
  pull request, your fellow student has enough feedback to make their PR 
  clean enough to approve. 

Please be kind in all of your interactions, and adhere to our 
[community code of conduct](https://zulip.readthedocs.io/en/latest/code-of-conduct.html).

A few non-obvious things that help keep the server manageable:
* All test messages should go to the [#test
here](https://chat.zulip.org/#narrow/stream/test.20here) stream.
* Always use a topic. If you're not sure what to put, you can use your name.
* When asking for help, include as much detail as you can, in particular,
  what you tried, and the full traceback of any error messages you got.

## Setting up the Zulip Development environment

Most coding tasks require a working Zulip development environment. There are
two strategies for setting one up.

### Remote VM

Zulip has partnered with Digital Ocean to provide VMs for GCI
participants developing Zulip.  To get a VM,
[follow the instructions here](https://zulip.readthedocs.io/en/latest/request-remote-dev.html).

Once you have access to your VM, take a look at our tips for [editing code on a
remote development server
machine](https://zulip.readthedocs.io/en/latest/development/remote.html#making-changes-to-code-on-your-remote-development-server).

### Local install

See the [Vagrant environment setup
tutorial](https://zulip.readthedocs.io/en/latest/development/setup-vagrant.html)
for installing Zulip on Linux or OS X. There are also instructions for
installing locally on Windows, though the setup can be tricky.

There is also documentation for using Docker or installing directly on
Ubuntu. We don't recommend either of those methods unless you have a
specific reason to prefer them.

### How to choose

Setting up a Remote VM can be faster, but day to day development can be more
convenient with a local install. If you are running Windows, have a slow
internet connection (the local install is ~500 Mb), or are planning on doing
a small number of Zulip tasks, we recommend starting with the remote VM.
You can always set up a local install later.

## GCI repositories

This repository is the home for Google Code In documentation, code, task 
descriptions, and anything else that helps us keep Google Code In organized. 

Many of the tasks will instruct you to submit pull requests and create github 
issues on a github respository that we made especially for 
[student submissions](https://github.com/zulip/zulip-gci-submissions) 
that do not yet have a place in other Zulip repositories.

If you are not sure how to submit a pull request (or what that even means), check out our
[beginner task](https://github.com/zulip/zulip-gci/tree/master/submit-a-pull-request)
on this topic.

## Can't find the perfect task to work on?

Zulip has hundreds of open issues that we'd like to resolve that don't
have corresponding GCI tasks; many of them have been tagged as
"good first issue" because we expect them to be accessible to new contributors:

https://github.com/zulip/zulip/issues?page=3&q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22+no%3Aassignee

You're encouraged to browse that list! If you see a project in there
that you're excited about helping with, ask about it on
https://chat.zulip.org; it's likely that we'll be happy to create a GCI task
for it. Additionally, you can comment `@zulipbot claim` on it to have our
GitHub bot [@zulipbot](https://github.com/zulipbot) officially assign the issue
to you. You can read more about using **@zulipbot**
[here](https://zulip.readthedocs.io/en/latest/contributing/zulipbot-usage.html).

## Information for GCI mentors

This repository also contains items generally related to Zulip's
participation in Google Code-In.

At the moment, this includes:

* `docs/`: Documentation that you can point students to in order to 
  help them learn about how open source works. 
* `scripts/`: Tools for iterating over the tasks in a category and
  creating actual GCI tasks out of them.
* `tasks/`: Template descriptions for large categories of tasks.  We
  put the bulk of the descriptions in this repo rather than in the GCI
  interface so that it's possible to update the documentation on how
  to do things as we see what folks find confusing.

For each major category of tasks, we'll want to have both a template
description under `tasks/` as well as a script under `scripts/` to import
the tasks into the GCI web application.  We'll run the relevant scripts
as tasks are ready to be published.
