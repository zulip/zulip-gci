# How to request a remote Zulip dev instance

Zulip is participating in this year's [Google Code-in][google-gci]. To make it
easy for participants to get started, Digital Ocean is providing virtual
machines for participants.

Any Google Code-in participant may request a remote Zulip developer instance.

## Step 1: Join GitHub and create SSH Keys

To contribute to Zulip and to use a remote Zulip developer instance, you'll
need a GitHub account. If you don't already have one, sign up
[here][github-join].

You'll also need to [create ssh keys and add them to your GitHub
account][github-help-add-ssh-key].

## Step 2: Create a fork of zulip/zulip

Zulip uses a **forked-repo** and **[rebase][gitbook-rebase]-oriented
workflow.**. This means that all contributors create a fork of the [Zulip
repository][github-zulip-zulip] they want to contribute to and then submit pull
requests to the upstream repository to have their contributions reviewed and
accepted.

When we create your Zulip dev instance, we'll connect it to your fork of Zulip,
so that needs to exist before you make your request.

While you're logged in to GitHub, navigate to [zulip/zulip][github-zulip-zulip]
and click the **Fork** button. (See [GitHub's help article][github-help-fork]
for further details).

## Step 3: Make request via chat.zulip.org

Now that you have a GitHub account, have added your ssh keys, and forked
zulip/zulip, you are ready to request your Zulip developer instance.

If you haven't already, creating an account on https://chat.zulip.org/.

Next, join the **GCI remote dev** stream. Create a new **stream message** with
your GitHub username as the **topic** and request your remote dev instance. Be
sure to CC your mentor so they see your request.

Once requested, it will only take a few minutes to create your instance. Once
created, it will be available via ssh at `<username>.zulipdev.org` where
<username> is your GitHub username.

## Next steps

First, take a look at our tips for [developing remotely][dev-remote].

Next, you'll want to read these documents to learn how to use it:

* [Using the Development Environment][using-dev-env]
* [Testing][testing]

[github-join]: https://github.com/join
[github-help-add-ssh-key]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[github-zulip-zulip]: https://github.com/zulip/zulip/
[github-help-fork]: https://help.github.com/articles/fork-a-repo/
[install-direct]: dev-env-first-time-contributors.html
[install-vagrant]: install-ubuntu-without-vagrant-dev.html
[google-gci]: https://codein.withgoogle.com/
[testing]: testing.html
[using-dev-env]: using-dev-environment.html
[dev-remote]: dev-remote.html
