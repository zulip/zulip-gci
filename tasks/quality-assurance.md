# GCI Tasks: Quality Assurance

## Prerequisites

* A working Zulip development environment. See
  https://github.com/zulip/zulip-gci/blob/master/README.md for instructions
  on how to set one up.

## Background

Find bugs in Zulip! The hardest part of shipping bug-free code is finding
them before users do, which is where this task comes in.

## Task descriptions

All of these can be done in the development environment.  A helpful
guide to doing manual testing in Zulip is here:
http://zulip.readthedocs.io/en/latest/manual-testing.html

### Task Type A: Internationalization overflow

Words and phrases have different lengths in different languages. German
translations are among the longest. Click around the UI in German
(chat.zulip.org/de/), while resizing the window to various sizes, and see if
you can get any of the text to overflow the box that it is in.

### Task Type B: Real time sync

Open up two browser tabs, one with an incognito window, and log in to the
development environments with two different users. Do a bunch of stuff in one
window, and try to get the other window to not be in sync with the first one.

### Task Type C: Frontend bug

Find any sequence of actions that results in something displaying the wrong
output.  Try to click on things that aren't the most natural next
thing to click.

### Task Type D: Android bug

Download the Zulip Android app from the Google Play Store, and find a
new bug in it.

## Submission instructions

Post the bug to the 'quality assurance' topic of the 'GCI task
discussion' stream on chat.zulip.org, and a mentor will check off on
whether it is a known bug (in the GitHub issue tracker) or not. If it
is indeed new, open a new GitHub issue the zulip/zulip-gci repository
(aka this repository), with:

* A title that starts with "Quality Assurance".
* A screenshot of the broken behavior.
* Step by step instructions for getting to that broken state. E.g. "log in
  as othello, then click on the settings gear icon, then ..."

Mentors will accept your task once you've written up a clear bug
report that they are able to reproduce.

Mentors: Create a new GCI task or zulip/zulip GitHub issue for fixing
the bug after accepting the bug report.

## General notes

* If you find broken or even just unexpected behavior not in any of the
  categories above, feel free to post it anyway to the
  gci-tasks/quality-assurance topic. If it is not a known bug we'll still
  give you credit for the task!

* Two suggestions for how to go about this (but feel free to come up with
  your own strategy):
  * Pick a section of the site, and perform all the actions you can to all
    the elements in that section (click, type, etc), looking for anything
    unexpected.
  * Pick any of the Task Types and systematically look for bugs of that
    type.
