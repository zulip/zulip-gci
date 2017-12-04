# GCI Tasks: Mypy Annotations

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/dashboard/tasks/4884433561714688/) and
  [intro to Zulip server development](https://codein.withgoogle.com/dashboard/tasks/5165908538425344/) tasks.

## Background

Mypy is an experimental static type checker for Python. Mypy ensures that
the codebase doesn't do things like pass a string (like `'42'`) to a function
that is expecting an int (like `42`).

You can read more about how mypy works at
http://zulip.readthedocs.io/en/latest/contributing/mypy.html.

Zulip was the
[first large project to be 100% mypy annotated](https://blog.zulip.org/2016/10/13/static-types-in-python-oh-mypy/).
Originally, comments were used to specify the types (to support both
Python 2 and 3).  However, since Zulip has dropped Python 2 support,
we can use the new PEP484 syntax for type annotations (supported by
Python 3), which is nicer and more readable.

Although we've built an automated script to convert most of these
annotations, the automated script only works with single-line
functions.  So we need your help to convert methods with multi-line
definitions manually.

## Task Descriptions

### Task Type A

Let *file* be a file listed in the task that brought you here.

* Convert mypy annotations for all multi-line methods in *file* (the
  single-line methods may or may not already be converted.  Don't
  bother converting them: manual conversions are more error-prone than
  automated ones, so it's better for you to leave them for the tool to
  migrate).

* Commit your changes with a commit message titled `mypy: Use Python 3
  type syntax in <file>.`

After you've converted the annotations for all the files, Submit a pull request,
with title  `mypy: Use Python 3 syntax for typing in <file>.`
  Include a link to the pull request when you submit your task on the GCI website.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review the code changes, as well as your
  individual commits and commit messages.
* Mentors should also make sure that the modified method definitions
  are line-wrapped properly and readable.

http://zulip.readthedocs.io/en/latest/mypy.html is a helpful document, as is
just looking at other files in the project and seeing their annotations.

#### General notes

`tools/test-all` runs most of the tests in Travis, but is somewhat slow.
`tools/run-mypy` runs just the mypy tests. You can also run
`tools/run-mypy file` on a particular file or directory, which is even faster,
but may not catch all the mistakes in that file.

### Task Type B

If you are not familiar with Zulip's interactive bots, please do the following
two tasks before attempting this task:

* [Learn about interactive bots, pt 1: running the helloworld bot.](https://codein.withgoogle.com/tasks/4753673148170240/)
* [Learn about interactive bots, pt 2: creating a message info bot.](https://codein.withgoogle.com/tasks/4787585941504000/)

Let *bot* be a bot listed in the task that brought you here.

* Write mypy annotations for all methods in the bot's main file and test
  file, as well as any other python files in the directory
  `python-zulip-api/zulip_bots/zulip_bots/bots/<bot>`.

* Add all the files you've just annotated to the `force_include` list in
  `tools/run-mypy`. Test your local changes by running
  `tools/test-static-analysis` and `tools/test-bots`.

* Commit your changes with a commit message titled `mypy: Add annotations for <bot>.`

After you've converted the annotations for all the listed bots, submit
a pull request with title  `mypy: Add annotations for bots.` to the
https://github.com/zulip/python-zulip-api repository. Include a link to
the pull request when you submit your task on the GCI website.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review the code changes, as well as your
  individual commits and commit messages.
* Mentors should also make sure that the modified method definitions
  are line-wrapped properly and readable.

#### General notes:

Take a look at
[this commit](https://github.com/zulip/python-zulip-api/commit/8cd310493a99dc95a949983a45206c0de8980df1)
as an example of adding annotations to a bot.
http://zulip.readthedocs.io/en/latest/mypy.html is a helpful document as well.
