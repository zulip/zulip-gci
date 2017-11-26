# GCI Tasks: Mypy Annotations

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) and
  [intro to Zulip server development](https://codein.withgoogle.com/tasks/4799263762546688/) tasks.

## Background

Mypy is an experimental static type checker for Python. Mypy ensures that
the codebase doesn't do things like pass a string (like `'42'`) to a function
that is expecting an int (like `42`).

You can read more about how mypy works at
http://zulip.readthedocs.io/en/latest/mypy.html.

Zulip has reached 100% mypy annotations coverage as a result of
work done during last year's code-in. Earlier, comments were used
to specify types to support both Python 2 and 3. As we're migrating our
codebase to Python 3 only, we can use the new PEP484 syntax for
type annotations.

Although we've built an automated script to convert most of these annotations, we
still need to convert methods with multiline definitions manually.

## Task Descriptions

### Task Type A

Let *file* be a file listed in the task that brought you here.
* Convert mypy annotations for all multiline methods in the *file*.
* Commit your changes with a commit message `mypy: User Python 3 syntax for typing in <file>.`

After you've converted the annotations for all the files, Submit a pull request,
with title  `mypy: Use Python 3 syntax for typing in <file>.`
  Include a link to the pull request when you submit your task on the GCI website.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review the code changes.
* Mentors should also make sure that the modified method definitions
are line-wrapped properly and readable

http://zulip.readthedocs.io/en/latest/mypy.html is a helpful document, as is
just looking at other files in the project and seeing their annotations.

## General notes

`tools/test-all` runs most of the tests in Travis, but is somewhat slow.
`tools/run-mypy` runs just the mypy tests. You can also run
`tools/run-mypy file` on a particular file or directory, which is even faster,
but may not catch all the mistakes in that file.
