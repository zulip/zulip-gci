# GCI Tasks: User Documentation

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

* Good written English.

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) task.

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

There are two types of task in this category, each corresponding to one of
the Task Types below. Let *feature* or *features* be the feature or set of
features mentioned in the task that brought you here.

### Task Type A

* First, search https://chat.zulip.org/help/ to see if it already
  discusses *feature*.  If it does, you will instead want to take that
  documentation, extract it to a new page (linked to from the main
  index page), and then edit it to make sure it is high quality and
  covers the topic fully.  You'll still want to do the research
  suggested in this task description, however.
* Play with the Zulip UI to learn how *feature* works in Zulip.
  Browse the documentation linked from the gear menu in the upper-left
  to see if it's documented there.  If you can't find out how to do
  something in Zulip (or whether it's even possible), ask about it on
  the `GCI tasks` stream; one of the mentors can likely answer it for
  you.
* Write an outline for documentation for *feature*, and post it to the
  Zulip `GCI tasks` stream to get feedback from mentors and other GCI
  participants on what you plan to include in your documentation.
* Now work on writing your new documentation!  You should add your
  documentation to a new file to the `templates/zerver/help/` directory of
  https://github.com/zulip/zulip/.
  The name of the file should be a lowercase, hyphenated version of *feature*
  like `view-the-markdown-source-of-a-message` for the feature "View the Markdown source of a message".
  The end result should be a nice
  and clear user guide for *feature*, written in Markdown.
* Add a link to your guide under the "Using Zulip"
  heading in `templates/zerver/help/index.md`.
* Verify your documentation looks as you intended and all links work;
  it's common to make small mistakes in the markdown that cause your
  documentation to not look right.
* Add a commit and submit a pull request to the
  https://github.com/zulip/zulip/ repository. The title of both the commit
  and the pull request should be `docs: Add user guide for *feature*`.
  Include a link to the pull request when you submit your task on the GCI
  website.

*Completion criteria*: This should be a polished product, something
that could go live on the site.  Mentors will check that that is
indeed the case, and that we are not copying text or images from other
products.

### Task Type B

Read the guides corresponding to *features*. For each feature, do the following:
* Follow the instructions step-by-step, completely precisely. Correct
  anything that is unclear, incorrect, and add any tips, warnings or other
  information the author may not have thought of.
* Edit the guide to conform to the
[user documentation style guide](https://zulip.readthedocs.io/en/latest/README.html#style-guide).
* Verify your documentation looks as you intended and all links work;
  it's common to make small mistakes in the markdown that cause your
  documentation to not look right.
* Add a commit for a each feature, with commit message like `docs: Edit
  change-your-name to conform to style guide`. Submit a single pull request
  with all your commits to the https://github.com/zulip/zulip/
  repository. The title of the pull request should be something like `docs:
  Edit Accounts Basics articles to conform to style guide.`

## General Notes

* The source for the user documentation is the Markdown files is under
`templates/zerver/help/` in the main Zulip repository (zulip/zulip).

* To see the current version of a user documentation file,
templates/zerver/help/feature.md in Markdown, reload your browser on
`http://<hostname>:9991/help/feature`, where `<hostname>` is either
`localhost` or the hostname of your VM.

* If there are visual elements that you'd like to be able to express
  in your user guide, but aren't sure how to, bring it up in the `GCI
  tasks` stream!  Our user guide rendering software is very new, and
  your feedback will help improve the documentation for the user guide
  system, and additionally, it should be possible to add features to
  the user guide system as needed.  If there's interest, we can create
  GCI tasks for adding some of those features!

* You can check out the other guides in `templates/zerver/help/` or at
  https://get.slack.help/hc/en-us/categories/200111606-Using-Slack for
  inspiration.

* That being said, it is *extremely important* that you not copy text or
  images from other products’ documentation. The companies that develop
  those products own the copyright to their documentation. If you are not
  sure what constitutes copying, please ask on the "user guides" topic of
  the "GCI tasks" stream at chat.zulip.org!
