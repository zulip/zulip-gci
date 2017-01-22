I had some issues doing this setup process, not gonna lie. Long story short:
First I had some issues with ssh keys. 
Once I managed to connect to  the dev server and open the localhost, the button for downloading the zuliprc file
didn't appear and I got errors when I tried to run python run.py lib/followup.py --config-file ~/.zuliprc-local because I was
trying to connect zulip with the credentials of localhost. Once all the previous problems were sorted out, the bot was working!
