# GCI Tasks: User Documentation

Good user guides help users and search engines discover Zulip features. They
are crucial since they are a medium through which we present Zulip to our
potential users and contributors.

## General Instructions

* All the tasks below require a working Zulip development environment. Complete the
[add link to task for setting up dev environment] task first if you haven't already.

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

## Task Descriptions

There are three types of task in this category, each corresponding to one of
the Parts below. Let *feature* be the feature mentioned in task that brought
you here (if relevant).

### Part 1

* Look at the list below to see a link to how *feature* works in Slack. Play
  with the Zulip UI to learn how *feature* works in Zulip.
* Write an outline for documentation for this feature. It doesn't have to be
  in Markdown, and it is okay if the writing isn't perfect, but it should
  include all the relevant content, including screenshots and links pointing
  to parts of the Zulip UI if appropriate.
* Post your work as an issue on GitHub using
  https://github.com/zulip/zulip-gci/issues/new.

### Part 2

Write a nice and clear user guide for *feature*, using the outline from Part
1. The user guide should be written in Markdown. Create a pull request
adding it to the templates/zerver/help/ directory of the zulip-gci
repository.

### Part 3

Read three of the guides that have been written by other GCI contributors.
Try to follow the instructions step-by-step, completely precisely, taking
careful notes on any issues or mistakes you run into.  Submit those notes
and any suggested edits to the documentation.

## List of Features

* Edit Messages: https://get.slack.help/hc/en-us/articles/202395258-Edit-or-delete-messages
* Mention a Team Member: https://get.slack.help/hc/en-us/articles/205240127-Mention-a-team-member
* Change Language: https://get.slack.help/hc/en-us/articles/215058658-Slack-in-different-languages
* Message Display Settings: https://get.slack.help/hc/en-us/articles/213893898-Change-your-message-display-settings
* Browse and Join Streams: https://get.slack.help/hc/en-us/articles/205239967-Browse-and-join-channels

TODO: Slack’s help center has around 100 total articles, of which probably 75 are applicable to Zulip on https://get.slack.help/hc/en-us/categories/200111606-Using-Slack and https://get.slack.help/hc/en-us/categories/200122103-Team-Administration).
