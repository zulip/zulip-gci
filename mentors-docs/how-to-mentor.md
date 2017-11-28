# How to Mentor

## Know your stuff:

 * Make sure you’re familiar with the Zulip development environment and our 
   [code contribution guide](https://zulip.readthedocs.io/en/latest/code-reviewing.html) 
   from ReadTheDocs so that you can review students’ work.

 * Check out the list of [common issues](common-issues.md) that come up when 
   working with students so that you know how to respond.

 * Have [relelvent Zulip resources](tabs-and-useful-links.md) available so that 
   you can look up 
   answers to student questions or point students in the right directioin to 
   find answers. 


## Teach students how to learn:

 * Skim the index of our [ReadTheDocs](http://zulip.readthedocs.io/en/latest/) 
   so you know the scope of our developer docs
   and can point students to docs (or review them yourself if you don’t know 
   something).

 * Since students are new to open source, part of what you’re teaching them is
   how to figure things out.  So if you don’t know something, feel free to spend
   some time trying to figure it out (and explain how you figured it out when you
   give the student the answer!).  `git grep` is one of the more valuable skills
   you can teach the students.


## Be Nice and Develop Community:

 * [Be encouraging](https://paper.dropbox.com/doc/aNpjVzRthI9YjsZOGNvWn), 
   especially because younger students are still children 
   (13-17 years old!). 

 * Follow the [Code of Conduct](https://zulip.readthedocs.io/en/latest/code-of-conduct.html), 
   and enforce the code of conduct between students.

 * Follow [Google's recommendations](https://developers.google.com/open-source/gci/help/oa-tips#reviewing_student_work)
   for reviewing student work.

 * Tell the admins when you see students helping each other. It will help when 
   determining the winners of the competition, as community support is part of 
   what they are judged on. Share the good karma. 

 * Be as public as possible. If a student asks for help privately, move the
   discussion to a public place where other students will be able to see the
   issue and resolution. That being said, if they are asking for help with
   something that should stay private, it’s fine to keep it private 

 * If a student needs critical feedback on their behavior patterns, bring it up
   on “GCI Mentors”.  We’ll want to send such feedback to the student in a
   private message thread, but it’s important for the org admins to be involved.


## Sign up for shifts:

[Claim your shifts](https://docs.google.com/spreadsheets/d/1ivw43Y6-dhitenj1aknc58J4HoskosMaqZYdo-VeSKg/edit?usp=sharing). 

 * If you are new to the Zulip community and will need training, please sign up
   for at least 5 of our 4-hour shifts over the course of the 7-week program.
   That’s a bit under 1 shift/week.

 * We need lots of coverage for the first two weeks!

   * That is when students are getting their development environment getting set
     up and learning git, so there are lot of “get me unstuck” questions that
     are critical for allowing our students to have a good experience with
     Zulip.

   * We want to have two people per shift, and 24/7 shifts for this period
     because fast response times are so critical to student retention.

   * If you're less experienced with either Zulip or mentorship, sign up for
     your first couple shifts during the first two weeks, when others will be on
     shift as well, so they can help show you how it's done.

 * We’ll send out email reminders every week to sign up for shifts, if you don’t
   know when exactly you will be available, but you know that you want to
   contribute. If you take that route, please drop us a note telling us your
   overall volunteer goals so we know about how much to expect / how much to
   panic-recruit more shift coverage.


## Your job during your shift is to:

 * Answer students’ questions on the GCI app. 

 * Review student task submissions (tasks with status “Quality Assurance”) and 
   leave feedback for students or mark task as finished. You want to close a 
   task when the work is acceptable, even though it may undergo further review 
   and be committed later.

    * Try to stick to the queue as closely as you can, although it is okay to 
      clear out a bunch of easy-to-review tasks before tackling harder-to-review 
      tasks. 

    * Remind students to post a link to the submission in the GCI app - it’s a 
      requirement to keep the tasks and the submissions linked. 

  * Check the backlog of pull requests and maintain it, by:
    
    * Closing duplicated PRs and asking students to learn to work with git 
      rather than opening a new PR for every change

    * Asking students to add a link to the submission in the GCI app, if the PR 
      has been submitted but there is no task for it - it usually means the 
      student worked on the task before claiming it, but it also happens that 
      students just forget to resubmit a task after updating the PR

    * Inviting students to chat with us on Zulip if they have trouble 
      understanding how the GCI and/or development process works

  * Be responsive on the GCI streams on chat.zulip.org

    * Many questions would be requests about the task status, often with 
      @-mentions - we’re striving to be more assertive this year, so don’t 
      prioritize a question just because a student @-mentioned you multiple 
      times.

    * Discuss problematic tasks on mentor chat and ask for help when needed 
      (e.g. asking one of the more experienced mentors to review a complex task 
      you’re not sure about)

    * Sometimes students get lost, especially in the beginning, and asking them 
      to read some introductory docs on Zulip, git etc. might be helpful

    * Encourage other students to help out, since they’re waiting for their 
      tasks to be reviewed anyway, it's a great way to facilitate their learning 
      and make sure everyone is having a good experience

  * When code is ready to merge into zulip.git, add the label 
    “ready for final review” by writing 
    `@zulipbot label “ready for final review”` in a comment on the PR

  * When merging changes to zulip-gci.git, use the “rebase and merge” feature 
    (in the little down-arrow at the right of the “Merge” button) to avoid 
    creating merge commits.

 * Other people not on-shift might be available for help during your shift, but 
   you are the first line of help for students during your shift. 

 * We recommend muting the “GCI mentors shifts” stream when not on shift so that
   you can focus on your own work. Put discussions that you think people might 
   want to catch up on in “GCI mentors”.

 * After a while, you’ll get a pretty good idea on how to tackle all the 
   predefined tasks and who to ask for help when needed - remember we’re always 
   here for you should you have any problems!

 * Be proactive!  
   * Update task descriptions to improve clarity, fix bugs, create new tasks 
     (e.g. to do follow-up work to a task someone completed), etc.