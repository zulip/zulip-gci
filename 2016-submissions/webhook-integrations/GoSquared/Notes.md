I was told I could create a pull request describing my experience with GoSquared and trying to integrate it.

GoSquared is a website that has tools intended for business so they can grow their company, 
for instance GoSquared has website analytical tools for tracking and visualizing user’s interactions with a website. 
Slack is a chatroom (similar to Zulip), when integrated with GoSquared, 
is able to notify if certain triggers are met (for example a certain amount of users in the chat room). 
One of these ways it can notify, is via a webhook request sending JSON formatted data. 
For this task, the goal was to use GoSquared's Slack service to explore what webhook fixtures GoSquared could send. 
Then find what types of messages can be created. With the preceding tasks to be integrating GoSquared into Zulip.

The GoSquared integration research task provides many difficulties that I think should be addressed.

First, the suggested webhook inspector, RequestBin, does not work with Go Squared’s webhook interface, because GoSquared requires a https communication for it to function, which RequestBin does not use. I do want to note however GoSquared's documentation provides a guide (https://www.gosquared.com/customer/en/portal/articles/1996494-webhooks) to webhooks also suggesting RequestBin, but the documentaion also says the url has to be https. Even after following the documentation’s guide and trying different ways to trigger a payload to be sent, nothing was able to work. So I had to use HookBin which provides a https connection.
Also whenever I attempted to triggered a request to be sent to Slack only twice; Once saying it connected, the other time saying 0 users were online. Even when attempting to replicate my actions, I never received output on Slack again. I also was never was able to receive a webhook fixture on HookBin.

This task in my opinion needs to be reviewed to see if there are more errors than the ones I saw, or possibly be removed.




