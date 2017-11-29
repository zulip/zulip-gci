# GCI Tasks: Increase node test coverage

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.
* Experience working in the Zulip server environment.  We recommend completing the
  [Intro to Zulip Server development beginner task](https://github.com/zulip/zulip-gci/blob/master/tasks/intro-to-zulip-server.md).
* Learn how [testing](http://zulip.readthedocs.io/en/latest/testing/testing.html)
  works in Zulip and how to write tests, specifically [JavaScript unit tests](http://zulip.readthedocs.io/en/latest/testing/testing-with-node.html). 
* Know how to submit a [pull request](https://github.com/zulip/zulip-gci/blob/master/tasks/2017/submit-a-pull-request.md).

## Background

Unit tests ensure the quality and correctness of your code, especially when doing
large code refactorings, and prevent regressions. Zulip uses node to unit test its
150+ JavaScript files.

You should definitely read how our JavaScript unit tests work and how to write them:
http://zulip.readthedocs.io/en/latest/testing/testing-with-node.html.

You will be writing node tests for Zulip's webapp repository [`zulip/zulip`](https://github.com/zulip/zulip).
You can find all our existing node tests in `frontend_tests/node_tests` directory.

## Task Description

Let *file* be the file and *functions* be the functions in *file* listed in the task that brought you here.
Again, all files/functions are in the [`zulip/zulip`](https://github.com/zulip/zulip) repository.

**Tip:** All files can be found in directory `static/js/<file>`, where `<file>` is *file*. The corresponding
file you should add tests to is `frontend_tests/node_tests/<file>`, where `<file>` is *file*.

The goal of this task is to obtain full testing coverage for all *functions* in *file*. The following
will help you recognize which lines in *functions* that haven't been tested/covered.

* Start up your [Zulip development environment](https://github.com/zulip/zulip-gci/blob/master/README.md#setting-up-the-zulip-development-environment).
  This will be where you will run all your tests.
* Generate testing coverage reports by running `./tools/test-js-with-node --coverage` in your
  development environment.
* To see the coverage report, open `node-coverage/lcov-report/index.html` locally. Click on the `zulip/static/js` link.
  Then find *file* in the list of files and click on it to see the coverage report for *file*.
    * **Tip:** Another way to see the coverage report is to go to `http://<hostname>:9991/node-coverage/index.html`,
      where `<hostname>` is either `localhost` or the hostname of your VM. Click on the `zulip/static/js` link and then find
      *file* in the list of files to see the coverage report for *file*.
* For example, if you were testing `narrow_state.js`, you should see that 92% of statements are covered in the top left corner.
  You should also see `narrow_state.js` with colored lines, green meaning that line is successfully tested and red
  meaning that line is **not** successfully tested.
* Your task is to test all the red-colored lines in *functions*!

When you successfully covered a function in *functions* in *file*,
* Add a commit with commit message `node tests: Cover <function_name>.`, where 
  `<function_name>` is the function name in *functions*.
* Submit a pull request that contains these commits. Include a link to the pull request
  when you submit your task on the GCI website.

