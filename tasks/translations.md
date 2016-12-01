# GCI Tasks: Creating translation style guides

## Prerequisites

* Native fluency in the appropriate language.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

* You need to know how to create a GitHub pull request. Check out the
  [Learn how to create a GitHub Pull Request](https://codein.withgoogle.com/tasks/6541581402243072/)
  task if you aren't sure how to do this, or read through the task description
  [here](https://github.com/zulip/zulip-gci/blob/master/tasks/submit-a-pull-request.md).

## Background

Zulip is a tool used by many teams daily. In order to make it more approachable
to users, there is an ongoing translation effort. [Read more about translating
Zulip](https://zulip.readthedocs.io/en/latest/translating.html).

This group of tasks is about creating common translation style guides, to give
guidance on how Zulip should be translated into specific languages. Currently
we have a benchmark [Chinese](https://zulip.readthedocs.io/en/latest/chinese.html)
guide and initial [Polish](https://zulip.readthedocs.io/en/latest/polish.html)
and [Spanish](https://zulip.readthedocs.io/en/latest/spanish.html) guides.

## Task Descriptions

Let *language* and `<language>` be the language mentioned in the task that
brought you here.

### Task Type A: Research web application translations

* Find three different web applications that have been translated into the
*language*. Some examples of applications translated into multiple languages:
  * Facebook
  * GMail
  * Twitter
  * Instagram
  * Skype
  * YouTube
  * Wikpedia

* Look for common words and phrases associated with web applications such as
*log in*, *home*, *reply* etc. Take screenshots of the applications with the
interface both in English and *language* - save the English screenshots as
`<application>_EN.png` and the *language* screenshots as `<application>.png`.
Add the screenshots to a new folder `translations/<language>/research`.

* Think about the language used - is it more formal or informal? Are there any
specific forms that should or shouldn't be used? What words or phrases are most
commonly used? What could sound awkward?

* Are there any other specific requirements for the *language*? Does the
application interface change when you switch languages? Is the *language*
right-to-left or left-to-right? Does it require any special encodings or
characters?

* Write your notes as `notes.md` in `translations/<language>/research`.

* Create a commit with the screenshots and notes, with commit message
`translations: Research translations for <language>.`.

* Create a pull request in the `zulip/zulip-gci` repository, with title
`translations: Research translations for <language>.`.

*Completion criteria*: The mentors will verify that you successfully created a
pull request with at least 6 screenshots of 3 different interfaces and notes.

### Task Type B: Write general rules for translations

* Create a new file `general-rules.md` in `translations/<language>`.

* Write rules for translations specific to the *language*. If applicable, answer
the following questions:

  * Should the language be formal or informal?

  * Which grammatical person should be used for translations (e.g. second person
    singular, first person plural)?

  * What verbs should be used (e.g. active, imperative, continuous)?

  * Are there any particles that should or should not be used (e.g. reflexives)?

  * What types words or phrases should not be used (e.g. slang, regional)?

* Make sure you mention:

  * Consistent usage of Zulip-specific terms and common verbs for actions

  * Mindful usage of long words and phrases to keep frontend working properly

  * Balancing common verbs and nouns with specific IT-related translation of
  English terms

* Add any other rules you believe are appropriate in the *language* context.

* Reference the [Chinese](https://zulip.readthedocs.io/en/latest/chinese.html),
[Polish](https://zulip.readthedocs.io/en/latest/polish.html)
and [Spanish](https://zulip.readthedocs.io/en/latest/spanish.html) style guides
for inspiration and to make sure you didn't omit any important rules.

* Communicate with other native speakers of the *language* in the Zulip
`translation` stream.

* Create a commit with the `general-rules.md`, with commit message  `translations:
Write general rules for <language>.`.

* Create a pull request in the `zulip/zulip-gci` repository, with title
`translations: Write general rules for <language>.`.

*Completion criteria*: The mentors will verify that you have created general
rules for *language*. Additional questions about specific rules may be asked by
fluent *language* speakers, to make sure the guide is appropriate.

### Task Type C: Translate special terms used in Zulip

* Create a new file `special-terms.md` in `translations/<language>`.

* Translate every term in [this list](/translation-terms.md) to *language* in
the format `English word: *language word*, [explanation for the
decision], [example usage in the Zulip context]`.

* Reference the [Chinese](https://zulip.readthedocs.io/en/latest/chinese.html)
style guide for formatting your `.md` file. Put the words in their appropriate
sections.

* Communicate with other native speakers of the *language* in the Zulip
`translation` stream.

* Create a commit with the `special-terms.md`, with commit message  `translations:
Translate special terms for <language>.`.

* Create a pull request in the `zulip/zulip-gci` repository, with title
`translations: Translate special terms for <language>.`.

*Completion criteria*: The mentors will verify that you have translated all the
special terms into *language*. Additional questions about specific translations
may be asked by fluent *language* speakers, to make sure the translation is
appropriate.

### Task Type D: Improve existing style guides

* Improve the existing *language* style guide, using the [Chinese](https://zulip.readthedocs.io/en/latest/chinese.html) style guide as
your benchmark. Make sure your improvement includes:

  * Putting the initial general rules in the *Notes* section
  * Diving the *Special terms used in Zulip* into *Terms*, *Phrases* and *Other*
  sections
  * Adding any missing terms in the appropriate sections - the full list of words
  is available [here](/translation-terms.md) (do not remove any existing
  translations)
  * Providing example usage of the translated terms in the Zulip context
  * Refactoring the formatting of the markdown file

* Communicate with other native speakers of the *language* in the Zulip
`translation` stream. Before you change an existing translation of a word, be
sure to talk about it.

* Create a commit with the improvements, with commit message `translations:
Improving the <language> style guide.`

* Create a pull request in the `zulip/zulip` repository, with title `translations:
 Improving the <language> style guide.`

*Completion criteria*: The mentors will verify that you have improved the style
guide and put the translated terms in the appropriate sections, providing
examples of usage in the *language*. Additional questions about specific
translations may be asked by fluent *language* speakers, to make sure the
translation is appropriate.

### Task Type E: Propose a language

* Create a topic on your *language* in the Zulip `translation` stream. Describe
your experience with the *language*, e.g. *I'm a native speaker of the [language],
I currently live in the [language_country_of_origin]*.

* Do **Task Type A** for the *language*.

* As soon as your pull request is accepted, request mentors to create Tasks Type
B and C for the *language*.

*Completion criteria*: The mentors will verify that you have completed the
**Task Type A** for the *language* and created the appropriate topic in the
`translation` stream. They will also check that you have requested appropriate
tasks and @mention you when they are published.

## General notes

This group of tasks is intended for fluent speakers of the *language*.
