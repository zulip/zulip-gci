# GCI Tasks: User Documentation

## Prerequisites

* A working Zulip development environment. See
  https://github.com/zulip/zulip-gci/blob/master/README.md for instructions
  on how to set one up.

## Background

Good user guides help users and search engines discover Zulip features. They
are important since they are a medium through which we present Zulip to our
potential users and contributors. This task involves writing a user
guide for one of our features.

You can see the existing user guide style content that we have at
https://chat.zulip.org/help/; we may already have some content related
to the relevant feature.  If so, you should clean up that content and
extract it into its own page.

## Task Descriptions

There are three types of task in this category, each corresponding to one of
the Task Types below. Let *feature* be the feature mentioned in the task
that brought you here (if relevant).

### Task Type A

* Look at the link in the task description to how *feature* works in
  Slack. Play with the Zulip UI to learn how *feature* works in Zulip.
* Write an outline for documentation for *feature*. It doesn't have to be
  in Markdown, and it is okay if the writing isn't perfect, but it should
  include all the relevant content, including screenshots and links pointing
  to parts of the Zulip UI if appropriate.

  Put the outline and screenshots into a new directory
  `user-documentation/<folder name>/`, where 'folder name' is a lowercase
  version of *feature* with all spaces replaced with hyphens, like
  edit-messages, or mention-a-team-member.
* Post your work as a pull request in the zulip/zulip-gci repository
  (aka this one). The title of the commit should be
  `User guides: Add outline for *feature*`, and the title of the
  pull request should be "User guides A: *feature*".

*Completion criteria*: Mentors will check that the information is correct and complete.

### Task Type B

Write a nice and clear user guide for *feature*, using the outline
from Task Type A. The user guide should be written in Markdown. Create
a pull request adding it to the `templates/zerver/help/` directory of
the https://github.com/zulip/zulip/ repository. The title of both the
commit and the pull request should be `Add user guide for *feature*`.

*Completion criteria*: This should be a polished product, and something that
could go live on the site. Mentors will check that that is indeed the case,
and that we are not copying text or images from other products.

### Task Type C

Read three of the guides that have been written by other GCI
contributors.  Try to follow the instructions step-by-step, completely
precisely, taking careful notes on any issues or mistakes you run
into.  Add those notes and any suggested edits as comments on the
appropriate pull requests (or if they have already been merged, just
make your changes and submit a pull request to update the text).

## General Notes

* The source for the user documentation is the Markdown files is under
templates/zerver/help/ in the main Zulip repository (zulip/zulip).

* To see the current version of a user documentation file,
templates/zerver/help/feature.md in Markdown, reload your browser on
http://localhost:9991/help/feature.

* It is *extremely important* that you not copy text or images from other
products’ documentation. The companies that develop those products own the
copyright to their documentation. If you are not sure what constitutes
copying, please ask on the "user guides" topic of the "GCI tasks" stream at
chat.zulip.org!
