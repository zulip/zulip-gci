# Zulip Google Code-In tasks repository

This repository contains items related to Zulip's participation in
Google Code-In that aren't part of an individual Zulip subproject
(e.g. the [Zulip server](https://github.com/zulip/zulip)).

At the moment, this includes:

* `tasks/`: Template descriptions for large categories of tasks.  We
  put the bulk of the descriptions in this repo rather than in the GCI
  interface so that it's possible to update the documentation on how
  to do things as we see what folks find confusing.
* `scripts/`: Tools for iterating over the tasks in a category and
  creating actual GCI tasks out of them.

For each major category of tasks, we'll want to have both a template
description under `tasks/` as well as a script under `scripts/` to
actually import the tasks into the GCI web application.  We'll run the
relevant scripts batches of tasks are ready to publish.

This repository will likely also be the home for GCI contributions
that don't yet have a clear place in another Zulip repository
(e.g. cute avatar images might just be stored in a directory here).
