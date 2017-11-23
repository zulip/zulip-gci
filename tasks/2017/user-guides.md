# GCI Tasks: User Documentation

## Prerequisites

* A working **Zulip development environment**. See
  [here](https://github.com/zulip/zulip-gci#setting-up-the-zulip-development-environment)
  for instructions on how to set one up.

* A **new feature branch** rebased off of the latest `upstream/master` remote
  branch. See [here](../../before-every-task.md) to learn how to do so.

* **Good written English.** Proper spelling, grammar, and word usage conventions
  are critical for this task, so you should be fluent in English if you decide
  to claim this task.

* **Completion of the
  [submit a pull request](./submit-a-pull-request.md) task**. The task helps
  you familiarize yourself with the Zulip workflow and is a great first
  contribution!

## Background

Well-written user documentation helps users and search engines discover Zulip
features. They are important since they are a medium through which we present
Zulip to our potential users and contributors. This task involves writing user
documentation for one of our features.

You can our read existing user documentation we have at
https://chat.zulip.org/help/ to accustom yourself with our writing style.

We have already written a
[guide](http://zulip.readthedocs.io/en/latest/subsystems/user-docs.html) for
writing user docs in the Zulip developer documentation. **Please read the entire
guide before you proceed with this task.**

## Task Description

In the following task description, *feature* or *features* represents the
features in the task description that you plan to document.

1. Play with the Zulip UI to learn how *feature* works in Zulip.
  If you can't find out how to do something in Zulip (or whether it's even
  possible), ask about it on the [GCI
  tasks](https://chat.zulip.org/#narrow/stream/GCI.20tasks) stream; one of the
  mentors can likely answer it for you.

2. Write an outline for documentation for *feature*, and post it to the
  [GCI tasks](https://chat.zulip.org/#narrow/stream/GCI.20tasks) stream to
  receive feedback from mentors and other GCI participants on what you plan to
  include in your documentation.

3. Write your new documentation while following the
  [user documentation style
  guide](http://zulip.readthedocs.io/en/latest/subsystems/user-docs.html). The
  end result should be a nice, clear user documentation article for *feature*
  written in Markdown located in the `templates/zerver/help/` folder.

4. Add a link to your article under the appropriate user documentation subsection
  in `templates/zerver/help/include/sidebar.md` to be included in the user
  documentation index and sidebar.

5. Verify your documentation looks as you intended and all links work; it's
  common to make small mistakes in the markdown that cause your documentation to
  not look right.

    **Tip:** To see the current Markdown version of a user documentation file,
    reload your browser on `http://<hostname>:9991/help/<feature>`, where
    `<hostname>` is either `localhost` or the hostname of your VM, and `<feature>`
    is the name of the feature.

6. Ensure your article passes our user documentation linter. You can modify your
  article to pass the linter by making sure it does not contain any trailing
  whitespace or have any lines greater than 80 characters (it's okay for lines
  with links to go up to 120 characters).

    **Tip:** You can run the linter by running `tools/test-help-documentation` in
    your Zulip development environment.

7. Add a commit and submit a pull request to the https://github.com/zulip/zulip/
  repository. The title of both the commit and the pull request should be `user
  docs: Add user guide for *feature*`.

8. Submit your task on the GCI website with a link to the pull request you just
  created in the comments of your GCI task.

## Additional Notes

* If there are visual elements that you'd like to be able to express in your
  user documentation article, but aren't sure how to, bring it up in the [GCI
  tasks](https://chat.zulip.org/#narrow/stream/GCI.20tasks) stream! Make sure to
  review all available
  [features](http://zulip.readthedocs.io/en/latest/subsystems/user-docs.html#features)
  of the Zulip markdown rendering engine before doing so.

* Although it is okay to read user documentation from other products for
  inspiration, it is *extremely important* that you not copy text or images from
  their user documentation because the companies that develop those products own
  the copyright to their documentation. If you are not sure what constitutes
  plagiarism, please ask on the `user guides` topic of the [GCI
  tasks](https://chat.zulip.org/#narrow/stream/GCI.20tasks) stream!
