# GCI Tasks: GitHub Issues

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.
* Experience working in the Zulip server environment.  We recommend
completing the
[Intro to Zulip Server development beginner task](https://github.com/zulip/zulip-gci/blob/master/tasks/intro-to-zulip-server.md)
before claiming a GitHub issue task, since most GitHub issues require
the knowledge you learn with that task.
* If you are interested in working on a issue in some other project like the
mobile or desktop app, we recommend going through the contribution and setup
guide in their specific repository.

## Background

Zulip Issues are the bugs and open feature requests for the Zulip Project.
We have a number of projects from which you can select issues to work on:

* Zulip Server and Web Frontend - http://github.com/zulip/zulip
* React Native Mobile App - http://github.com/zulip/zulip-mobile
* Electon Desktop App - https://github.com/zulip/zulip-electron
* Zulip Python API and Bots Framework - https://github.com/zulip/python-zulip-api

Issues we add as GCI tasks are generally labelled as "good first issue"
but you may work on any open issue in the project. If an issue you
want to work on is not available in the GCI UI, ask on the "GCI tasks"
stream for a mentor to create a task for it.

## Task Description

Read the description of the issue and discussion in the comments. Try to understand
all the considerations involved in the code. When you're ready to start working,
you can claim the issue by commenting `@zulipbot claim` on the Github issue.
zulipbot is a workflow management bot for the Zulip project that streamlines
GitHub issue triage by allowing anyone to claim or label an issue and check the
issue's status. You can read more about zulipbot at
http://zulip.readthedocs.io/en/latest/contributing/zulipbot-usage.html

When making changes, carefully read the surrounding code to understand
the style in which it is written (which you'll want to replicate)
and its behavior.  When feasible, add tests for the new functionality,
so that it will continue working in the future.

If you have any questions, ask on the "GCI tasks" stream (set the
topic to the issue number) or add comments to the discussion on
Github.

When you have completed the task, submit a pull request to the
respective github respository. Make sure you reference the issue
number in the
[commit message](https://zulip.readthedocs.io/en/latest/version-control.html#commit-messages).

Be sure to follow the instructions in the "Code Contribution Guide"
section on http://zulip.readthedocs.io/en/latest/.
