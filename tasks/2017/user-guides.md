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
Zulip to our potential users and contributors. This task involves reviewing and
writing user documentation for some of our features.

You can our read existing user documentation we have at
https://chat.zulip.org/help/ to accustom yourself with our writing style; most
of it was written by students during GCI 2016!

We have already written a
[guide](http://zulip.readthedocs.io/en/latest/subsystems/user-docs.html) for
writing user docs in the Zulip developer documentation. **Please read the entire
guide before you proceed with this task.**

## Task Descriptions

In the following task descriptions, *feature* or *features* represents the
features in the task description that you plan to document.

### Task Type A

In this task, you will write a new article to document an feature in Zulip.

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

#### Additional Notes

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
  
### Task Type B

In this task, you will carefully review existing user documentation and note
potential improvements to increase the documentation's clarity and readability.

1. Start your development environment. In your browser, visit
`http://<hostname>:9991/help` to view the index for general user documentation or
`http://<hostname>:9991/api` to visit our API documentation, where `hostname` is
either `localhost` or the hostname of your VM.

2. Read the documentation corresponding to *features*.

3. Follow the instructions in the article exactly step-by-step. Note any steps
in the procedure that are unclear, incorrect. Additionally, suggest any
tips, warnings, or other information the author may not have thought of that
should be added to the user documentation.

4. Review the images included in the article and compare them with the
corresponding features in the your development environment. Do any features look
different? If so, take and save a screenshot of those features.

5. Compare the article's writing style and conventions to the ones established
in the [user documentation style
guide](https://zulip.readthedocs.io/en/latest/subsystems/user-docs.html). Do any
parts not conform to the guide? List them and describe how they could be
revised.

6. Compile your notes into an organized Markdown document located in a folder
named `user-guides/<username>` where `<username>` represents your username
(this folder you will create in the [`zulip-gci-submissions`](https://github.com/zulip/zulip-gci-submissions/)
repository).
**Include at least 3 questions, comments, or suggestions you encountered while
reading each article.**

7. Add a commit titled `user guides: Review user documentation for <features>.`
to your branch. Submit a single pull request with from your branch to the
https://github.com/zulip/zulip-gci-submissions/ repository.

8. Paste the link of your new pull request in the comments of your task on the
GCI website, and submit your task for review afterwards.
