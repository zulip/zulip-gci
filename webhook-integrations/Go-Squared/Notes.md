I was told I could create a pull request describing my experience with Gosquared and trying to integrate it.

The Go Squared integration research task provides many difficulties that I think should be addressed. 
First, the suggested webhook inspector, RequestBin, does not work with Go Squared’s webhook interface, 
because Go Squared requires a https communication for it to function, which RequestBin does not use. 
So I had to use HookBin which was not mentioned in the guide. 
Also whenever I attempted to triggered a request to be sent to Slack only twice; Once saying it connect, 
the other time saying 0 users were online. 
Even when attempting to replicate my actions the I never received output on Slack again.
I also was never was able to receive a webhook request on HookBin. 
This task in my opinion needs to be reviewed to see if there are more errors than the ones I saw.

