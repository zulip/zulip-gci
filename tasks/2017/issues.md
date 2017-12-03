# GCI Tasks: GitHub Issues

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Basic knowledge of git. We **strongly suggest** you finish the
  [Get Comfortable With Git](https://codein.withgoogle.com/dashboard/tasks/5415336817983488/)
  task first before attempting this.

* Experience working in the Zulip server environment.  We recommend
completing the
[Intro to Zulip Server development beginner task](https://github.com/zulip/zulip-gci/blob/master/tasks/intro-to-zulip-server.md)
before claiming a GitHub issue task, since most GitHub issues require
the knowledge you learn with that task.

* If you are interested in working on a issue in some other project
like our
[Python API and bots project](https://github.com/zulip/python-zulip-api),
[mobile app](https://github.com/zulip/zulip-mobile) or
[desktop app](https://github.com/zulip/zulip-electron), we recommend
going through the contribution and setup guide in their specific
repository (for some repos, there's a high-quality task that will help
teach you how the project works; we recommend doing those first).

* Some confidence from completing other tasks.  These tasks can be
  very rewarding, but they can also take many hours to complete.
  Also, since generally less pre-thought has been put into these
  issues by mentors, it's more likely that you might need to redo your
  work several times as it becomes apparent that the approach we'd had
  in mind isn't going to produce a good result.

## Background

Zulip Issues are the bugs and open feature requests for the Zulip Project.
We have a number of projects from which you can select issues to work on:

* Zulip Server and Web Frontend - https://github.com/zulip/zulip
* React Native Mobile App - https://github.com/zulip/zulip-mobile
* Electron Desktop App - https://github.com/zulip/zulip-electron
* Zulip Python API and Bots Framework - https://github.com/zulip/python-zulip-api

Issues we add as GCI tasks are generally labelled as "good first issue"
but you may work on any open issue in the project. If an issue you
want to work on is not available in the GCI UI, ask on the "GCI tasks"
stream for a mentor to create a task for it.

## Task Description

Read the description of the issue and discussion in the comments. Try
to understand all the considerations involved in the code. When you've
done enough reading to be confident you'll be able to make progress on
the issue, you can claim the issue on GitHub by commenting `@zulipbot
claim` on the Github issue (this will prevent Zulip contributors not
involved in GCI from starting working on the issue, and you should do
after claiming task in the GCI webapp).  zulipbot is a workflow
management bot for the Zulip project that streamlines GitHub issue
triage by allowing anyone to claim or label an issue and check the
issue's status. You can read more about zulipbot at
https://zulip.readthedocs.io/en/latest/contributing/zulipbot-usage.html

When making changes, carefully read the surrounding code to understand
the style in which it is written (which you'll want to replicate) and
its behavior.  When feasible, add tests for the new functionality, so
that it will continue working in the future.  Finally,
[write a reviewable series of commits](https://zulip.readthedocs.io/en/latest/contributing/version-control.html)
where the commit messages explain why your change both solves the
problem correctly and doesn't change anything else.

Make heavy use of tools like `git grep` and your code editor's search
features to find the definitions of relevant functions, chase the code
path of similar features, etc.

If you have any questions, ask on the "GCI tasks" stream (set the
topic to the issue number) or add comments to the discussion on
Github.

When you have completed the task, submit a pull request to the
respective github respository. Make sure you reference the issue
number in the
[commit message](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-messages).

Be sure to follow the instructions in the "Code Contribution Guide"
section on https://zulip.readthedocs.io/en/latest/.
