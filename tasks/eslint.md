# GCI Tasks: JavaScript code style cleanup

## Prerequisites

* A working Zulip development environment. See
  [here](https://github.com/zulip/zulip-gci/blob/master/README.md) for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../before-every-task.md).

* If this is your first contribution, you may be interested in the
  [how to create a pull request](https://codein.withgoogle.com/tasks/6541581402243072/) and
  [intro to Zulip server development](https://codein.withgoogle.com/tasks/4799263762546688/) tasks.

## Background
One can use special programs, called linters, to check whether code matches a
particular coding style; basically, a linter program reads the code of another
program and checks if it follows specific syntactic rules about how the code
is written.

Zulip’s linter tool tools/lint-all has been configured to run [eslint][eslint]
which checks the rules in [.eslintrc.json][eslintrc]. Some of the rules have
been set to warning (or off) instead of erroring, because the Zulip codebase
does not pass them.

Our goal is to have Zulip pass all of these rules by the end of GCI.

[eslint]: http://eslint.org/
[eslintrc]: http://eslint.org/docs/user-guide/configuring#configuration-file-formats

# Task Description

Each task in this category involves making Zulip pass one of the rules
in `.eslintrc.json`.

Let `rule` be the rule in the task description on
[codein.withgoogle.com](codein.withgoogle.com).

1. Edit `.eslintrc.json` to switch the rule from 0 (off) or 1 (warning)
   to the value specified in the task description. For example, in the 
   case of the rule `no-alert`, the value specified is `2`, so the changed
   rule looks like:

   ```
   "no-alert": 2
   ```

   In the case of `comma-dangle`, changing the rule to the value specified
   means the rule will now look like:

   ```
   "comma-dangle": ["error", {
     "arrays": "always-multiline",
     "objects": "always-multiline",
     "imports": "always-multiline",
     "exports": "always-multiline",
     "functions": "always-multiline"
   }],
   ```
2. Run `tools/lint-all`. This will print a list of errors.
3. Fix the errors. You can either do this by hand, write a script, or use `eslint`'s
   [--fix](http://eslint.org/docs/user-guide/command-line-interface#fix) option
   or some combination.  If you do use `--fix`, you still need to review
   the code manually to confirm that the changes look correct! Follow 
   [these instructions](#using-eslint---fix) to use `--fix`.
4. Run `tools/test-all`, and make sure your code (still) passes all the tests.
5. Add a commit with message 'eslint: change `rule` from warning to
   error and fix violations' (where a value is specified, use that
   instead of error, and if the current value is `0` or `off`, mention
   that).
6. Submit a pull request to the `zulip/zulip` repository using the commit
   message as the title. Include a link to the pull request when you submit
   your task on the GCI website.

An example pull request (PR) would look like this: https://github.com/zulip/zulip/pull/2408

_Completion criteria_:

* PASS_TRAVIS
* Mentor review. Mentors will review all code changes, check that the
  commits and their commit messages match Zulip's guidelines,
  and that the rule has been changed to the specified value.

## Rules that need fixing
All of the rules below have an associated GCI task.
This list is in order of number of errors.
Where possible, a link to the explanation from the airbnb rules docs page is provided.
If the rule has `(--fix)` next to it, it can be fixed using eslint's --fix option.
Follow [these instructions](#using-eslint---fix) to do so.

- [x] [no-loop-func](http://eslint.org/docs/rules/no-loop-func) (1 error) to be changed to `2`
      ([airbnb](http://eslint.org/docs/rules/valid-typeof))
      ([example pull request](https://github.com/zulip/zulip/pull/2408))
- [ ] [new-cap](http://eslint.org/docs/rules/new-cap) (1 error) to be changed
      to `"new-cap": ["error", { "newIsCap": true, "capIsNew": false }]`
      ([airbnb](https://github.com/airbnb/javascript#naming--PascalCase))
- [ ] [no-empty](http://eslint.org/docs/rules/no-empty) (2 errors) to be changed to `2`
- [ ] [yoda](http://eslint.org/docs/rules/yoda) (3 errors) (--fix) to be changed to `2`
- [ ] [space-before-blocks](http://eslint.org/docs/rules/space-before-blocks) (2 errors) (--fix)
      ([airbnb 1](https://github.com/airbnb/javascript#whitespace--before-blocks),
      [2](https://github.com/airbnb/javascript#functions--signature-spacing)) to be changed to `2`
- [ ] [brace-style](http://eslint.org/docs/rules/brace-style) (7 errors) (--fix)
      to be changed to `["error", "1tbs", { "allowSingleLine": true }]`
      ([airbnb](https://github.com/airbnb/javascript#blocks--cuddled-elses))
- [ ] [keyword-spacing](http://eslint.org/docs/rules/keyword-spacing) (12 errors)(--fix)
      ([airbnb](https://github.com/airbnb/javascript#whitespace--around-keywords)) to be changed to

    ```
       "keyword-spacing": ["error", {
          "before": true,
          "after": true,
          "overrides": {
            "return": { "after": true },
            "throw": { "after": true },
            "case": { "after": true }
          }
        }],
    ```
- [ ] [one-var](http://eslint.org/docs/rules/one-var) (32 errors) to be changed to `['error', 'never']`
- [ ] [no-else-return](http://eslint.org/docs/rules/no-else-return) (39 errors) to be changed to `2`
- [ ] [no-plusplus](http://eslint.org/docs/rules/no-plusplus) (40 errors) to be changed to `2`
      ([airbnb](https://github.com/airbnb/javascript#variables--unary-increment-decrement))
- [ ] [no-shadow](http://eslint.org/docs/rules/no-shadow) (56 errors) to be changed to `2`
- [ ] [max-len](http://eslint.org/docs/rules/max-len) (78 errors) to be changed to `2`
      ([airbnb](https://github.com/airbnb/javascript#whitespace--max-len)) to be changed to

    ```
        "max-len": ["error", 100, 2, {
          "ignoreUrls": true,
          "ignoreComments": false,
          "ignoreRegExpLiterals": true,
          "ignoreStrings": true,
          "ignoreTemplateLiterals": true
        }],
    ```

- [ ] [quote-props](http://eslint.org/docs/rules/quote-props) (201 errors) (--fix) to be changed
      to `["error", "as-needed", { "keywords": false, "unnecessary": true, "numbers": false }]`
      ([airbnb](https://github.com/airbnb/javascript#objects--quoted-props))
- [ ] [no-unused-vars](http://eslint.org/docs/rules/no-unused-vars) (221 errors) to be changed
      to `["error", { "vars": "local", "args": "after-used" }]`
- [ ] [comma-dangle](http://eslint.org/docs/rules/comma-dangle) (795 errors) (--fix)
      ([airbnb](https://github.com/airbnb/javascript#commas--dangling)) to be changed to

    ```
        "comma-dangle": ["error", {
          "arrays": "always-multiline",
          "objects": "always-multiline",
          "imports": "always-multiline",
          "exports": "always-multiline",
          "functions": "always-multiline"
        }],
    ```

    Note that there's an `eslint --fix` command that will do this automatically;
    you shouldn't change all 800 of these manually.


## Rules that need not be changed
The rules below do not have an associated GCI task.

1. strict - when we switch to ES6, babel will insert this for us
2. no-console - this is only a warning in airbnb’s lint rules, perhaps this can be discussed later?
3. [camelcase](http://eslint.org/docs/rules/camelcase) (3680 errors)
   [airbnb's recommendation](https://github.com/airbnb/javascript#naming--camelCase))
   is `["error", { "properties": "never" }]`,
4. [quotes](http://eslint.org/docs/rules/quotes) (5773 errors) (--fix)
   [airbnb's recommendation](https://github.com/airbnb/javascript#strings--quotes))
   is `["error", "single", { "avoidEscape": true }]`
5. [no-underscore-dangle](http://eslint.org/docs/rules/no-underscore-dangle) (410 errors)
      ([airbnb](https://github.com/airbnb/javascript#naming--leading-underscore))

## Using eslint --fix
Some of the rules can be fixed with eslint's 
[--fix](http://eslint.org/docs/user-guide/command-line-interface#fix) option. 
However, we would like to change just one rule per PR. Doing this involves a few steps,
since `--fix` seems to fix all warnings as well as errors. 
One way to work around this is to do the following:

1. Change the rule that you are fixing to the specified value.
2. `git add .eslintrc.json && git commit` with an appropriate commit message.
3. Run `tools/lint-all` to see which files need changing.
4. Change all warnings (`1`) to `0` (ignore).
5. Run `eslint --fix static/js frontend_tests`. Note: If there are files in other directories, 
   add them here.
6. Run `git checkout .eslintrc.json`.
7. Run `git add . && git commit` with a commit message explaining the fixes.
