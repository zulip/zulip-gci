# GCI Tasks: Unit Testing `narrow_state.js`

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

You can find all our existing node tests in `frontend_tests/node_tests`.

## Task Description

The goal of this task is to obtain full testing coverage for `static/js/narrow_state.js`. The following
is to help you recognize which lines in `narrow_state.js` that haven't been tested/covered.

* Start up your [Zulip development environment](https://github.com/zulip/zulip-gci/blob/master/README.md#setting-up-the-zulip-development-environment).
  This will be where you will run all your tests.
* Generate testing coverage reports by running `./tools/test-js-with-node --coverage` in your
  development environment.
* To see the coverage report, open `node-coverage/lcov-report/zulip/static/js/narrow_state.js.html`.
* You should see that 92% of statements are covered in the top left corner. You should also see
  `narrow_state.js` with colored lines, green meaning that line is successfully tested and red
  meaning that line is **not** successfully tested.
* Your task is to test all the red-colored lines!

The functions with lines that still need coverage:
* `exports.operators()`
* `collect_single()`
* `exports.set_compose_defaults()`
* `exports.stream()`
* `exports.topic()`
* `exports.is_for_stream_id()`

When you have reached 100% of statements covered in `narrow_state.js`,
* Add a commit with commit message `tests: Get narrow_state.js to 100% coverage.`
* Submit a pull request that contains this commit. Include a link to the pull request
  when you submit your task on the GCI website.

