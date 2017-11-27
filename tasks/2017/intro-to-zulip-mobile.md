# GCI Tasks: Intro to Zulip Mobile Development (React Native)

## Prerequisites

* Having completed our beginner tasks to learn about Git:
  [git-comfortable](git-comfortable.md) and [Submit a Pull Request](submit-a-pull-request.md)

* Having cloned the
  [zulip-mobile](https://github.com/zulip/zulip-mobile) repository and
  created a feature branch. [Learn how](../../before-every-task.md).

* Some confidence from completing other tasks or previous experience
  with mobile development.  Mobile environments can be difficult to
  setup and Zulip's mobile experience is less well-documented than the
  rest of Zulip, so this isn't a great first task if you're new to
  programming.

  ### Some useful links to get started with RN & Mobile Development environment

  #### React Native

  * [Facebook official tutorials](https://facebook.github.io/react-native/docs/tutorial.html)
  * [React Native Express](http://www.reactnativeexpress.com)
  * [React Native School](https://www.youtube.com/playlist?list=PLjVnDc2oPyOGBOb75V8CpeSr9Gww8pZdL)
  * [Start Building a React Native Application](https://egghead.io/lessons/react-start-building-a-react-native-application) (quick guide)
  * [Tutorials Point](https://www.tutorialspoint.com/react_native/)

  ##### Android Studio

  * [Download Android Studio](https://developer.android.com/studio/index.html)
  * [Building Your First Android App](https://developer.android.com/training/basics/firstapp/index.html)

  ##### Xcode

  * Download Xcode from [here](https://developer.apple.com/xcode/)
  * [Start Developing iOS Apps](https://developer.apple.com/library/content/referencelibrary/GettingStarted/DevelopiOSAppsSwift/BuildABasicUI.html)

### Setup a development environment

The first thing you'll need to do is setup a working Zulip mobile
development environment. See
[here](https://github.com/zulip/zulip-mobile/blob/master/docs/developer-guide.md#dev-environment)
for instructions on how to set one up.

Take notes on any trouble you run into as you're setting this up;
you'll want to share those notes later in this task.  Your feedback
will help the Zulip community improve the experience of getting
started with mobile development.

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

Then share your experience with us in
[#mobile](https://chat.zulip.org/#narrow/stream/mobile) stream with
topic as `setup feedback | <your name>` (replace `<your name>` with
your name or username).

Now, your task is to:
* share what you have learned with the Zulip mobile team on the
  [#mobile](https://chat.zulip.org/#narrow/stream/mobile) stream
* update the
  [documentation](https://github.com/zulip/zulip-mobile/tree/master/docs)
  with several improvements
* take screenshots of the app which needs to be submitted on the GCI
  tasks interface ([see below](#submit)).

**Tips:**

After running the app, answering the following questions will help you write your docs:

* Is the existing documentation sufficient for helping you setting up
  a development environment?  If not, suggest improvements to help us
  improve them.  Mentors may end up creating follow-up GCI tasks to
  implement your improvement ideas.

* Did you face any problems while setting up your development
  environments (e.g. errors in the command line)? Note these errors
  along with their solutions in your docs.

[This](http://zulip.readthedocs.io/en/latest/tutorials/screenshot-and-gif-software.html) guide will help you in taking screenshots.

### Submit

After running the app:

* narrow to `all private messages` by selecting from the envelope icon
in the sidebar/drawer.  Take a screenshot of the simulator/emulator
window.

* open sidebar/drawer and switch to night mode.  Take a screenshot of
the simulator/emulator window.

* narrow to the `test here` stream, and start composing a new message. Type `:smi` or
any other emoji of your choice.
Take a screenshot of the simulator/emulator window. Make sure the emoji autocomplete
(which will pop up just above compose box) is visible in the screenshot.

Now submit the screenshots, as well as your notes on the development
experience, using the GCI tasks interface.

Mentors will verify:
* That the three screenshots show a working mobile development
  environment.
* That the list of problems/improvements we could make to the mobile
  documentation is present and readable.

Mentors should also create one or more issues in the zulip-mobile repo
with those notes to make sure that we don't forget to address the
problems with the documentation.

### Next steps

Once you've gotten the mobile environment setup, you should do some
tasks working on the mobile app!  We recommend starting with
[finding a few issues](quality-assurance.md) by playing with the app,
and then moving on to working on [fixing issues](issues.md).  Start
with the simplest issues you can find, since mobile development can be
complex, and it's easy to build confident by starting with some
successes.

If you're excited about mobile development, but can't find a good task
to work on, please bring it up in Zulip.  We did not prepare a lot of
tasks for the very beginning of GCI, since we aren't sure how many
students will be excited about mobile; the more activity, the more
tasks we're create.
