# GCI Tasks: JavaScript code style cleanup

`.eslintrc` contains a list of rules that we would like to lint our JavaScript
code with. Some of them error on our code, so they have been switched to warnings
instead. A task would look like:

1. Edit `.eslintrc` to switch a rule from 0 (off) or 1 (warning) to 2 (error)
   or the value specified in the task description
2. Run `tools/lint-all`
3. Fix the errors

An example PR would look like https://github.com/zulip/zulip/pull/2408 

## Rules that need fixing
Unless otherwise mentioned, change the value from 0 or 1 to 2.
This list is in order of number of errors.
Where possible, a link to the explanation from the airbnb rules docs page is provided.
Some of these rules may be fixed using `node npm_modules/.bin/eslint --fix`
(after changing the value in `eslintrc` appropriately)

1. [block-scoped-var](http://eslint.org/docs/rules/block-scoped-var) (0 errors)
2. [guard-for-in](http://eslint.org/docs/rules/guard-for-in) (0 errors)
3. [radix](http://eslint.org/docs/rules/radix) (0 errors) 
   ([airbnb](http://eslint.org/docs/rules/guard-for-in))
4. [valid-typeof](http://eslint.org/docs/rules/valid-typeof) (0 errors) to be changed
   to `['error', { requireStringLiterals: true }]` 
5. [no-loop-func](http://eslint.org/docs/rules/no-loop-func) (1 error) 
   ([airbnb](http://eslint.org/docs/rules/valid-typeof)) 
   ([example PR](https://github.com/zulip/zulip/pull/2408))
6. [new-cap](http://eslint.org/docs/rules/new-cap) (1 error) to be changed
   to `'new-cap': ['error', { newIsCap: true, capIsNew: false, }]`
   ([airbnb](https://github.com/airbnb/javascript#naming--PascalCase))
7. [no-empty](http://eslint.org/docs/rules/no-empty) (2 errors)
8. [space-before-blocks](http://eslint.org/docs/rules/space-before-blocks) (2 errors) (--fix) 
   ([airbnb 1](https://github.com/airbnb/javascript#whitespace--before-blocks), 
   [2](https://github.com/airbnb/javascript#functions--signature-spacing))
9. [yoda](http://eslint.org/docs/rules/yoda) (3 errors) (--fix)
10. [brace-style](http://eslint.org/docs/rules/brace-style) (7 errors) (--fix) 
    to be changed to `['error', '1tbs', { allowSingleLine: true }]`
    ([airbnb](https://github.com/airbnb/javascript#blocks--cuddled-elses))
11. [keyword-spacing](http://eslint.org/docs/rules/keyword-spacing) (12 errors) (--fix)
    ([airbnb](https://github.com/airbnb/javascript#whitespace--around-keywords)) to be changed to 

    ```
       'keyword-spacing': ['error', {
          before: true,
          after: true,
          overrides: {
            return: { after: true },
            throw: { after: true },
            case: { after: true }
          }
        }],
    ```

12. [one-var](http://eslint.org/docs/rules/one-var) (32 errors) to be changed to `['error', 'never']` 
13. [no-else-return](http://eslint.org/docs/rules/no-else-return) (39 errors)
14. [no-plusplus](http://eslint.org/docs/rules/no-plusplus) (40 errors)
    ([airbnb](https://github.com/airbnb/javascript#variables--unary-increment-decrement))
15. [no-shadow](http://eslint.org/docs/rules/no-shadow) (56 errors)
16. [max-len](http://eslint.org/docs/rules/max-len) (78 errors)
    ([airbnb](https://github.com/airbnb/javascript#whitespace--max-len)) to be changed to 

    ```
        'max-len': ['error', 100, 2, {
          ignoreUrls: true,
          ignoreComments: false,
          ignoreRegExpLiterals: true,
          ignoreStrings: true,
          ignoreTemplateLiterals: true,
        }],
    ```

17. [quote-props](http://eslint.org/docs/rules/quote-props) (201 errors) (--fix) to be changed
    to `['error', 'as-needed', { keywords: false, unnecessary: true, numbers: false }]`
    ([airbnb](https://github.com/airbnb/javascript#objects--quoted-props))
18. [no-unused-vars](http://eslint.org/docs/rules/no-unused-vars) (221 errors) to be changed
    to `['error', { vars: 'local', args: 'after-used' }]` 
19. [no-underscore-dangle](http://eslint.org/docs/rules/no-underscore-dangle) (410 errors)
    ([airbnb](https://github.com/airbnb/javascript#naming--leading-underscore))
20. [comma-dangle](http://eslint.org/docs/rules/comma-dangle) (795 errors) (--fix)
    ([airbnb](https://github.com/airbnb/javascript#commas--dangling)) to be changed to 

    ```
        'comma-dangle': ['error', {
          arrays: 'always-multiline',
          objects: 'always-multiline',
          imports: 'always-multiline',
          exports: 'always-multiline',
          functions: 'always-multiline',
        }],
    ```

21. [camelcase](http://eslint.org/docs/rules/camelcase) (3680 errors)
    ([airbnb](https://github.com/airbnb/javascript#naming--camelCase)) to be changed 
    to `['error', { properties: 'never' }]` 
22. [quotes](http://eslint.org/docs/rules/quotes) (5773 errors) (--fix) to be changed to 
    `['error', 'single', { avoidEscape: true }]`
    ([airbnb](https://github.com/airbnb/javascript#strings--quotes))

## Rules that need not be changed
1. strict - when we switch to ES6, babel will insert this for us
2. no-console - this is only a warning in airbnb’s lint rules, perhaps this can be discussed later?

