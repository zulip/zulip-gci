# GCI Tasks: Visual art

## Prerequisites

* You need to know how to create a GitHub pull request. Check out the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/dashboard/tasks/4884433561714688/)
  task if you aren't sure how to do this, or read through the task
  description [here](https://github.com/zulip/zulip-gci/blob/master/tasks/2017/submit-a-pull-request.md).

## Background

As a group chat app, Zulip uses visual art in many ways - users can add their
own avatars, use emoji reactions, and upload images, videos and GIFs.

You can create your own art in a variety of ways:
- using any editor you already used for creating art on your computer
- using a graphics editor such as [Krita](https://krita.org/en/)
- using a vector art editor such as [Vectr](https://vectr.com/)
- using a pixel art editor such as [Piskel](https://www.piskelapp.com/)
- using an image editor such as [GIMP](https://www.gimp.org/)

Choose a tool that works best for you!

## Task Descriptions

There are four types of tasks in this category, each corresponding to one of
the Task Types below.

### Task Type A: Draw user avatars

Zulip would like to provide a library of cute custom avatars that users can
choose from when creating an account. Our non-custom avatars are automatically
generated [identicons](https://en.wikipedia.org/wiki/Identicon). In this task,
you'll create a set of user avatars with a shared theme.

* Create a directory `draw-avatars/<username>`, where `<username>` is
  your GitHub username.

* Design 4-5 avatar images that fit together thematically, e.g. animals,     
  monsters, smiley faces. They should look good at 50x50px as well as 300x300px
  size. If possible, try to use a vector format for the avatars. It’s OK for
  the first versions of these to be rough versions; it makes sense to defer
  spending a lot of time making them really good until you’ve gotten feedback
  on which design directions others like.

* Don't use others' work for your avatars - do not submit images from the
  Internet. Create the avatars on your own.

* Add the images to the directory above, either as SVG files or two PNG images  
  for each avatar, at 50x50 and 300x300 pixel.

* Add a commit with these files, with commit message "visual art: Add
  a/an `<theme>` avatar set.", where `<theme>` is the leading theme of your
  avatar set, e.g. cute monsters.

* Submit a pull request to the `zulip/zulip-gci-submissions` repository, with
  title "visual art: Draw a/an `<theme>` avatar set.". Include a link to the
  pull request when you submit your task on the GCI website.

**Making inclusive avatars**

Some tips on making your avatars inclusive and diverse:
- avoiding humanoid avatars is usually a good idea
- users often like cute animals or creatures
- well designed initials are always welcome - if you're creating text-only
  avatars, create a set for all 24 letters
- smiley faces and custom emoji are used quite often
- aliens and monsters allow for a lot of creativity
- using Zulip brand colors and logo in creative ways can be a base for avatars
- everyday objects, especially computer-related, might be interesting

If you want to read more on inclusive avatars, here's a [great article](https://uxdesign.cc/design-avatars-that-make-sense-and-be-more-inclusive-in-the-process-d4dd6a486ea6).

*Completion criteria:*
* Student submitted 4-5 distinct avatars (24 if avatars are text-only) either
  in SVG format or as 2 PNGs (50x50px and 300x300px) per avatar.
* The avatars share a theme, e.g. it's a set of animals, monsters or smiley
faces.
* The avatars' distinct features are clear in the 50x50px image.
* The avatars are student's own work, not images downloaded from the Internet.

### Task Type B: Generate identicons for user avatars

Currently, Zulip's non-custom avatars are  [identicons](https://en.wikipedia.org/wiki/Identicon) automatically generated
by Gravatar. In this task, you'll generate your own identicons for user avatars.

* Create a directory `generate-avatars/<username>`, where `<username>` is
  your GitHub username.

* Write a Python 3 script for generating identicons from provided data - allow  
  it to take as many arguments as provided when running the script, with a
  minimum of 1. The script should hash the provided data, translate the hash to
  a 50x50px image and save the file as PNG. Call this file
  `generate-identicons.py` and add it to the directory.

* Test run your script with different inputs and save 5 different identicons as
  PNG files (name them `avatar-1.png`, `avatar-2.png` etc.). Add them to the
  directory.

* Add a `README.md` file to your directory. Describe your approach to hashing
  the data and translating it to a 50x50px image. Add information on the
  examples you provided - provide the input data for each of your saved images.

* Add a commit with these files, with commit message "visual art: Add    
  a script for user identicons.".

* Submit a pull request to the `zulip/zulip-gci-submissions` repository, with
  title "visual art: Generate identicons for user avatars.". Include a link to
  the pull request when you submit your task on the GCI website.

**Generating identicons**

Identicons are usually generated by hashing chosen user data (like name or
email) and using that hash to flip image pixels on and off. For creating an
image with Python you need to:

1. Hash the input data.

2. Figure out a way to translate the hash to a 50x50px image.

3. Draw and save the image

To make your identicons more appealing, you can experiment with foreground and
background colors.

*Completion criteria:*
* Student submitted a Python 3 script for generating identicons with at least
  one required argument for hashing.
* Student submitted 5 distinct avatars as 50x50px PNGs, with names
  `avatar-1.png`, `avatar-2.png` etc.
* Student submitted a `README.md` in which they explain their approach and
  provide input data for generated avatars - the mentor will test if the input
  data generates avatars similar to the ones provided by the student.
* The script is student's own work.

### Task Type C: Create a custom animated reaction

Zulip allows for adding custom emoji and supports GIFs as reactions. Creating
custom animated reactions could add some sparkle to the user experience.

* Create a directory `animated-reactions/<username>`, where `<username>` is
  your GitHub username.

* There are two ways you could go about this task:

a. Creating animated reactions from existing emoji
  Pick an emoji from [Noto Emoji](https://github.com/googlei18n/noto-emoji) and
  think of a way to animate it - maybe you want to create a transformation
  between two emoji? Animate a smile to move on a smiling face? Enlarge a heart?
  Create all the steps for the animation. Make sure the background for the
  images is transparent. Make sure the images look good at 32x32px.

b. Creating animated reactions from your own art
  Create your own image and think of ways to animate it. Create all the steps
  for the animation. Make sure the background for the images is transparent.
  Make sure the images look good at 32x32px.

* Create a 32x32px GIF from the image. There are many online tools you could
  use for that, you could also use GIMP layers for creating an animation.

* Add the images and the GIF to the directory above.

* Add a commit with these files, with commit message "visual art: Add
  a/an <name> animated reaction.", where `<name>` is the name of your animation
  e.g. growing heart.

* Submit a pull request to the `zulip/zulip-gci-submissions` repository, with
  title "visual art: Create a/an <name> animated reaction." Include a link to
  the pull request when you submit your task on the GCI website.

*Completion criteria:*
* Student submitted an animated reaction as a 32x32px GIF, alongside the image
  files used in the animation.
* The animation uses either existing Noto Emoji or custom art created by the
  student.
* The animation's distinct features are clear in the 32x32px image.

### Task Type D: Create a standalone animation

Users learn a lot about Zulip from our website. We would love to have some
custom animations we could use on our website and in blog posts.

* Create a directory `standalone-animations/<username>`, where `<username>` is
  your GitHub username.

* Come up with a custom animation for Zulip. You can get inspired by existing
  art featured on [our website](https://zulipchat.com/) or have some ideas for
  animating our logo.

* There are two ways you could go about this task:

a. Creating SVG-based animations
  Use a set of SVG images and write code to transition between them.

b. Creating pure CSS animations
  Use pure CSS3 for creating an animation.

* Add the files for your animation to the directory above.

* Add a commit with these files, with commit message "visual art: Add
  a/an <name> standalone animation", where `<name>` is the name of your
  animation e.g. happy octopus.

* Submit a pull request to the `zulip/zulip-gci-submissions` repository, with
  title "visual art: Create a/an <name> standalone animation." Describe what
  is the intended behavior for the animation. Include a link to the pull
  request when you submit your task on the GCI website.

*Completion criteria:*
* Student submitted an standalone animation with all the files used in the    
  animation.
* The animation is created by using either SVG or pure CSS animations.
* The animation is student's own work.
* The animation is related to Zulip and student expressed their reasoning for
  the idea in the pull request.

## General notes

* If you have an idea for a visual element for Zulip, that's great! Discuss it
on [Zulip](https://chat.zulip.org) - try to think of something that could be
used in the chat itself and would be fun or practical for users.
