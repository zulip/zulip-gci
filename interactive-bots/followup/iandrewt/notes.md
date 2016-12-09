Andrew's Followup Bot Notes
===========================

 - I'm unsure as to whether the second message was supposed to have `@follow-up` changed to `from cordelia@zulip.com:`
 - The message did appear though so ¯\\_(ツ)_/¯
 - The followup bot code in `contrib_bots/lib/followup.py` works as follows
   - The message is checked to ensure that it's not following up a followup
   - The message is checked to see if it needs to be added to the followup stream (starts with `@followup` or `@follow-up`)
   - The message content is changed to replace the text `@followup` with `from <original sender>:`
   - The new message is sent as a stream message to the followup stream with the subject being the sender's email and the message being the updated message from the previous step
