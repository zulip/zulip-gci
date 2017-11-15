# ReviewBot Integration
The ReviewBot integration is designed to keep track of reviews on an iOS
app, an Android app, a Yelp website, or a iTunes podcast. It notifies you on
Slack or through several other services. You can set parameters for which
reviews you receive notifications, for example to only get notifications
for 5 star reviews. This is the official website for the integration:
<https://reviewbot.io/>

## Problems

There was no available documentation. As a result, I could not
figure out how to add a webhook URL. My guess is that ReveiwBot was built
to support specific services (such as Slack or Twitter), without a way to
implement a webhook. I contacted the ReviewBot team, to see if they could
provide any additional information. They responded and said that it was not
currently possible to add a webook, but they could add a general webhook
option, which would make a ReviewBot integration possible. Unfortunately,
they said said that they could not add this for at least a month. That
means that for the Google Code-in 2016-2017, it will not be possible to
build a ReviewBot integration. However, eventually a ReviewBot
integration could be added to Zulip.
