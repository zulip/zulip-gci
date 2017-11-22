# GCI Git & GitHub Guide

This a shortened version of zulip's git guide specifically focused on GCI
students. You can read the original version [here][zulip-git-guide].

## Quick start: How Zulip uses Git and GitHub

This quick start provides a brief overview of how Zulip uses Git and GitHub.

Those who are familiar with Git and GitHub should be able to start contributing
with these details in mind:

- We use **GitHub for source control and code review.** To contribute, fork
  [zulip/gci-submissions-2017][github-gci-submissions] (or the appropriate
  [repository][github-zulip]) to your own account and then create feature/issue
  branches. When you're ready to get feedback, submit a work-in-progress (WIP) pull
  request. *We encourage you to submit WIP pull requests early and often.*

- We use a **[rebase][gitbook-rebase]-oriented workflow.** We do not use merge
  commits. This means you should use `git fetch` followed by `git rebase`
  rather than `git pull` (or you can use `git pull --rebase`). Also, to prevent
  pull requests from becoming out of date with the main line of development,
  you should rebase your feature branch prior to submitting a pull request, and
  as needed thereafter. If you're unfamiliar with how to rebase a pull request,
  [read this excellent guide][github-rebase-pr].

  We use this strategy in order to avoid the extra commits that appear
  when another branch is merged, that clutter the commit history (it's
  popular with other large projects such as Django).  This makes
  Zulip's commit history more readable, but a side effect is that many
  pull requests we merge will be reported by GitHub's UI as *closed*
  instead of *merged*, since GitHub has poor support for
  rebase-oriented workflows.

- We have a **[code style guide][zulip-rtd-code-style]**, a **[commit message
  guide][zulip-rtd-commit-messages]**, and strive for each commit to be *a
  minimal coherent idea* (see **[commit
  discipline][zulip-rtd-commit-discipline]** for details).

- We provide **many tools to help you submit quality code.** These include
  [linters][zulip-rtd-lint-tools], [tests][zulip-rtd-testing], continuous
  integration with [Travis CI][travis-ci], and [mypy][zulip-rtd-mypy].

- We use [zulipbot][zulip-rtd-zulipbot-usage] to manage our issues and
pull requests to create a better GitHub workflow for contributors.

***

The following sections will help you be awesome with Zulip and Git/GitHub in a
rebased-based workflow. Read through it if you're new to git, to a rebase-based
git workflow, or if you'd like a git refresher.

## Set up Git

If you're already using Git, have a client you like, and a GitHub account, you
can skip this section. Otherwise, read on!

### Install and configure Git, join GitHub

If you're not already using Git, you might need to [install][gitbook-install]
and [configure][gitbook-setup] it.

**If you are using Windows 10, make sure you [are running Git BASH as an
administrator][git-bash-admin] at all times.**

You'll also need a GitHub account, which you can sign up for
[here][github-join].

We also highly recommend the following:

- [Configure Git][gitbook-config] with your name and email.  We
  recommend using your full name (not just your first name), since
  that's what we'll use to give credit to your work in places like the
  Zulip release notes.
- Install the command auto-completion and/or git-prompt plugins available for
  [Bash][gitbook-other-envs-bash] and [Zsh][gitbook-other-envs-zsh].

### Get a graphical client

Even if you're comfortable using git on the command line, having a graphic
client can be useful for viewing your repository. This is especially when doing
a complicated rebases and similar operations because you can check the state of
your repository after each command to see what changed. If something goes
wrong, this helps you figure out when and why.

If you don't already have one installed, here are some suggestions:

- macOS: [GitX-dev][gitgui-gitxdev]
- Ubuntu/Linux: [git-cola][gitgui-gitcola], [gitg][gitgui-gitg], [gitk][gitgui-gitk]
- Windows: [SourceTree][gitgui-sourcetree]

If you like working on the command line, but want better visualization and
navigation of your git repo, try [Tig][tig], a cross-platform ncurses-based
text-mode interface to Git.

And, if none of the above are to your liking, try [one of these][gitbook-guis].

## Important Git terms

When you install Git, it adds a manual entry for `gitglossary`. You can view
this glossary by running `man gitglossary`. Below we've included the git terms
you'll encounter most often along with their definitions from *gitglossary*.

### branch
A "branch" is an active line of development. The most recent commit
on a branch is referred to as the tip of that branch. The tip of
the branch is referenced by a branch head, which moves forward as
additional development is done on the branch. A single Git
repository can track an arbitrary number of branches, but your
working tree is associated with just one of them (the "current" or
"checked out" branch), and HEAD points to that branch.

### cache
Obsolete for: index

### checkout
The action of updating all or part of the working tree with a tree
object or blob from the object database, and updating the index and
HEAD if the whole working tree has been pointed at a new branch.

### commit
As a noun: A single point in the Git history; the entire history of
a project is represented as a set of interrelated commits. The word
"commit" is often used by Git in the same places other revision
control systems use the words "revision" or "version". Also used as
a short hand for commit object.

As a verb: The action of storing a new snapshot of the project's
state in the Git history, by creating a new commit representing the
current state of the index and advancing HEAD to point at the new

### fast-forward
A fast-forward is a special type of merge where you have a revision
and you are "merging" another branch's changes that happen to be a
descendant of what you have. In such these cases, you do not make a
new mergecommit but instead just update to their revision. This will
happen frequently on a remote-tracking branch of a remote
repository.

### fetch
Fetching a branch means to get the branch's head ref from a remote
repository, to find out which objects are missing from the local
object database, and to get them, too. See also git-fetch(1).

### hash
In Git's context, synonym for object name.

### head
A named reference to the commit at the tip of a branch. Heads are
stored in a file in $GIT_DIR/refs/heads/ directory, except when
using packed refs. (See git-pack-refs(1).)

### HEAD
The current branch. In more detail: Your working tree is normally
derived from the state of the tree referred to by HEAD. HEAD is a
reference to one of the heads in your repository, except when using
a detached HEAD, in which case it directly references an arbitrary
commit.

### index
A collection of files with stat information, whose contents are
stored as objects. The index is a stored version of your working
tree. Truth be told, it can also contain a second, and even a third
version of a working tree, which are used when merging.

### pull
Pulling a branch means to fetch it and merge it. See also git-
pull(1).

### push
Pushing a branch means to get the branch's head ref from a remote
repository, find out if it is a direct ancestor to the branch's
local head ref, and in that case, putting all objects, which are
reachable from the local head ref, and which are missing from the
remote repository, into the remote object database, and updating
the remote head ref. If the remote head is not an ancestor to the
local head, the push fails.

### rebase
To reapply a series of changes from a branch to a different base,
and reset the head of that branch to the result.

It is fine if you don't understand all of these terms in first pass.
They will start to make sense as you start using git.

## How Git is different

Whether you're new to Git or have experience with another version control
system (VCS), it's a good idea to learn a bit about how Git works. We recommend
this excellent presentation *[Understanding Git][understanding-git]* from
Nelson Elhage and Anders Kaseorg and the [Git Basics][gitbook-basics] chapter
from *Pro Git* by Scott Chacon and Ben Straub.

Here are the top things to know:

- **Git works on snapshots:** Unlike other version control systems (e.g.,
  Subversion, Perforce, Bazaar), which track files and changes to those files
  made over time, Git tracks *snapshots* of your project. Each time you commit
  or otherwise make a change to your repository, Git takes a snapshot of your
  project and stores a reference to that snapshot. If a file hasn't changed,
  Git creates a link to the identical file rather than storing it again.

- **Most Git operations are local:** Git is a distributed version control
  system, so once you've cloned a repository, you have a complete copy of that
  repository's *entire history*. Staging, committing, branching, and browsing
  history are all things you can do locally without network access and without
  immediately affecting any remote repositories. To make or receive changes
  from remote repositories, you need to `git fetch`, `git pull`, or `git push`.

- **Nearly all Git actions add information to the Git database**, rather than
  removing it. As such, it's hard to make Git perform actions that you can't
  undo. However, Git can't undo what it doesn't know about, so it's a good
  practice to frequently commit your changes and frequently push your commits to
  your remote repository.

- **Git is designed for lightweight branching and merging.** Branches are
  simply references to snapshots. It's okay and expected to make a lot of
  branches, even throwaway and experimental ones.

- **Git stores all data as objects, of which there are four types:** blob
  (file), tree (directory), commit (revision), and tag. Each of these objects
  is named by a unique hash, the SHA-1 has of its contents. Most of the time
  you'll refer to objects by their truncated hash or more human-readable
  reference like `HEAD` (the current branch). Blobs and trees represent files
  and directories. Tags are named references to other objects. A commit object
  includes: tree id, zero or more parents as commit ids, an author (name,
  email, date), a committer (name, email, date), and a log message. A Git
  repository is a collection of mutable pointers to these objects called
  **refs**.

- **Cloning a repository creates a working copy.** Every working copy has a
  `.git` subdirectory, which contains its own Git repository. The `.git`
  subdirectory also tracks the *index*, a staging area for changes that will
  become part of the next commit. All files outside of `.git` is the *working
  tree*.

- **Files tracked with Git have possible three states: committed, modified, and
  staged.** Committed files are those safely stored in your local `.git`
  repository/database. Staged files have changes and have been marked for
  inclusion in the next commit; they are part of the index. Modified files have
  changes but have not yet been marked for inclusion in the next commit; they
  have not been added to the index.

- **Git commit workflow is as follows:** Edit files in your *working tree*. Add
  to the *index* (that is *stage*) with `git add`. *Commit* to the HEAD of the
  current branch with `git commit`.

## Getting your hands dirty

People learn more by doing things rather than reading its theoretical concepts.
Applying same philosophy here, lets jump into using git. So first step in this
regard will be understanding Zulip's git workflow. Zulip uses a **forked-repo**
and **[rebase][gitbook-rebase]-oriented workflow.**. This means that all
contributors create a fork of the [Zulip repository][github-zulip] they want to
contribute to and then submit pull requests to the upstream repository to have
their contributions reviewed and accepted. We also recommend you work on feature
branches. So lets get started:

### Setting up your playground

#### Step 1: Create your fork

The following steps you'll only need to do the first time you setup a machine
for contributing to a given Zulip project. You'll need to repeat the steps for
any additional Zulip projects ([list][github-zulip]) that you work on.

As a GCI student you will be mostly working on submissions repo for 2017. The
first thing you'll want to do is to is fork ([see how][github-help-fork]) the
[GCI submissions repository][github-zulip-submissions-2017].

#### Step 2: Clone to your machine

Next, clone your fork to your local machine:

```
$ git clone https://github.com/<your_username>/gci-submissions-2017.git
Cloning into 'gci-submissions-2017'
remote: Counting objects: 86768, done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 86768 (delta 5), reused 1 (delta 1), pack-reused 86752
Receiving objects: 100% (86768/86768), 112.96 MiB | 523.00 KiB/s, done.
Resolving deltas: 100% (61106/61106), done.
Checking connectivity... done.
```

#### Step 3: Connect your fork to upstream

Next you'll want to [configure an upstream remote repository][github-help-conf-remote] for your
fork. This will allow you to [sync changes][github-help-sync-fork] from the main repo back into
your fork.

First, view the currently configured remote repository:

```
$ git remote -v
origin  https://github.com/<your_username>/gci-submissions-2017.git (fetch)
origin  https://github.com/<your_username>/gci-submissions-2017.git (push)
```

Note: If you've cloned the repository using a graphical client, you may already
have the upstream remote repository configured. For example, when you clone
[zulip/gci-submissions-2017][github-gci-submissions-2017] with the GitHub desktop
client it configures the remote repository `gci-submissions-2017` and you see the
following output from `git remote -v`:

```
origin                  https://github.com/<your_username>/gci-submissions-2017.git (fetch)
origin                  https://github.com/<your_username>/gci-submissions-2017.git (push)
gci-submissions-2017    https://github.com/zulip/gci-submissions-2017.git (fetch)
gci-submissions-2017    https://github.com/zulip/gci-submissions-2017.git (push)
```

Even if your client has automatically configured a remote for zulip/gci-submissions-2017, we
recommend that you add a remote as follows to avoid confusion while reading this guide or while
asking for help on [Zulip][zulip-chat]:

```
$ git remote add upstream https://github.com/zulip/gci-submissions-2017.git
```

Finally, confirm that the new remote repository, upstream, has been configured:

```
$ git remote -v
origin  https://github.com/<your_username>/gci-submissions-2017.git (fetch)
origin  https://github.com/<your-username>/gci-submissions-2017.git (push)
upstream https://github.com/zulip/gci-submissions-2017.git (fetch)
upstream https://github.com/zulip/gci-submissions-2017.git (push)
```

## Using Git as you work

### Know what branch you're working on

When using Git, it's important to know which branch you currently have checked
out because most git commands implicitly operate on the current branch. You can
determine the currently checked out branch several ways.

One way is with [git status][gitbook-git-status]:

```
$ git status
On branch issue-demo
nothing to commit, working directory clean
```

Another is with [git branch][gitbook-git-branch] which will display all local
branches, with a star next to the current branch:

```
$ git branch
* issue-demo
  master
```

To see even more information about your branches, including remote branches,
use `git branch -vva`:

```
$ git branch -vva
* issue-123                 517468b troubleshooting tip about provisioning
  master                    f0eaee6 [origin/master] bug: Fix traceback in get_missed_message_token_from_address().
  remotes/origin/HEAD       -> origin/master
  remotes/origin/issue-1234 4aeccb7 Another test commit, with longer message.
  remotes/origin/master     f0eaee6 bug: Fix traceback in get_missed_message_token_from_address().
  remotes/upstream/master   dbeab6a Optimize checks of test database state by moving into Python.
```

You can also configure [Bash][gitbook-other-envs-bash] and
[Zsh][gitbook-other-envs-zsh] to display the current branch in your prompt.

### Keep your fork up to date

You'll want to [keep your fork][github-help-sync-fork] up-to-date with changes
from Zulip's main repositories.

**Note about git pull**: You might be used to using `git pull` on other
projects. With Zulip, because we don't use merge commits, you'll want to avoid
it. Rather that using `git pull`, which by default is a shortcut for `git fetch
&& git merge FETCH_HEAD` ([docs][gitbook-git-pull]), you should use `git fetch`
and then `git rebase`.

First, [fetch][gitbook-fetch] changes from Zulip's upstream repository you
configured in the step above:

```
$ git fetch upstream
```

Next, checkout your `master` branch and [rebase][gitbook-git-rebase] it on top
of `upstream/master`:

```
$ git checkout master
Switched to branch 'master'

$ git rebase upstream/master
```

This will rollback any changes you've made to master, update it from
`upstream/master`, and then re-apply your changes. Rebasing keeps the commit
history clean and readable.

When you're ready, [push your changes][github-help-push] to your remote fork.
Make sure you're in branch `master` and the run `git push`:

```
$ git checkout master
$ git push origin master
```

You can keep any branch up to date using this method. If you're working on a
feature branch (see next section), which we recommend, you would change the
command slightly, using the name of your `feature-branch` rather than `master`:

```
$ git checkout feature-branch
Switched to branch 'feature-branch'

$ git rebase upstream/master

$ git push origin feature-branch
```

### Work on a feature branch

One way to keep your work organized is to create a branch for each issue or
feature. Recall from [how Git is different][self-how-git-is-different] that
**Git is designed for lightweight branching and merging.** You can and should
create as many branches as you'd like.

First, make sure your master branch is up-to-date with Zulip upstream ([see
how][self-keep-up-to-date]).

Next, from your master branch, create a new tracking branch, providing a
descriptive name for your feature branch:

```
$ git checkout master
Switched to branch 'master'

$ git checkout -b issue-1755-fail2ban
Switched to a new branch 'issue-1755-fail2ban'
```

Alternatively, you can create a new branch explicitly based off
`upstream/master`:

```
$ git checkout -b issue-1755-fail2ban upstream/master
Switched to a new branch 'issue-1755-fail2ban'
```

Now you're ready to work on the issue or feature.

### Stage changes

Recall that files tracked with Git have possible three states:
committed, modified, and staged.

To prepare a commit, first add the files with changes that you want
to include in your commit to your staging area. You *add* both new files and
existing ones. You can also remove files from staging when necessary.

#### Get status of working directory

To see what files in the working directory have changes that have not been
staged, use `git status`.

If you have no changes in the working directory, you'll see something like
this:

```
$ git status
On branch issue-123
nothing to commit, working directory clean
```

If you have unstaged changes, you'll see something like this:

```
On branch issue-123
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        newfile.py

nothing added to commit but untracked files present (use "git add" to track)
```

#### Stage additions with git add

To add changes to your staging area, use `git add <filename>`. Because `git
add` is all about staging the changes you want to commit, you use it to add
*new files* as well as *files with changes* to your staging area.

Continuing our example from above, after we run `git add newfile.py`, we'll see
the following from `git status`:

```
On branch issue-123
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   newfile.py
```

You can view the changes in files you have staged with `git diff --cached`. To
view changes to files you haven't yet staged, just use `git diff`.

If you want to add all changes in the working directory, use `git add -A`
([documentation][gitbook-add]).


You can also stage changes using your graphical Git client.

If you stage a file, you can undo it with `git reset HEAD <filename>`. Here's
an example where we stage a file `test3.txt` and then unstage it:

```
$ git add test3.txt
On branch issue-1234
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   test3.txt

$ git reset HEAD test3.txt
$ git status
On branch issue-1234
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        test3.txt

nothing added to commit but untracked files present (use "git add" to track)
```

#### Stage deletions with git rm

To remove existing files from your repository, use `git rm`
([documentation][gitbook-rm]). This command can either stage the file for
removal from your repository AND delete it from your working directory or just
stage the file for deletion and leave it in your working directory.

To stage a file for deletion and **remove** it from your working directory, use
`git rm <filename>`:

```
$ git rm test.txt
rm 'test.txt'

$ git status
On branch issue-1234
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    test.txt

$ ls test.txt
ls: No such file or directory
```

To stage a file for deletion and **keep** it in your working directory, use
`git rm --cached <filename>`:

```
$ git rm --cached test2.txt
rm 'test2.txt'

$ git status
On branch issue-1234
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    test2.txt

$ ls test2.txt
test2.txt
```

If you stage a file for deletion with the `--cached` option, and haven't yet
run `git commit`, you can undo it with `git reset HEAD <filename>`:

```
$ git reset HEAD test2.txt
```

Unfortunately, you can't restore a file deleted with `git rm` if you didn't use
the `--cache` option. However, `git rm` only deletes files it knows about.
Files you have never added to git won't be deleted.

### Commit changes

When you've staged all your changes, you're ready to commit. You can do this
with `git commit -m "My commit message."` to include a commit message.

Here's an example of committing with the `-m` for a one-line commit message:

```
$ git commit -m "Add a test commit for docs."
[issue-123 173e17a] Add a test commit for docs.
 1 file changed, 1 insertion(+)
 create mode 100644 newfile.py
```

You can also use `git commit` without the `-m` option and your editor to open,
allowing you to easily draft a multi-line commit message.

How long your commit message should be depends on where you are in your work.
Using short, one-line messages for commits related to in-progress work makes
sense. For a commit that you intend to be final or that encompasses a
significant amount or complex work, you should include a longer message.

Keep in mind that your commit should contain a 'minimal coherent idea' and have
a quality commit message. See Zulip docs [Commit
Discipline][zulip-rtd-commit-discipline] and [Commit
messages][zulip-rtd-commit-messages] for details.

Here's an example of a longer commit message that will be used for a pull request:

```
Integrate Fail2Ban.

Updates Zulip logging to put an unambiguous entry into the logs such
that fail2ban can be configured to look for these entries.

Tested on my local Ubuntu development server, but would appreciate
someone testing on a production install with more users.

Fixes #1755.
```

The first line is the summary. It's a complete sentence, ending in a period. It
uses a present-tense action verb, "Integrate", rather than "Integrates" or
"Integrating".

The following paragraphs are full prose and explain why and how the change was
made. It explains what testing was done and asks specifically for further
testing in a more production-like environment.

The final paragraph indicates that this commit addresses and fixes issue #1755.
When you submit your pull request, GitHub will detect and link this reference
to the appropriate issue. Once your commit is merged into zulip/master, GitHub
will automatically close the referenced issue. See [Closing issues via commit
messages][github-help-closing-issues] for details.

Make as many commits as you need to to address the issue or implement your feature.

### Push your commits to GitHub

As you're working, it's a good idea to frequently push your changes to GitHub.
This ensures your work is backed up should something happen to your local
machine and allows others to follow your progress. It also allows you to
[work from multiple computers][self-multiple-computers] without losing work.

Pushing to a feature branch is just like pushing to master:

```
$ git push origin <branch-name>
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 658 bytes | 0 bytes/s, done.
Total 6 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local objects.
To git@github.com:christi3k/zulip.git
 * [new branch]      issue-demo -> issue-demo
```

If you want to see what git will do without actually performing the push, add
the `-n` (dry-run) option: `git push -n origin <branch-name>`. If everything
looks good, re-run the push command without `-n`.

If the feature branch does not already exist on GitHub, it will be created when
you push and you'll see `* [new branch]` in the command output.

### Examine and tidy your commit history

Examining your commit history prior to submitting your pull request is a good
idea. Is it tidy such that each commit represents a minimally coherent idea
(see [commit discipline][zulip-rtd-commit-discipline])? Do your commit messages
follow [Zulip's style][zulip-rtd-commit-messages]? Will the person reviewing
your commit history be able to clearly understand your progression of work?

On the command line, you can use the `git log` command to display an easy to
read list of your commits:

```
$ git log --all --graph --oneline --decorate

* 4f8d75d (HEAD -> 1754-docs-add-git-workflow) docs: Add details about configuring Travis CI.
* bfb2433 (origin/1754-docs-add-git-workflow) docs: Add section for keeping fork up-to-date to Git Guide.
* 4fe10f8 docs: Add sections for creating and configuring fork to Git Guide.
* 985116b docs: Add graphic client recs to Git Guide.
* 3c40103 docs: Add stubs for remaining Git Guide sections.
* fc2c01e docs: Add git guide quickstart.
| * f0eaee6 (upstream/master) bug: Fix traceback in get_missed_message_token_from_address().
```

Alternatively, use your graphical client to view the history for your feature branch.

If you need to update any of your commits, you can do so with an interactive
[rebase][github-help-rebase]. Common reasons to use an interactive rebase
include:

- squashing several commits into fewer commits
- splitting a single commit into two or more
- rewriting one or more commit messages

There is ample documentation on how to rebase, so we won't go into details
here. We recommend starting with GitHub's help article on
[rebasing][github-help-rebase] and then consulting Git's documentation for
[git-rebase][gitbook-git-rebase] if you need more details.

If all you need to do is edit the commit message for your last commit, you can
do that with `git commit --amend`. See [Git Basics - Undoing
Things][gitbook-basics-undoing] for details on this and other useful commands.

### Force-push changes to GitHub after you've altered your history

Any time you alter history for commits you have already pushed to GitHub,
you'll need to prefix the name of your branch with a `+`. Without this, your
updates will be rejected with a message such as:

```
$ git push origin 1754-docs-add-git-workflow
To git@github.com:christi3k/zulip.git
 ! [rejected] 1754-docs-add-git-workflow -> 1754-docs-add-git-workflow (non-fast-forward)
error: failed to push some refs to 'git@github.com:christi3k/zulip.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

Re-running the command with `+<branch>` allows the push to continue by
re-writing the history for the remote repository:

```
$ git push origin +1754-docs-add-git-workflow
Counting objects: 12, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 3.71 KiB | 0 bytes/s, done.
Total 12 (delta 8), reused 0 (delta 0)
remote: Resolving deltas: 100% (8/8), completed with 2 local objects.
To git@github.com:christi3k/zulip.git
 + 2d49e2d...bfb2433 1754-docs-add-git-workflow -> 1754-docs-add-git-workflow (forced update)

```

This is perfectly okay to do on your own feature branches, especially if you're
the only one making changes to the branch. If others are working along with
you, they might run into complications when they retrieve your changes because
anyone who has based their changes off a branch you rebase will have to do a
complicated rebase.

## Create a pull request

When you're ready for feedback, submit a pull request. Pull requests
are a feature specific to GitHub. They provide a simple, web-based way
to submit your work (often called "patches") to a project. It's called
a *pull request* because you're asking the project to *pull changes*
from your fork.

If you're unfamiliar with how to create a pull request, you can check
out GitHub's documentation on
[creating a pull request from a fork][github-help-create-pr-fork]. You
might also find GitHub's article
[about pull requests][github-help-about-pr] helpful. That all said,
the tutorial below will walk you through the process.

### Work in progress pull requests

In the Zulip project, we encourage submitting work-in-progress pull
requests early and often. This allows you to share your code to make
it easier to get feedback and help with your changes. Prefix the
titles of work-in-progress pull requests with **[WIP]**, which in our
project means that you don't think your pull request is ready to be
merged (e.g. it might not work or pass tests).  This sets expectations
correctly for any feedback from other developers, and prevents your
work from being merged before you're confident in it.

### Step 1: Update your branch with git rebase

The best way to update your branch is with `git fetch` and `git rebase`. Do not
use `git pull` or `git merge` as this will create merge commits. See [keep your
fork up to date][self-keep-up-to-date] for details.

Here's an example (you would replace *issue-123* with the name of your feature branch):

```
$ git checkout issue123
Switched to branch 'issue-123'

$ git fetch upstream
remote: Counting objects: 69, done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 69 (delta 49), reused 39 (delta 39), pack-reused 7
Unpacking objects: 100% (69/69), done.
From https://github.com/zulip/zulip
   69fa600..43e21f6  master     -> upstream/master

$ git rebase upstream/master

First, rewinding head to replay your work on top of it...
Applying: troubleshooting tip about provisioning
```

### Step 2: Push your updated branch to your remote fork

Once you've updated your local feature branch, push the changes to GitHub:

```
$ git push origin issue-123
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 658 bytes | 0 bytes/s, done.
Total 6 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local objects.
To git@github.com:christi3k/zulip.git
 + 2d49e2d...bfb2433 issue-123 -> issue-123
```

If your push is rejected with error **failed to push some refs** then you need
to prefix the name of your branch with a `+`:

```
$ git push origin +issue-123
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 658 bytes | 0 bytes/s, done.
Total 6 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local objects.
To git@github.com:christi3k/zulip.git
 + 2d49e2d...bfb2433 issue-123 -> issue-123 (forced update)
```

### Step 3: Open the pull request

If you've never created a pull request or need a refresher, take a look at
GitHub's article [creating a pull request from a
fork][github-help-create-pr-fork]. We'll briefly review the process here.

The first step in creating a pull request is to use your web browser to
navigate to your fork of Zulip. Sign in to GitHub if you haven't already.

Next, navigate to the branch you've been working on. Do this by clicking on the
**Branch** button and selecting the relevant branch. Finally, click the **New
pull request** button.

Alternatively, if you've recently pushed to your fork, you will see a green
**Compare & pull request** button.

You'll see the *Open a pull request* page:

![images-create-pr]

Provide a **title** and first comment for your pull request. Remember to prefix
your pull request title with [WIP] if it is a [work-in-progress][wip-prs].

If your pull request has an effect on the visuals of a component, you might want
to include a screenshot of this change or a GIF of the interaction in your first
comment. This will allow reviewers to comment on your changes without having to
checkout your branch; you can find a list of tools you can use for this over
[here][screenshots-gifs].

When ready, click the green **Create pull request** to submit the pull request.

Note: **Pull request titles are different from commit messages.** Commit
messages can be edited with `git commit --amend`, `git rebase -i`, etc., while
the title of a pull request can only be edited via GitHub.

## Update a pull request

As you get make progress on your feature or bugfix, your pull request, once
submitted, will be updated each time you [push commits][self-push-commits] to
your remote branch. This means you can keep your pull request open as long as
you need, rather than closing and opening new ones for the same feature or
bugfix.

It's a good idea to keep your pull request mergeable with upstream by frequently
fetching, rebasing, and pushing changes. See [keep your fork up to
date][self-keep-up-to-date] for details. You might also find this excellent article
[How to Rebase a Pull Request][edx-howto-rebase-pr] helpful.

And, as you address review comments others have made, we recommend posting a
follow-up comment in which you: a) ask for any clarifications you need, b)
explain to the reviewer how you solved any problems they mentioned, and c) ask
for another review.

## Review changes

### Changes on (local) working tree

Display changes between index and working tree (what is not yet staged for commit):

```
$ git diff
```

Display changes between index and last commit (what you have staged for commit):

```
$ git diff --cached
```

Display changes in working tree since last commit (changes that are staged as
well as ones that are not):

```
$ git diff HEAD
```

### Changes within branches

Use any git-ref to compare changes between two commits on the current branch.

Display changes between commit before last and last commit:

```
$ git diff HEAD^ HEAD
```

Display changes between two commits using their hashes:

```
$ git diff e2f404c 7977169
```

### Changes between branches

Display changes between tip of topic branch and tip of master branch:

```
$ git diff topic master
```

Display changes that have occurred on master branch since topic branch was created:

```
$ git diff topic...master
```

Display changes you've committed so far since creating a branch from upstream/master:

```
$ git diff upstream/master...HEAD
```

## Get and stay out of trouble

Git is a powerful yet complex version control system. Even for contributors
experienced at using version control, it can be confusing. The good news is
that nearly all Git actions add information to the Git database, rather than
removing it. As such, it's hard to make Git perform actions that you can't
undo. However, git can't undo what it doesn't know about, so it's a good
practice to frequently commit your changes and frequently push your commits to
your remote repository.

[gitbook-rebase]: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
[gitbook-git-rebase]: https://git-scm.com/docs/git-rebase
[gitbook-git-branch]: https://git-scm.com/docs/git-branch
[gitbook-git-status]: https://git-scm.com/docs/git-status
[gitbook-guis]: https://git-scm.com/downloads/guis
[gitbook-fetch]: https://git-scm.com/docs/git-fetch
[gitbook-git-pull]: https://git-scm.com/docs/git-pull
[gitbook-basics-undoing]: https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things
[gitbook-install]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[gitbook-setup]: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
[gitbook-other-envs-bash]: https://git-scm.com/book/en/v2/Git-in-Other-Environments-Git-in-Bash
[gitbook-other-envs-zsh]: https://git-scm.com/book/en/v2/Git-in-Other-Environments-Git-in-Zsh
[gitbook-aliases]: https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases
[gitbook-add]: https://git-scm.com/docs/git-add
[gitbook-reset]: https://git-scm.com/docs/git-reset
[gitbook-rm]: https://git-scm.com/docs/git-rm
[gitbook-three-states]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics#The-Three-States
[gitbook-basic-merge-conflicts]: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#Basic-Merge-Conflicts
[gitbook-advanced-merging]: https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_advanced_merging
[gitbook-basics]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
[gitbook-git-cherry-pick]: https://git-scm.com/docs/git-cherry-pick
[gitbook-config]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
[github-rebase-pr]: https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request
[github-zulip]: https://github.com/zulip/
[github-join]: https://github.com/join
[github-help-fork]: https://help.github.com/articles/fork-a-repo/
[github-help-conf-remote]: https://help.github.com/articles/configuring-a-remote-for-a-fork/
[github-help-sync-fork]: https://help.github.com/articles/syncing-a-fork/
[github-help-push]: https://help.github.com/articles/pushing-to-a-remote/
[github-help-rebase]: https://help.github.com/articles/using-git-rebase/
[github-help-amend]: https://help.github.com/articles/changing-a-commit-message/
[github-help-about-pr]: https://help.github.com/articles/about-pull-requests/
[github-help-create-pr]: https://help.github.com/articles/creating-a-pull-request/
[github-help-create-pr-fork]: https://help.github.com/articles/creating-a-pull-request-from-a-fork/
[github-help-resolve-merge-conflict]: https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/
[github-help-closing-issues]: https://help.github.com/articles/closing-issues-via-commit-messages/
[zulip-rtd-git-guide]: http://zulip.readthedocs.io/en/latest/git-guide.html
[zulip-rtd-commit-messages]: version-control.html#commit-messages
[zulip-rtd-commit-discipline]: version-control.html#commit-discipline
[zulip-rtd-lint-tools]: code-style.html#lint-tools
[zulip-rtd-testing]: testing.html
[zulip-rtd-mypy]: mypy.html
[zulip-rtd-code-style]: code-style.html
[zulip-rtd-zulipbot-usage]: zulipbot-usage.html
[gitgui-tower]: https://www.git-tower.com/
[git-bash-admin]: dev-env-first-time-contributors.html#running-git-bash-as-an-administrator
[gitgui-fork]: https://git-fork.com/
[gitgui-gitxdev]: https://rowanj.github.io/gitx/
[gitgui-ghdesktop]: https://desktop.github.com/
[gitgui-sourcetree]: https://www.sourcetreeapp.com/
[gitgui-gitcola]: http://git-cola.github.io/
[gitgui-gitg]: https://wiki.gnome.org/Apps/Gitg
[gitgui-rabbit]: http://rabbitvcs.org/
[gitgui-giggle]: https://wiki.gnome.org/Apps/giggle
[gitgui-gitextensions]: https://gitextensions.github.io/
[gitgui-gitk]: https://git-scm.com/docs/gitk
[travis-ci]: https://travis-ci.org/
[screenshots-gifs]: screenshot-and-gif-software.html
[self-setup]: git-guide.html#setup-git
[self-how-git-is-different]: git-guide.html#how-git-is-different
[self-git-terms]: git-guide.html#important-git-terms
[self-get-zulip-code]: git-guide.html#get-zulip-code
[self-use-git]: git-guide.html#using-git-as-you-work
[self-create-pr]: git-guide.html#create-a-pull-request
[self-update-pr]: git-guide.html#update-a-pull-request
[self-review-changes]: git-guide.html#review-changes
[self-clone-to-your-machine]: git-guide.html#step-1b-clone-to-your-machine
[self-connect-upstream]: git-guide.html#step-1c-connect-your-fork-to-zulip-upstream
[self-keep-up-to-date]: git-guide.html#keep-your-fork-up-to-date
[self-push-commits]: git-guide.html#push-your-commits-to-github
[images-gui-stage]: _images/zulip-gui-stage.gif
[images-gui-hist]: _images/zulip-gui-hist-tower.png
[images-create-pr]: images/zulip-open-pr.png
[understanding-git]: http://web.mit.edu/nelhage/Public/git-slides-2009.pdf
[edx-howto-rebase-pr]: https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request
[tig]: http://jonas.nitro.dk/tig/
[wip-prs]: #work-in-progress-pull-requests
