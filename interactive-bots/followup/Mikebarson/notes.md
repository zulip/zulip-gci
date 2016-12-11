One of the problems doing the setup part was this:

cd ~/zulip/contrib_bots
python run.py lib/followup.py --config-file ~/.zuliprc-local

the dir to finding  ~/.zuliprc-local was not accurate. It's supposed to be  ~/zulip/.zuliprc-local 
that way it would point to the zulip folder and then to the .zuliprc-local.


