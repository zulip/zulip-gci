# GCI Tasks: Legacy URLs migration

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.
* Experience working in the Zulip server environment.  We recommend
completing the
[Intro to Zulip Server development beginner task](https://github.com/zulip/zulip-gci/blob/master/tasks/intro-to-zulip-server.md)
before claiming a Legacy URLs migration task, since this will require
the knowledge you learn with that task.

## Background

Zulip has a number of "legacy" API URLs that are not properly
available via the Zulip REST API, which are present in
`zproject/legacy_urls.py` in the main Zulip project.

Please carefully read
[the master GitHub issue for this migration](https://github.com/zulip/zulip/issues/611)
for details on the migration and some notes on how to migrate one of
these URLs.

The goal is to migrate all of these URLs to new REST endpoints under
`v1_api_and_json_patterns` in `zproject/urls.py`; note that the
leading `/json` or `/api/v1` is not included in
`v1_api_and_json_patterns`, because both prefixes are added
automatically further down in `zproject/urls.py`.

The
[writing Zulip views](http://zulip.readthedocs.io/en/latest/writing-views.html)
documentation will also be helpful for completing this task.

## Task Description

Read the description linked in the previous section and relevant discussion.

Be sure to carefully search the Zulip codebase for how the old URL was
used; it may have been used in tests as well as in the frontend
JavaScript code.  You should use e.g. `git grep /json/foo` to make
sure you're changing every reference to a particular URL in the
codebase.

Also, make sure to manually test any frontend code paths before
submitting your changes for review.  It is very easy to accidentally
completely break a feature when doing this migration, so you must
manually test every reference in the frontend code that you change.

If you have any questions, ask on the "GCI tasks" stream (use "Legacy
URLs" as the topic) or add comments to the discussion on Github.

When you have completed the task, submit a pull request to the
`zulip/zulip` GitHub respository. Make sure you write a clear
[commit message](https://zulip.readthedocs.io/en/latest/version-control.html#commit-messages).

Be sure to follow the instructions in the "Code Contribution Guide"
section on http://zulip.readthedocs.io/en/latest/.
