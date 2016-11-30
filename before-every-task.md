# Commands to run before starting every task

Before beginning each and every GCI task, you should do the following:

**1. Fetch new commits from [zulip/zulip] (upstream):**

```
$ git fetch upstream
```

**2. Apply these new commits to your local `master` branch:**

```
$ git checkout master
$ git rebase upstream/master
```

**3. Create a new feature branch for your task:**

```
$ git checkout -b task-<task-name> upstream/master
```

(Replace `<task-name>` with text describing which task you are are about to
start. Use hyphens `-` to separate words instead of spaces.)
