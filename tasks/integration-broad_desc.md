#GCI Tasks: Incoming Webhook Integrations

A Zulip integration is a special type of bot that brings information from the outside world into Zulip. Zulip integration allows teams to stay up-to-date on code changes, issue tickets, build system results, tweets, and more. Zulip currently has over 50 integrations (example: Twitter , GitHub). It would be fun to add more as there are at least 50 more remaining to be written.

The instructions given below will guide you how to play around with some cool integrations. The tasks below center around adding the HelloSign integration (a tool for collecting signatures online). Feel free to choose any integration that you find particularly interesting (scroll down to find a list of possible new integrations). The tasks given below must be done in the same order.

**TASK 0**

- **Instructions**:
1. Follow the incoming webhook integration tutorial [TODO]// add link // to create a duplicate of our HelloWorld webhook integration that is named after yourself, and sends a unique message you’d like to share with the world.
2. As you’re going through the tutorial, take notes on where you got stuck or needed to look up terminology. 
3. Submit your notes on where you got stuck or were confused as well as a link to your cool new integration!
- **Type**: Quality assurance, Coding
- **Level**: Beginner

**TASK 1** 

- **Instructions**:
1. Create a test team with[ Slack](https://slack.com/), and a test account at the integration site (e.g, hellosign.com). Add this integration to your Slack account, and play around with it to figure out what information is getting posted.
2. Take screenshots of all the different types of messages you can generate, and make a brief note about any messages you think are possible, but which you are unable to generate (e.g. because they are only available to paying HelloSign customers). Place the screenshots and notes in a new GitHub issue at https://github.com/zulip/zulip-gci/issues/new.
3. Use[ ](http://requestb.in/)[RequestBin](http://requestb.in/) or a similar site to capture example webhook payloads (i.e. the actual data that the webhook posts to the provided URL) for all the message types above.
4. Put the webhook payloads generated for your integration in files having some illustrative names under `zerver/fixtures/hellosign/`  (replace `hellosign` with your integration’s name).
5. Open a pull request to add files to the zulip-gci project.
- **Type**: Outreach/Research
- **Level**: Beginner

**TASK 2**

- **Instructions**:
1. Install the [Zulip development environment](http://zulip.readthedocs.io/en/latest/dev-overview.html) in case you haven’t. 
2. Write webhook handlers and tests for the webhook payloads captured in Task 1, following the guide at http://zulip.readthedocs.io/en/latest/integration-guide.html#webhook-integrations. Since Zulip has some features (e.g topics) that Slack doesn’t have, the formatting shouldn’t look exactly like it does in Slack, but it should clearly describe all the relevant information that is present in the Slack notification. You are advised not to use abbreviations and follow professional language throughout.
- **Type**: Coding
- **Level**: Intermediate [??] 

**TASK 3**

- **Instructions**: 
1. Install the [Zulip development environment](http://zulip.readthedocs.io/en/latest/dev-overview.html) in case you haven’t.
2. Write documentation explaining how to enable your new integration in Zulip, following the instructions [here](http://zulip.readthedocs.io/en/latest/integration-guide.html#documenting-your-integration). 
- **Type**: Documentation
- **Level**: Intermediate [??]

##POSSIBLE NEW INTEGRATIONS

Here is the list of some popular webhooks:

- AppFollow: Monitors appstore activity.
- Mention: Media monitoring tool.
- GoSquared: Real time analytics.
- Mailchimp: Email marketing.
- InVision: Collaborative prototyping app.
- Heroku: Cloud hosting and deployment.
- Stripe: Online payments.
- Papertrail: Log management.
- Zeplin: Design collaboration.

Want to explore more? You can check out hundreds of integrations available [here. ](http://www.slack.com/apps)Before deciding to work on any of these, please ensure that we intend to add your chosen integration to Zulip. You can then start working to add your favorite one.

[TODO] Update the list regularly as the contest goes on. 

##GENERAL NOTES


- Try to follow these tasks in proper order.
- Remember to change the integration’s name in the instructions above while working on the tasks for your own integration. 
- Express interest in one or more integrations either through GitHub comments or on the Zulip chat before taking it up just to ensure that no two participants work on the same task at a given time.
- The commit with the changes should have no other cleanup. If you end up making other code changes while doing this task, please put it in a separate commit.

##RESOURCES


- Webhook Integration Guide - [TODO] // Add link
- An **example** on how to add integrations - https://github.com/zulip/zulip/pull/324/files. 
- Git and GitHub Guide - http://zulip-ck.readthedocs.io/en/1754-docs-add-git-workflow/git-guide.html
- Documentation Guide - http://zulip.readthedocs.io/en/latest/integration-guide.html#documenting-your-integration. 

