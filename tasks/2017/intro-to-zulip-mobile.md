# GCI Tasks: Intro to Zulip Mobile Development (React Native)

## Prerequisites

* A working Zulip mobile development environment. See [here](https://github.com/zulip/zulip-mobile/blob/master/docs/developer-guide.md#dev-environment) for instructions on how to set one up.

* Update your working copy of [zulip-mobile](https://github.com/zulip/zulip-mobile) and then create a feature branch. [Learn
  how](../../before-every-task.md).

### Practice Running zulip-mobile

Run the app with one of the following commands:
```
react-native run-ios //  run the app on an iOS device on Mac OS
react-native run-android // run the app on an Android device
```

If you are running on an Android emulator, then make sure it is launched before you
run the command on terminal.

Enter the server URL (we recommend using https://chat.zulip.org for testing)
and your login credentials. Open the left drawer (by clicking on hamburger icon
on top left or swiping from left to right) and narrow to the `test here` stream
then send a message with your name as the topic.

Then share your experience with us in [#mobile](https://chat.zulip.org/#narrow/stream/mobile) stream with topic as `feedback: setting up environment | <your name>` (replace `<your name>` with your name).

Now, your task is to:
* share what you have learned with the Zulip mobile team on the [#mobile](https://chat.zulip.org/#narrow/stream/mobile) stream
* update the [documentation](https://github.com/zulip/zulip-mobile/tree/master/docs) with several improvements
* take screenshots of the app which needs to be submitted on the GCI tasks interface ([see below](#submit)).

**Tips:**
After running the app, answering the following questions will help you write your docs:
* Is the existing documentation sufficient for helping you setting up a development environment?
If not, suggest improvement to help us improve them.
* Did you face any problems while setting up your development environments (e.g. errors in the command line)? Note these errors along with their solutions in your docs.

[This](http://zulip.readthedocs.io/en/latest/tutorials/screenshot-and-gif-software.html) guide will help you in taking screenshots.

### Submit

After running the app

* narrow to `all private messages` by selecting from the envelope icon in the sidebar/drawer.
Take a screenshot of the simulator/emulator window.

* open sidebar/drawer and switch to night mode.
Take a screenshot of the simulator/emulator window.

* narrow to the `test here` stream, and start composing a new message. Type `:smi` or
any other emoji of your choice.
Take a screenshot of the simulator/emulator window. Make sure the emoji autocomplete
(which will pop up just above compose box) is visible in the screenshot.

Now submit the screenshots using the GCI tasks interface.
