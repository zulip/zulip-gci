One of the major things that we as mentors need to do for the GCI competitors is
to make sure that they always have enough to work on. We need help writing and 
polishing the tasks for the students. 

The overall strategy is to write 
approximately 15 distinct types of tasks, each of which 10-100 students will 
complete. For some learning tasks, every student will do the same thing; for 
others, we’ll have about 20 similar projects, with the same rough instructions 
but some parameterization (e.g. 20 different bots). We need people to both write
new tasks, update old ones, and test-solve the tasks, to make sure that the 
descriptions are clear. 

If you are willing to help with any of that, follow the 
below workflow for polishing a task in this version-controlled repo. Once you 
are done, tell the admins, and they will upload the task to the GCI webapp for 
students to claim and work on.

  1. Take a task idea issue from the 
  [task creation project](https://github.com/zulip/zulip-gci/projects/1) 
  or a make a new task from an idea that you have on your own.

  2. Create or update the task in the   
  [tasks/2017](https://github.com/zulip/zulip-gci/tree/master/tasks/2017)
  folder of the zulip-gci repo.

  3. Test-solve the task: verify every link, follow the instructions, check for
  variations from the default style in Zulip today and adjust them

  4. Open a pull request.

  5. Get someone else to try to follow the instructions and verify your work,
and comment that they did so.

  6. Add an upload script to the 
  [scripts folder](https://github.com/zulip/zulip-gci/tree/master/scripts/2017) 
  and do a dry run with a fake API key to test it.

  7. Fix any issues, repeat, and merge the tasks

  8. Let the GCI admins (Lyla, Tim, Vishnu) know: we’ll bulk-create the tasks
in the GCI webapp. 

  9. If there’s a directory for the task’s submissions in the [submissions repo]
(https://github.com/zulip/zulip-gci-submissions), update the link in that
directory to point to the 2017 version of the task (see e.g. [translations/]
(https://github.com/zulip/zulip-gci-submissions/tree/master/translations))

  Yay, work complete!
