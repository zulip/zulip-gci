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

Zulip has reached 100% mypy annotations for the core library (see
http://blog.zulip.org/2016/10/13/static-types-in-python-oh-mypy/), but there
are several things left to do.

## Task Descriptions

### Task Type A

Python 2 and Python 3 have different string types, which makes it
complicated to annotate a codebase that supports both Python 2 and Python 3,
as Zulip currently does.

The old way of doing the annotation was to use `six.text_type`, which is a
type that acts as the Python 2 (or Python 3) type when the code is being run
with Python 2 (or Python 3, respectively). The new way is to use
`typing.Text`. See https://github.com/zulip/zulip/issues/1582 for a bit of
discussion around the change.

Let *set of directories* be the set of directories listed in the task that
brought you here. For each directory:

* Run `git grep text_type` from the directory to find all instances of
  `text_type` in the directory, or `git grep -c text_type` to just get the
  list of files.
* For each file:
  * Replace all `text_type` annotations with `Text`. A line is an annotation
  if and only if it starts with `# type: `.
  * Update the import statements. Add `typing.Text`, and remove
    `six.text_type` if it no longer appears in the file.
* Add a commit with commit message `mypy: Convert <directory> to use typing.Text.`

* Submit a pull request containing your commits with
  title `mypy: Use typing.Text in <set of directories>`.
  Include a link to the pull request when you submit your task on the GCI website.

See commit
[fdae58f](https://github.com/zulip/zulip/commit/fdae58f96b284b4153ff6b4fa4b07343647b85b2)
for an example.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review the code changes, check that the
  remaining `text_type`s (if any) are not mypy annotations, check the
  imports, and check the commit message.

### Task Type B

Let *file* be the file listed in the task that brought you here.
* Remove *file* from the `exclude_common` list in `tools/run-mypy`.
* Add mypy annotations to *file* until all the tests pass.
* Commit your changes with a commit message `mypy: Annotate *file*`.
* Submit a pull request, with title
  `mypy: Add annotations to <file>.`
  Include a link to the pull request when you submit your task on the GCI website.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review the code changes.

http://zulip.readthedocs.io/en/latest/mypy.html is a helpful document, as is
just looking at other files in the project and seeing their annotations.

## General notes

`tools/test-all` runs most of the tests in Travis, but is somewhat slow.
`tools/run-mypy` runs just the mypy tests. You can also run
`tools/run-mypy file` on a particular file or directory, which is even faster,
but may not catch all the mistakes in that file.
