# GCI Tasks: User Documentation

## Prerequisites

* SET_UP_ZULIP_DEVELOPMENT_ENVIRONMENT

## Background

Good user guides help users and search engines discover Zulip features. They
are crucial since they are a medium through which we present Zulip to our
potential users and contributors. This task involves writing a user
guide for one of our features.

## Task Descriptions

There are three types of task in this category, each corresponding to one of
the Task Types below. Let *feature* be the feature mentioned in task that brought
you here (if relevant).

### Task Type A

* Look at the List of Features section below to see a link to how *feature*
  works in Slack. Play with the Zulip UI to learn how *feature* works in
  Zulip.
* Write an outline for documentation for *feature*. It doesn't have to be
  in Markdown, and it is okay if the writing isn't perfect, but it should
  include all the relevant content, including screenshots and links pointing
  to parts of the Zulip UI if appropriate.

  Put the outline and screenshots into a new directory
  `gci/user-documentation/<folder name>/`, where 'folder name' is something
  like edit-messages, or mention-a-team-member.
* Post your work as a pull request in the zulip/gci-submissions
  repository. The title of the pull request should be "User documentation A: *feature*"

*Completion criteria*: Mentors will check that the information is correct and complete.

### Task Type B

Write a nice and clear user guide for *feature*, using the outline from Task
Type A. The user guide should be written in Markdown. Create a pull request
adding it to the `templates/zerver/help/` directory of the zulip/gci-submissions
repository. The title of the pull request should be "User documentation B: *feature*"

*Completion criteria*: This should be a polished product, and something that
 could go live on the site. Mentors will check that that is indeed the case.

### Task Type C

Read three of the guides that have been written by other GCI contributors.
Try to follow the instructions step-by-step, completely precisely, taking
careful notes on any issues or mistakes you run into.  Add those notes and
any suggested edits as comments on the appropriate pull requests. Open a new
pull request with links to the three guides.
The title of the pull request should be "User documentation C: *feature1*, *feature2*, *feature3*"

## General Instructions

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

TODO: Add some others / better ones.



## List of Features

* Edit Messages: https://get.slack.help/hc/en-us/articles/202395258-Edit-or-delete-messages
* Mention a Team Member: https://get.slack.help/hc/en-us/articles/205240127-Mention-a-team-member
* Change Language: https://get.slack.help/hc/en-us/articles/215058658-Slack-in-different-languages
* Message Display Settings: https://get.slack.help/hc/en-us/articles/213893898-Change-your-message-display-settings
* Browse and Join Streams: https://get.slack.help/hc/en-us/articles/205239967-Browse-and-join-channels

TODO: Slack’s help center has around 100 total articles, of which probably 75 are applicable to Zulip on https://get.slack.help/hc/en-us/categories/200111606-Using-Slack and https://get.slack.help/hc/en-us/categories/200122103-Team-Administration).
