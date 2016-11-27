# Comparison with other chat tools

Help us prepare the comparison page between Zulip and other chat tools,
with a matrix of which features each product has or doesn't have. There
are 5 sets of tasks in this section. The first 3 types involves testing
whether a given set of features is present in a chat application. The last 2
sets contains open ended questions. You have to work on 
only one chat application for testing the features. Visit GCI website to 
find out the chat application that you should be testing.

# Set A

Check whether the following features are present in the **chat application** 
that is described in the task description in GCI website :tada:.

:bangbang: Make sure that you follow the same output format 
as [described here](#output-format).

## Features to Test

- Is this the first time you are using this chat application?
- Private Channels: Does the chat application support private channels?
- Direct Messaging: Does the chat application allow users to message
each other privately outside of channels?
- Group chat: Can users create group conversations in which they can
chat privately outside of channel?
- Audio call: Does the chat application supports audio call with other
users?
- Video chat:  Does the chat application support video call with other
users?
- Full-text Search Chat history.  Can the users search the chat history?
- File sharing: Can users share files with other users?
- File upload size limit: What is the size of the biggest file a user
can share?
- Total shared file size limit: What is the storage limit of all the
shared files?
- Drag-and-drop file uploads: Does the product support uploading files
via dragging them?  
- Emoji: Can users include emoticons in chat messages?
- Choose emoji set: Can users change the set of default emojis by
choosing another set of emojis?
- Create custom emoticons: If the emoji user is not looking for is
not present can he/she create a custom emoji?
- Screen Sharing: Can users share the screen with other users?
- GIF Support: Does the chat application play the GIFs send by the users?
- Share Code Snippets: Does the chat application allow users to quickly
create code snippets and share it other users?
- Desktop Application: Does that chat application have a desktop
Application? Mention the operating systems in which it is available.
- Mobile App: Does that chat application have a mobile app? Mention the
operating systems in which it is available.
- Apple Watch App: Does that chat application have an Apple Watch app?
- Themes: Can the users or admins change how the application look like
using themes?
- Custom Themes: Can users or admins create custom themes? 
- RSS feeds: Can the chat application bring the posts from blog or news
site to the users via RSS? 
- Online Demo: Can the users try the application without installing or
creating a new organization?
- Preview Links: Does the chat application preview the links send by
the users in messages?
- Preview docs and PDFs: Can the chat application preview the documents
so that users don’t have to download them for viewing the content?
- Preview Images: Does the chat application preview the images send in
the chat?

## Output Format

The output should be submitted as a spreadsheet with the following column names 
 * **Feature** - The feature you are testing. Eg Private Channels
 * **Yes/No/Not Sure** - Whether the feature is present in the chat application.
 * **Additional Information** - Additional information regarding the feature if 
 required.
 * **Documentation** - Link to the documentation if available.
 * **Screenshots** - Take the screenshots of the feature while you are testing them.
Put the spreadsheat and screenshots into a new directory gci/user-doc

[Here is an example](https://docs.google.com/spreadsheets/d/16a46fPeEd-PnqS5ZBpspTScnjIaXwr60xFVEdcwKiTY/edit?usp=sharing) of how the spreadsheet would look like while testing Slack.

# Set B

Check whether the following features are present in the **chat application** 
that is described in the task description in GCI website :tada:. 

:bangbang: Make sure that you follow the [same output format](#output-format) 
as described in task A.

- Is this the first time you are using this chat application? 
- Open Source: Is the chat application open source?
- Multi Tenancy: If open source can multiple organizations be hosted in a 
single server?
- Subdomain: Does each organization have a subdomain of it’s own? eg: 
team-subdomain.example.com
- LDAP/AD: Can users sign in to the chat application using LDAP/AD 
credentials? 
- Migration support: Does the chat application have features to ease the 
migration from other chat applications? If yes specify the chat applications
and features.
- @user mentions: Can a user be notified in the chat?
- @here mentions: Can all users currently active in channel be notified?
- @channel mentions: Can all the members of a channel be notified?
- @all mentions: Can everyone in the organization be notified?
- Edit sent messages: Can the messages which are already send be edited?
Is there a time period within which editing is allowed? eg. Users cannot
edit messages after X minutes have passed.
- Delete sent messages: Can the messages which are already send be deleted?
Is there a time period within which deletion is allowed? eg. Users cannot
delete messages after X minutes have passed.
- Message Pinning: Does the chat application support message pinning? 
The pinned messages would be visible to everyone in the channel.
- Off-the-Record Messaging: Messages send in this mode won’t be stored in 
the server. Only the receiver is expected to get the message. Does the 
chat application support this?
- Message starring: Does the chat application allow users to star or favorite
messages?
- Channel starring: Can the users star a channel? 
- Desktop Notifications: Does the chat application supports desktop notifications?
- Desktop Notification duration:  Can the duration of the desktop notification
be configured?
- Mobile App - Push notifications: Does the mobile app supports push notifications?
- Mobile App - Icon notifications: Does the mobile app supports icon notifications?
- Mobile App - Notification Light: Can the notification color of the app be changed 
via mobile App?
- Email notifications: Does the chat applications sends notification to users via 
email?
- Highlight word: Can users specify custom words which would be highlighted when 
appeared in the chat?
- DND mode: Is DND mode supported? Chat application does not send any notification
to the users when this mode is enabled. 
- Newsfeed: Does the chat application have any functionality similar to a newsfeed?
- Mute Channel: Can a channel be muted?
- Sign in to multiple organizations: If the user is member of more than one
organizations can he sign into all at the same time? How does the chat application 
handle that?
- 2FA - SMS: An SMS  with a single use authentication code would be send to the user 
when the user try to login to the account.
- 2FA - Authentication APP: Does the chat application support 2FA via Authentication
APP?
- Backup Codes: Can the user sign in to the application using backup codes?
- Single sign-on: Does the chat application support single sign on?

# Set C

Check whether the following features are present in the **chat application** 
that is described in the task description in GCI website :tada:.

:bangbang: Make sure that you follow the [same output format](#output-format)
as described in task A.

- Is this the first time you are using this chat application? 
- handles/username: Does users have handles or usernames? (Similar to Github
 handles)
- Change handle/username: Can the username/handle be changed?
- Status Message: Can users show custom status messages? 
- Sign out of all other sessions: Does the chat application allows users to 
log out of all the other sessions?
- Support Markdown: Does the chat application support message formatting 
using markdown?
- Unread message count: Does the chat application shows the count of messages
that are not read by the user?
- Message seen: Does the chat application show whether the message has been seen
by the receiver? 
- User is typing: Does the chat application notifies other users when a user is
typing?
- Message reactions: Can users react to a message using emoji? Similar to Github
comment reactions.
- Share message: Can a message be shared to other channels or users?
- User groups: Does the chat application support creating groups of team members?
User groups can be used to notify a set of people. It can be also used for adding
a set of people to a channel.
- Make public channel private: Can channels which were public at the time of 
creation be made private? 
- Make private channels public: Can channels which were private at the time of 
creation be made public? 
- Command support: Can users use commands to make chat application perform a 
particular action? eg sending /leave in channel would result in the user leaving
the channel.
- IRC: Can the users connect to the chat application using IRC?
- XMPP: Can the users connect to the chat application using XMPP?
- Integrations: Does the chat application supports integrations?
- Hubot support: Does the chat application has a hubot integration?
- hashtag: Does the chat application make use of hashtags. If yes how it is used?
- Auto highlight sent messages: Does the chat application highlight the messages 
sent by the user?
- Last seen online: Does the chat application shows when was a user last seen 
online? Can it be disabled?
- Buttons: Buttons are used by some chat applications to make chat conversations
more interactive. eg: An integration can send a poll to the channel with 2 different
buttons. The buttons can be clicked to vote in the poll. Does the chat application
supports buttons?
- user joined/user left: Does the chat application display user joined/user left
messages? Can it be configured by admin?
- reminder: Can users use chat application for setting reminders? The chat 
application would notify the user or channel at the time of the reminder.
- user documentation: Is there a documentation for users?
- Sign in using Link:  Does the chat application allow users to sign in using a 
one time use special link?

# Set D

Try to answer the following questions by playing with the chat application.

* Does the chat application have threaded conversations similar to Zulip.
If yes how is it implemented? Take screenshots.
* Compare the search functionality of Zulip with the chat application.
* Describe the pricing tier of the chat application.
* Who can create channels? How can admins restrict it? Take screesshots.
* What are the different type of roles for a user? (eg Admin, moderator,
user etc) Explain how the roles differ.
* Does the application have a user profile page or similar? What all details
are displayed? Take screesnshots.
* Do they have a guest mode, and if so, what do guests have access to?
* Public organization - Is there an option that allows users to join
the organization without invite? If yes how can they do that? Take screenshots.
* Can a user be member of multiple teams or organizations in the chat
application. If yes how how will the user login to a specific organization?
How can user identify which all teams he is a part of? Take screenshots.

## :bangbang: Output
The ouput can be submitted as a plain text file or markdown. It is okay if the 
writing isn't perfect, but it should include all the relevant content, including
screenshots and links pointing to documentations if appropriate.

# Set E

Try to answer the following questions by playing with the chat application.

- Does the chat application’s has it’s own bot?(Used for welcoming users,
answering queries etc). What else does it do? Take screenshots.
- Does the chat application support message formatting? If yes explain 
with screenshots.
- What options are available for hiding channel without leaving them? 
Take screenshots.
- Compare Zulip mobile app with the chat application mobile app. Take screenshots.
- Take a screenshot of every step of the on-boarding experience (for creating a 
new organization, and then for creating a user joining that organization). What 
did you like / not like about it?
- Play with the organization administrator settings and see what administration 
settings the chat application have have that Zulip doesn’t. Take screenshots.
- Which application was easier to use? What things that you really like about 
the user experience, features, etc they have that Zulip lacks, etc? Take Screenshots
- Compare the getting started tutorial with Zulip’s. Which one was more user 
friendly and informative? Take screenshots.

## :bangbang: Output
The ouput can be submitted as a plain text file or markdown. It is okay if the 
writing isn't perfect, but it should include all the relevant content, including
screenshots and links pointing to documentations if appropriate.