# Submit A Pull Request to Zulip GCI Repository

This task will familiarize you with our GitHub workflow.  If you
are already familiar with making a pull request in GitHub, feel free
to skip this task.

As a first step, we recommend reading GitHub's
[hello world tutorial](https://guides.github.com/activities/hello-world/), which covers
forking a repository, creating a branch, creating commits, and make a new pull request
using only the GitHub web interface. You can also use command line Git for creating
branches and making commits. This is not necessary for completing this
task, but is a skill that you should learn sooner or later. Here is a
[great tutorial](https://try.github.io) if you want to learn command line Git.

## Task

* Fork the [zulip-gci](https://github.com/zulip/zulip-gci) repository.
If you are not sure what this means, refer to [this tutorial](https://guides.github.com/activities/forking/#fork).

* Create a new branch called `submit-a-pull-request` in the forked repository.
If you are not sure what a branch is, refer to [this tutorial](https://guides.github.com/activities/hello-world/#branch).

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

* Open a Pull Request in the zulip-gci repository with title "Submit a Pull Request".
  Refer to [this tutorial](https://guides.github.com/activities/hello-world/#pr)
  if you don't know how to open a pull request.

* Sign the Dropbox CLA using the link posted by the Dropbox CLA bot.

* Post a link to the pull request when you submit your task on the GCI
  website. The link should look like
  `https://github.com/zulip/zulip-gci/pull/<number>`, where `<number>` is a 2 or
  3 digit number.

The mentors will verify that you successfully created a pull request
with 2 commits, first adding the file and then editing it to contain
your username.  Once you've signed the Dropbox CLA, your pull request
will be merged. Congratulations!  You've learned the basics of GitHub
workflow.

Zulip has a detailed guide on how we use GitHub for our server project
that you may find useful reading as you continue to learn about Git and
GitHub: http://zulip.readthedocs.io/en/latest/git-guide.html.

After you finish this task, a great next task is to learn how to use
the Zulip server development environment:
https://codein.withgoogle.com/tasks/4799263762546688/
