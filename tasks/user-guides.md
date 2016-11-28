# GCI Tasks: User Documentation

## Prerequisites

* A working Zulip development environment. See
  https://github.com/zulip/zulip-gci/blob/master/README.md for instructions
  on how to set one up.
* Good written English.

## Background

Good user guides help users and search engines discover Zulip features. They
are important since they are a medium through which we present Zulip to our
potential users and contributors. This task involves writing a user
guide for one of our features.

You can see the existing user guide style content that we have at
https://chat.zulip.org/help/; that document may already have some
content related to the feature you're hoping to document.  Our plan is
to split that giant page into a number of smaller pages about
individual topics, rather than continuing to add more content to it.
So regardless of whether a topic is already covered there, there is
work to be done!

There is detailed documentation on how Zulip's documentation is
written available here:
http://zulip.readthedocs.io/en/latest/README.html

You should read it, especially the
[section on general user documentation](http://zulip.readthedocs.io/en/latest/README.html#general-user-documentation),
to make sure you're familiar with how to edit the documentation.

## Task Descriptions

There are three types of task in this category, each corresponding to one of
the Task Types below. Let *feature* be the feature mentioned in the task
that brought you here (if relevant).

### Task Type A

* First, search https://chat.zulip.org/help/ to see if it already
  discusses *feature*.  If it does, you will instead want to take that
  documentation, extract it to a new page (linked to from the main
  index page), and then edit it to make sure it is high quality and
  covers the topic fully.  You'll still want to do the research
  suggested in this task description, however.
* Look at the link in the task description to how *feature* works in
  Slack.
* Play with the Zulip UI to learn how *feature* works in Zulip.
  Browse the documentation linked from the gear menu in the upper-left
  to see if it's documented there.  If you can't find out how to do
  something in Zulip (or whether it's even possible), ask about it on
  the `GCI tasks` stream; one of the mentors can likely answer it for
  you.
* Write an outline for documentation for *feature*, and post it to the
  Zulip `GCI tasks` stream to get feedback from mentors and other GCI
  participants on what you plan to include in your documentation.
* Now work on writing your new documentation!  You should add your new
  documentaton to a new file with a clear, lowercase, hyphenated name
  like `edit-messages` or `mention-a-team-member`, to the
  `templates/zerver/help/` directory of
  https://github.com/zulip/zulip/.  The end result should be a nice
  and clear user guide for *feature*, using the outline from Task Type
  A. The user guide should be written in Markdown. Create a pull
  request adding it to the directory of the
  https://github.com/zulip/zulip/ repository. The title of both the
  commit and the pull request should be `docs: Add user guide for
  *feature*`.
* If there are visual elements that you'd like to be able to express
  in your user guide, but aren't sure how to, bring it up in the `GCI
  tasks` stream!  Our user guide rendering software is very new, and
  your feedback will help improve the documentation for the user guide
  system, and additionally, it should be possible to add features to
  the user guide system as needed.  If there's interest, we can create
  GCI tasks for adding some of those features!

*Completion criteria*: This should be a polished product, something
that could go live on the site.  Mentors will check that that is
indeed the case, and that we are not copying text or images from other
products.

### Task Type B

Read three of the guides that have been written by other GCI
contributors.  Try to follow the instructions step-by-step, completely
precisely, taking careful notes on any issues or mistakes you run
into.  Add those notes and any suggested edits as comments on the
appropriate pull requests (or if they have already been merged, just
make your changes and submit a pull request to update the text).

## General Notes

* The source for the user documentation is the Markdown files is under
`templates/zerver/help/` in the main Zulip repository (zulip/zulip).

* To see the current version of a user documentation file,
templates/zerver/help/feature.md in Markdown, reload your browser on
http://localhost:9991/help/feature.

* It is *extremely important* that you not copy text or images from other
products’ documentation. The companies that develop those products own the
copyright to their documentation. If you are not sure what constitutes
copying, please ask on the "user guides" topic of the "GCI tasks" stream at
chat.zulip.org!
