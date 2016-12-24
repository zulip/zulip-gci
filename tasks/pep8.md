# GCI Tasks: PEP 8

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) and
  [intro to Zulip server development](https://codein.withgoogle.com/tasks/4799263762546688/) tasks.

## Background

PEP-8 (https://www.python.org/dev/peps/pep-0008/) is the standard style
guide for how to write Python code, covering issues like where the
whitespace should be in code. One can use special programs, called linters,
to check whether code matches a particular coding style; basically, a linter
program reads the code of another program and checks if it follows specific
syntactic rules about how the code is written.

Zulip’s linter tool `tools/lint-all` has been configured to support running
the standard PEP-8 linter for Python code style, but some of the rules are
not being checked because the Zulip codebase does not pass them. In a few
cases, the violations are intentional, but in other cases, the violations
are in code written before Zulip started enforcing the PEP-8 standard and
should be fixed. Our goal is to fix all the non-intentional PEP-8 violations
by the end of GCI.

## Task Description

Each task in this category involves making Zulip pass one or more of the PEP-8
rules. You can find the list of all the rules not being checked in the
`check_pep8` function in `tools/lint-all`. Each rule has a name like LNNN,
where L is a letter and the Ns are numbers.

Let *rules* be the rules in the task description on codein.withgoogle.com.

Steps for completing the task:

For each *rule* in *rules*:

  * Remove *rule* from the `ignored_rules` array in `tools/lint-all`. Leave the
    line-wrapping as is, in order to reduce rebase conflicts with other
    contributors.
  * Run `tools/lint-all --pep8`. This should print out a long list of errors.
  * Fix the errors. You can either do this by hand, write a script to do it,
    or some combination.
  * Run `tools/test-all`, and make sure your code (still) passes all the tests.
  * Add a commit with message 'pep8: Fix *rule* violations.'

Submit a pull request with all the commits.  The title of the pull
request should be 'pep8: Fix *rules*'.
Include a link to the pull request when you submit your task on the GCI website.

See git commit [6d93b3b](https://github.com/zulip/zulip/commit/6d93b3b) for an example.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review all the code changes, check that the
  commit messages are correct, that you've removed each *rule* from the
  `ignored_rules` array, and that there is reasonable justification for any
  excluded files (see next section).

## General notes

* If you think a style change would make the code less readable, would
  change the behavior of the code, or would otherwise be a regression, talk
  to a mentor on the "GCI Task" stream. We may end up adding the line or
  file to an exclude list.
