# Intro

While reviewing pull requests on `zulip-gci` and submissions in the GCI app, and
when helping students on Zulip, I've encountered some common problems. This document
is a short list of common issues and some ideas on how to address them.

## Maintaining a positive attitude

The students are learning a lot and they are eager to tackle the challenges. That's
why I'm always positive:

  * I thank the student for their contribution

    `Thanks for posting the pull request! Looks great.`

  * I point out the issues in their submission

  * I ask them to fix the issues and thank them

    ```
    Could you submit your task in the app?

    Thanks!
    ```
    
### Student asks for extension

If a student asks for an extension on a task, you can go ahead and give it to them 
as long as they have *some* interaction on the task. The deadlines on tasks are 
mostly to allow tasks to go back into the pool if a student isn’t actively working 
on it, rather than to be a difficult deadline to meet.
```
I've given you an extra three days to complete the task, since you seem to be 
diligently working on it.
```

## Interaction on GitHub

### Student posts a PR without submitting the task

I ask the student if they have claimed and submitted the task:

`This looks great! Have you claimed and submitted the task in the GCI app?`

Some students say they'll do it after their PR is merged - I ask them to submit
the task in the GCI app, with more details:

```
You should submit the task in the GCI app, so the mentors know what they should review.
[The flow](https://github.com/zulip/zulip-gci/blob/master/docs/improving-gci-experience.md#why-is-it-taking-so-long-for-the-mentors-to-check-my-task) of reviewing tasks is first claiming them in the app, then submitting
and waiting for mentor review, then resubmitting them should there be a need for fixes.

Could you submit your task in the app?
```

### Student opens another PR on the same task

I go to all the previous PRs on this task and close them with comment:

`Another PR for this was opened at <PR_hash>`

I also ask the student to learn how to review and edit their commit history:

```
You don't have to open a new pull request each time you want to change what
you've submitted. You can update your feature branch and force push changes.
Changes pushed to your feature branch will be automatically updated in the
pull request. [This guide](https://github.com/zulip/zulip-gci/blob/master/docs/fixing-commits.md)
has some useful information on fixing commits and you can refer to [this guide](http://zulip.readthedocs.io/en/latest/git-guide.html?highlight=git#force-push-changes-to-github-after-you-ve-altered-your-history)
if you are not sure how to force push your changes. If you get stuck somewhere you
are always welcome to chat with us on [Zulip](https://chat.zulip.org). Thanks!
```

### Student doesn't know how to edit commit history

I point them to docs:

```
Some helpful docs:

- [fixing commits](https://zulip.readthedocs.io/en/latest/fixing-commits.html)
- [working copies](https://zulip.readthedocs.io/en/latest/working-copies.html)
- [Git guide](http://zulip.readthedocs.io/en/latest/git-guide.html)
```

### Student has the same problem for a prolonged time/the problem became complicated

I ask them to join us on Zulip, since it's much easier to discuss there:

`Can you come and chat with us on [Zulip](https://chat.zulip.org/)?`

## GCI app

### Student resubmits the task without properly reviewing it

I ask the student to make sure they don't have any obvious issues in their code
before resubmitting:

`Please make sure to look through all the files before you submit the task for
review. This will save time for you as well as the mentors, since we will have
to review your code less times, and you won't have to put your task so many times
in the review queue.`

## Zulip

### Student pings mentors constantly for reviews

I inform the student there is a queue of submissions and their submission will be
reviewed shortly:

```
The task is in the submissions queue, a mentor will get to it soon. In case you
are interested in knowing more about our submission queue system you can read
about it [here](https://github.com/zulip/zulip-gci/blob/master/docs/improving-gci-experience.md#why-is-it-taking-so-long-for-the-mentors-to-check-my-task).
Thanks!
```

# Improvements

Please add any other examples and suggestions you find useful.
