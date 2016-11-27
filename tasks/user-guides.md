# GCI Tasks: User Documentation

## Prerequisites

* SET_UP_ZULIP_DEVELOPMENT_ENVIRONMENT

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
  `gci/user-documentation/<folder name>/`, where 'folder name' is something
  like edit-messages, or mention-a-team-member.
* Post your work as a pull request in the zulip/gci-submissions
  repository. The title of the pull request should be "User guides A: *feature*"

*Completion criteria*: Mentors will check that the information is correct and complete.

### Task Type B

Write a nice and clear user guide for *feature*, using the outline from Task
Type A. The user guide should be written in Markdown. Create a pull request
adding it to the `templates/zerver/help/` directory of the zulip/gci-submissions
repository. The title of the pull request should be "User guides B: *feature*"

*Completion criteria*: This should be a polished product, and something that
could go live on the site. Mentors will check that that is indeed the case,
and that we are not copying text or images from other products.

### Task Type C

Read three of the guides that have been written by other GCI contributors.
Try to follow the instructions step-by-step, completely precisely, taking
careful notes on any issues or mistakes you run into.  Add those notes and
any suggested edits as comments on the appropriate pull requests. Open a new
pull request with links to the three guides.
The title of the pull request should be "User guides C: *feature1*, *feature2*, *feature3*"

## General Notes

* The source for the user documentation is the Markdown files under
templates/zerver/help/ in the main Zulip repository.

* To see the latest version of a user documentation file
templates/zerver/help/feature.md in Markdown, reload your browser on
http://localhost:9991/help/feature.

* It is *extremely important* that you not copy text or images from other
products’ documentation. The companies that develop those products own the
copyright to their documentation. If you are not sure what constitutes
copying, please ask on the [TODO] stream at chat.zulip.org!

* Some examples of good user guides:
** The “How to add tasks” section at https://asana.com/guide/get-started/begin/adding-assigning-tasks
** The [Create cute emoji](https://get.slack.help/hc/en-us/articles/206870177-Create-custom-emoji) guide of Slack.
** Let us know if you find others, and we'll add them here!
