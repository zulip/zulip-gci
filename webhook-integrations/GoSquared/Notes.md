I was told I could create a pull request describing my experience with GoSquared and trying to integrate it.

The GoSquared integration research task provides many difficulties that I think should be addressed.

For this task, the goal was to use GoSquared's Slack service to explore what webhook fixtures GoSquared could send. 
Then find what types of messages can be created. With the preceding tasks to be integrating GoSquared into Zulip.

First, the suggested webhook inspector, RequestBin, does not work with Go Squared’s webhook interface, 
because GoSquared requires a https communication for it to function, which RequestBin does not use. 
So I had to use HookBin which was not mentioned in the guide. 
Also whenever I attempted to triggered a request to be sent to Slack only twice; Once saying it connected, the other time saying 0 users were online. 
Even when attempting to replicate my actions, I never received output on Slack again. 
I also was never was able to receive a webhook fixture on HookBin.

This task in my opinion needs to be reviewed to see if there are more errors than the ones I saw, or possibly be removed.
