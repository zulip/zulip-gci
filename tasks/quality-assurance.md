# GCI Tasks: Quality Assurance

## Prerequisites

* SET_UP_ZULIP_DEVELOPMENT_ENVIRONMENT

## Background

Find bugs in Zulip! The hardest part of shipping bug-free code is finding
them before users do, which is where this task comes in.

## Task descriptions

All of these can be done in the development environment.

### Task Type A: Internationalization overflow

Words and phrases have different lengths in different languages. German
translations are among the longest. Click around the UI in German
(chat.zulip.org/de/), while resizing the window to various sizes, and see if
you can get any of the text to overflow the box that it is in.

### Task Type B: Real time sync

Open up two browser tabs, one with an incognito window, and log in to the
development environments with two different users. Do a bunch of stuff in one
window, and try to get the other window to not be in sync with the first one.

### Task Type C: Open graph

Zulip has this cool “open graph” integration, where when you post a link
into Zulip, it provides a nice visual preview of the webpage. Post links to
a bunch of web pages (homepages of websites, blogs, etc.). Find at least
one URL for a website where the preview doesn’t look good, fails to show up,
or is broken.

### Task Type D: Frontend bug

Find any sequence of actions that results in something displaying the wrong
output.

## Submission instructions

Post the bug to the 'quality assurance' topic of the 'GCI task discussion'
stream on chat.zulip.org, and a mentor will check off on whether it is a
known bug or not. If it is indeed new, submit a pull request to the
zulip/gci-submissions repository, with
* A title that starts with "Quality Assurance".
* A screenshot of the broken behavior.
* Step by step instructions for getting to that broken state. E.g. "log in
  as othello, then click on the settings gear icon, then ..."

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
