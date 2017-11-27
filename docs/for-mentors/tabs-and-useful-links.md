# Tabs and Useful Links

In order to quickly set up for a mentor shift, using browser profiles might be
useful. This setup should work well both in Chrome and Firefox, as they both
support user profiles (though it’s easier to use in Chrome as it has a native UI
to switch between profiles).

During a mentor shift, you’ll need a few things:

* Zulip to monitor questions from students
* GCI app to monitor the task queue
* GitHub to monitor PR submissions by students
* Zulip development environment to fetch and test PRs you’re reviewing
* links to various helper docs, mainly but not limited to the `zulip-gci` repo,
  Zulip docs, and GCI website

## Browser setup

This setup allows you to quickly open all the tools you need for the mentor
shift by opening the browser profile and just as easily end your shift by
closing it.

1. Create a separate browser profile for GCI - you can easily do it in 
[Chrome](https://support.google.com/chrome/answer/2364824?co=GENIE.Platform%3DDesktop&hl=en) or
[Firefox](https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles)

2. Add pinned tabs
* https://chat.zulip.org
* https://codein.withgoogle.com/
* https://github.com/zulip/zulip-gci-submissions

3. Add a tab manager

[OneTab](https://www.one-tab.com/) works pretty well in both Chrome and Firefox
- it allows you to open tabs and save them in groups. You can name the groups
and then restore them, either in your current or separate browser window, and
then save them back with one click.

My preferred setup for OneTab is:

  a. When a tab group is restored, send the tabs to: A new window, unless OneTab is the only tab in the current window
  b. Pinned tabs: Don't send pinned tabs to OneTab
  c. Startup: Display OneTab whenever you start your web browser for the first time
  d. On clicking 'restore all' or restoring a single tab: Open the tab(s) and remove them from your OneTab list
  e. Duplicates: Allow duplicates

Useful OneTab groups for GCI:

* Mentor and contributor docs:
  * [How to mentor](how-to-mentor.md) 
  * [Shift spreadsheet](https://docs.google.com/spreadsheets/d/1ivw43Y6-dhitenj1aknc58J4HoskosMaqZYdo-VeSKg/edit#gid=0)
  * [Common student issues](common-issues.md)
  * [Code review](https://zulip.readthedocs.io/en/latest/contributing/code-reviewing.html)

* Student docs:
  * [Improving the GCI experience](../improving-gci-experience.md)
  * [GCI rules](https://developers.google.com/open-source/gci/resources/contest-rules)

* Zulip docs:
  * [Vagrant setup](https://zulip.readthedocs.io/en/latest/development/setup-vagrant.html#)
  * [Fixing commits](https://zulip.readthedocs.io/en/latest/tutorials/fixing-commits.html)
  * [Git cheat sheet](https://zulip.readthedocs.io/en/latest/tutorials/git-cheat-sheet-detailed.html)
  * [Zulip code style](https://zulip.readthedocs.io/en/latest/contributing/code-style.html)
  * [Version control](https://zulip.readthedocs.io/en/latest/contributing/version-control.html#)

It’s useful to add specific groups of links if you find you use them quite often 
- last year I had themed groups, e.g. for interactive bot tasks.


4. Add a distinct color theme to the browser profile, so you always know you
work in the context of GCI 

## Setup for saved drafts

You’ll find that students often ask the same questions, especially at the
beginning. We have an initial doc on the [common issues](common-issues.md), but 
as you mentor more,
you’ll probably have a lot of your own ideas. It’s useful to save them and reuse
later.

There is no good setup for saved drafts in Zulip yet, so make sure to add them
to (a) doc(s) you can reuse later, but you can use GitHub saved replies when
maintaining pull requests - https://github.com/settings/replies.

## Shell scripts and aliases

We have some useful [Zulip scripts](http://zulip.readthedocs.io/en/latest/contributing/git-guide.html#zulip-specific-tools) ready, during GCI especially `fetch a pull
request and rebase` comes in handy. Setting up some GCI specific aliases is also
useful if you review a lot of PRs.
