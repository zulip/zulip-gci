# GCI Tasks: PEP 8

## Prerequisites

* SET_UP_ZULIP_DEVELOPMENT_ENVIRONMENT

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
are in code written before Zulip started enforcing the PEP-8 standard, and
should be fixed. Our goal is to fix all the non-intentional PEP-8 violations
by the end of GCI.

## Task Description

Each task in this category involves making Zulip pass one of the PEP-8
rules. You can find the list of all the rules not being checked in the
`check_pep8` function in `tools/lint-all`. Each rule has a name like LNNN,
where L is a letter and the Ns are numbers.

Let *rule* be the rule in the task description on codein.withgoogle.com.

Steps for completing the task:

* Remove *rule* from the `ignored_rules` array in `tools/lint-all`. Leave the
  line-wrapping as is, in order to reduce rebase conflicts with other
  contributors.
* Run `tools/lint-all --pep8`. This should print out a long list of errors.
* Fix the errors.
* Run `tools/test-all`, and make sure your code (still) passes all the tests.
* Submit a pull request. Your commit message should be 'pep8: Fix *rule*
  violations.'

See git commit [6d93b3b](https://github.com/zulip/zulip/commit/6d93b3b) for an example.

*Completion criteria*:
* PASS_TRAVIS
* Mentor review. Mentors will review all the code changes, check that the
  commit message is correct, that you've removed *rule* from the
  `ignored_rules` array, and that there is reasonable justification for any
  excluded files (see next section).

## General notes

* TODO: If you think a style change would make the code less readable, would
  change the behavior of the code, or would otherwise be a regression, add
  the relevant file to the [???] list in `tools/lint-all` and add a comment
  to the pull request.
* The commit with the PEP-8 changes should have no other cleanup. If you end
  up making other code changes while doing this task, please put it in a
  separate commit.

## List of rules

Any special instructions for *rule* will appear below.

* TODO
