# GCI Tasks: Comparison with Slack integrations

## Background

A Zulip integration is a special type of bot that brings information
from the outside world into Zulip. Zulip integrations allow teams to
stay up-to-date on code changes, issue tickets, build system results,
tweets, and more. Zulip currently has over 50 integrations, but there
are dozens more that would be valuabled to add.

To get an idea of the type of integrations out there, we've grabbed a
list of all the apps available for Slack, another chat tool. We'd like
some analysis of Slack's integrations with these apps, in particular
some information about how the integration works (is it a webhook, a
slash command, a command-line script or something else?) and whether
it's something that would be good to implement for Zulip.

We will use these to determine what the next 10-20 most useful
integrations to add to Zulip would be, and create GCI tasks for
implementing those, so this is a great task to work on if you'd like
more integrations tasks :).

You can read more about the different types of Slack integrations in
the [Slack API documentation](https://api.slack.com/).

## Task Description

Open up our
[Slack integrations analysis spreadsheet](https://docs.google.com/spreadsheets/d/1BGD9kszda3BWgvwE4TehcfvoMuMbqE5LbZiJ2AMDL74/edit#gid=0)
and find the row numbers indicated in your task description.

For each row, open up the URL in column C. Read over the integration
description and try to figure out the type of integration and record
that in column D. Add a brief description along with anything
interesting or unusual about the integration in column E.

If you have any questions ask on the "GCI tasks" stream (set the topic
to "Slack integration analysis").

When you have completed the task submit it for review. Each task
requires looking at 30 Slack integrations.

*Completion criteria:* Mentors will check that all of the rows have
 been completed, the data appears correct and is formatted correctly
 and consistent with the other rows in the documentation, and the
 notes would make sense to someone reading this in 3 months.
