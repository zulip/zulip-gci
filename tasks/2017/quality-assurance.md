# GCI Tasks: Quality Assurance

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

## Background

Find bugs in Zulip! The hardest part of shipping bug-free code is finding
them before users do, which is where this task comes in.

### Useful resources

A helpful guide to doing manual testing in Zulip is here:
https://zulip.readthedocs.io/en/latest/testing/manual-testing.html

(Pull requests to update that guide are appreciated!)

This guide on writing bugs good reports may also be helpful if you're
not familiar with writing bug reports (though reading a few bug
reports in our issue tracker is probably equally helpful):
http://zulip.readthedocs.io/en/latest/contributing/bug-reports.html

## Task description

All of these can be done in the Zulip development environment, and
many of them can be done directly on chat.zulip.org.

Any bug that you find in Zulip is fair game for this task.  Here, we
recommend a few types of bugs that tend to be common and thus might be
particularly easy to find.

### Internationalization overflow

First, read about
[internationalization in Zulip](https://zulip.readthedocs.io/en/latest/translating/translating.html).

Words and phrases have different lengths in different
languages. German translations are among the longest. Click around the
UI in German (https://chat.zulip.org/de/), while resizing the window
to various sizes, and see if you can get any of the text to overflow
the box that it is in.

(You can also get the UI in any language by selecting that language in
[the app's settings](https://chat.zulip.org/help/change-your-language)).

### Missing internationalization tags

Pick one of the languages that should be nearly 100% translated, and
browse through the Zulip logged-in UI in that language looking for
strings that are not translated.  After finding some, verify that the
problem is a string that isn't properly tagged for translation (for
new strings, it's possible that our translators haven't translated
them yet).  (Note that the landing pages, like /features/, are
intentionally not translated).

### Browser real-time sync

Open up two browser tabs, one with an incognito window, and log in to the
development environments with two different users. Do a bunch of stuff in one
window, and try to get the other window to not be in sync with the first one.

### Frontend UI bugs

Zulip has a lot of UI surface area, especially in places like the
settings.  Find any sequence of actions that results in something
displaying the wrong output.  Try to click on things that aren't the
most natural next thing to click.

### Mobile app bugs

Zulip's mobile apps are relatively new, and thus are likely to have
more bugs than the rest of the product.

Download the Zulip Mobile app from the
[Google Play Store](https://play.google.com/store/apps/details?id=com.zulipmobile)
or
[Apple App Store](https://itunes.apple.com/us/app/zulip/id1203036395),
and find a new bug in it.

Play around with the UI, trying to get the mobile version to crash,
render something wrong, or show data inconsistent with what you see in
the webapp.  Testing with both phones and tablet is encouraged!

## Submission instructions

You can check whether the bug is already known by looking at the open
bug lists for the varous projects:
[server/web](https://github.com/zulip/zulip/issues?q=is%3Aissue+is%3Aopen+label%3Abug),
[Python API](https://github.com/zulip/python-zulip-api/issues?q=is%3Aissue+is%3Aopen+label%3Abug),
and
[mobile](https://github.com/zulip/zulip-mobile/issues?q=is%3Aissue+is%3Aopen+label%3Abug).
If you believe your bug is new, post the bug to the 'quality
assurance' topic of the
[GCI tasks stream](https://chat.zulip.org/#narrow/stream/GCI.20tasks)
on chat.zulip.org, and a mentor will verify whether it is indeed a new
bug.

If it is indeed new, open a new GitHub issue the
[zulip/zulip](https://github.com/zulip/zulip) repository or
[zulip/zulip-mobile](https://github.com/zulip/zulip-mobile) repository
(as appropriate), with:

* A [screenshot or video](http://zulip.readthedocs.io/en/latest/tutorials/screenshot-and-gif-software.html))
  demonstrating the buggy behavior.
* Step by step instructions for getting to that broken state. E.g. "log in
  as othello, then click on the settings gear icon, then ..."

Mentors will accept your task once you've submitted a clear bug report
that they are able to reproduce.

If you're interested in fixing the bug you found, you can work on it
[via the issues task](https://github.com/zulip/zulip-gci/blob/master/tasks/2017/issues.md).

If you're not sure how to take screenshots, [this guide](http://zulip.readthedocs.io/en/latest/tutorials/screenshot-and-gif-software.html)
should be helpful.

## General notes

* We have made multiple copies of this task available.  A cluster of
  related problems in Zulip is usually considered one bug (e.g. if
  there's an HTML template file with 5 strings missing translation
  tags, that's one issue, not 5).

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
