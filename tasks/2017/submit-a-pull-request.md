# Submit A Pull Request to Zulip GCI Submissions Repository

This task will familiarize you with our GitHub workflow.  If you
are already familiar with making a pull request in GitHub, feel free
to skip this task.

We **strongly recommend** doing the
[Get Comfortable With Git](https://codein.withgoogle.com/dashboard/tasks/5415336817983488/)
task first, since that task teaches you a lot of things you might
otherwise need to look up when working on this one.

## Task

**Please follow the directions below exactly step by step. We will return the submission even if you are missing only a period.**

Why?
* We want you to introduce you to Zulip's [commit discipline](http://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-discipline).
* We also want to introduce how to write good [commit messages](http://zulip.readthedocs.io/en/latest/contributing/version-control.html#commit-messages).
* Finally, if you do make a mistake, you'll be able to learn to [fix your commits](http://zulip.readthedocs.io/en/latest/git/fixing-commits.html).


The directions for the task is as follows (you should use Git in **command line** for this task):

* Fork the [zulip-gci-submissions](https://github.com/zulip/zulip-gci-submissions) repository.
If you are not sure what this means, refer to [this tutorial](
https://guides.github.com/activities/forking/#fork).

* Create a new branch called `submit-a-pull-request` in the forked repository.
If you are not sure what a branch is, refer to [this tutorial](
https://guides.github.com/activities/hello-world/#branch).

* Make a new folder `submit-a-pull-request/<username>` where `<username>` is your GitHub username.

* Create a new file called `hello-world.md` with the following
content, verbatim (exactly as written).

```
Hello world
I am username. :tada:
```

* Add a commit to the `submit-a-pull-request` branch with the changes above,
with commit message `Add hello-world.md.`
Refer to
[this tutorial](https://guides.github.com/activities/hello-world/#commit)
if you are not sure how to do this.

* Now open the file again and replace `username` in the file with your
  GitHub username.

* Commit the changes you just made with the commit message
`hello-world.md: Change username to GitHub handle.`

## Submit

* Open a Pull Request in the [zulip-gci-submissions](
  https://github.com/zulip/zulip-gci-submissions) repository with title
  "Submit a Pull Request". Refer to [this tutorial](
  https://guides.github.com/activities/hello-world/#pr) or 
  [this doc](http://zulip.readthedocs.io/en/latest/git/pull-requests.html#create-a-pull-request) on creating pull requests
  if you don't know how to open a pull request.

* Sign the Dropbox CLA - https://opensource.dropbox.com/cla/

* Post a link to the pull request when you submit your task on the GCI
  website. The link should look like
  `https://github.com/zulip/zulip-gci-submissions/pull/<number>`, where
  `<number>` is a number (specifically, the number of pull requests
  submitted to this repository so far).

* Double-check that your pull request has the right title, the right branch name,
  doesn't contain any typos, etc. Use our automatic grader for this task
  to find out if there is anything you should fix. You can find the script
  in the `zulip-gci-submissions` repository. Run it:
  ```shell
  python ./submit-a-pull-request/grader.py <your-pull-request-number> <your-github-username>
  ```
  If your PR is correct, the script will print:
  > LGTM.

  Otherwise, the script will tell you what it thinks is wrong. If the script
  is complaining, but you think that your PR is correct, discuss it on
  chat.zulip.org in the stream [GCI tasks](
  https://chat.zulip.org/#narrow/stream/GCI.20tasks) on the topic `submit-a-pull-request`.

The mentors will verify that you successfully created a pull request
with 2 commits, first adding the file and then editing it to contain
your username.  Once you've signed the Dropbox CLA, your pull request
will be merged. Congratulations!  You've learned the basics of GitHub
workflow.

Zulip has a detailed guide on how we use GitHub for our server project
that you may find useful reading as you continue to learn about Git and
GitHub: https://zulip.readthedocs.io/en/latest/git/index.html.

After you finish this task, a great next task is to learn how to use
the Zulip server development environment:
https://codein.withgoogle.com/dashboard/tasks/5165908538425344/
