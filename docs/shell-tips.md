# Shell tips

The *shell* a is a **command line interpreter**. To use it you can open a
*terminal* (sometimes called a *console*). This is how most terminal windows
look like:

![An example shell window](shell-screenshot.png)

If you haven't used it before, you should probably take a look at
[this tutorial](http://linuxcommand.org/lc3_learning_the_shell.php).

If you're using Windows,
[these videos](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGDV6SnbINlVUd0o2xT4JbMu)
may be useful too, but keep in mind that the following tips only apply to
Linux/macOS environments (Unix shells). You can also use a tool, for example
[Cygwin](https://www.cygwin.com/), to have a Unix-like shell on Windows. 

## The prompt (`$`)

When searching Google, or Zulip's docs, you'll find commands that begin
with a dollar sign `$` or a dollar sign preceded by some text
(e.g. `(venv)john@laptop:~$`).

This is called the **prompt**, and it's only an indicator that the shell is
awaiting new orders. The prompt can contain useful information, let's look
at `(venv)john@laptop:~$`:

- `(venv)` informs the user that they're currently in a virtual environment
(more on [Python virtual
  environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/))
- the `john` before `@` is the username
- the `laptop` is the host machine name
- the `~` after the colon informs the user they're currently in the home
folder of the user `john`

You shouldn't type the prompt or the text preceding it, since it isn't a
part of the commands.

## Tilde character (`~`)

It's very frequent to see the tilde (`~`) in paths. The tilde is an
abbreviation for your home directory (`/home/YOUR_USERNAME` most of the times).

That's why the following is exactly the same, if the user running it is
`john`:

```
$ cd ~
$ cd /home/john
```

## Running commands as root (`sudo`)

You may have noticed that many commands begin with `sudo`. This informs the
shell that the following command must be run as the root - a user that by
default has access to all commands and files on a Unix operating system (i.e.
a user with administrator privileges). That's why you may be asked for a
password in those cases: the system verifies you have permission to act as
the *root* user.

As a curiosity, the name `sudo` comes from **s**uper **u**ser **do**.

## Escaping characters

Some characters cannot be used directly in the shell, because they have a
special meaning. Consider the following example:

```
$ echo "He said hello"
He said hello
```

What if you wanted to display double quotes? You can't use
`echo "He said "hello""`, because in that case you're using the
double quotes for two different purposes:

- Delimiting the string you want to use, from `He` to `"hello"`.
- Quoting something, by literally printing `"`.

You have to specify which double quotes are used in each case. When you want
one of those "special characters" to be literally printed, that's called
**character escaping**. To escape a character, simply add a backslash (`\`)
before it.

Returning to our example:

```
$ echo "He said \"hello\""
He said "hello"
```

As you can see, the double quotes with the backslash are shown, but the ones
without it are used as string delimiters.

Double quotes aren't the only case of special characters. Some others are `$`,
`#`, `{` or `}`, but there are many more. The backslash itself can be escaped
as well, using the same procedure: `\\`.

## Sequencing commands

It's also possible to run multiple commands in a single line. For that purpose,
the shell provides two different separators:

- **Semicolon `;`**: runs a command, and once it has finished, runs the next
  one:

  ```
  $ echo "Hello"; echo "World!"
  Hello
  World!
  ```

- **Double ampersand `&&`**: runs a command, and **only if** it finished
  without errors, it proceeds with the next one:

  ```
  $ qwfvijwe && echo "Hello"
  qwfvijwe: command not found
  ```

  Notice that it doesn't print `Hello` at the end, because the previous
  command (`qwfvijwe`) returned an error.

  When using an incorrect command with a semicolon, the `Hello` will still
  be printed:

  ```
  $ qwfvijwe; echo "Hello"
  qwfvijwe: command not found
  Hello
  ```

## Splitting commands into multiple lines

Sometimes you end up with a very long command, that is hard to read and may
be unclear. This is a problem, especially if you want to share that command,
e.g. in a documentation file.

In those cases, you can use a backslash at the end of each line, to inform the
shell "wait, there's more on the next line".

This is an example, taken from the docs on how to install the Zulip development
environment:

```
sudo apt-get -y purge vagrant && \
wget https://releases.hashicorp.com/vagrant/1.8.6/vagrant_1.8.6_x86_64.deb && \
sudo dpkg -i vagrant*.deb && \
sudo apt-get -y install build-essential git ruby lxc lxc-templates cgroup-lite redir && \
vagrant plugin install vagrant-lxc && \
vagrant lxc sudoers
```

It's all a single command, joined using the double ampersand explained in
[Sequencing commands](#sequencing-commands). If you're typing it manually,
you don't need to include the backslashes, just write it all on the same line,
and hit <kbd>ENTER</kbd>/<kbd>RETURN</kbd> at the end.

If you think about it, what is happening here is actually another case of
character escaping. The newline character (the one that appears when you hit
<kbd>ENTER</kbd>) usually means "read this command". However, here we want to literally
have the newline character, and thus the `\<newline>`.

The newline character is invisible (we only see a line break), but it's still
there!

## Understanding commands

Frequently, you may find commands that you don't understand, or don't
know what they do. You can use `man <command>` to see the **man**ual page for
that specific command. Also, you may find useful
[explainshell](http://explainshell.com/), a webpage that explains what most
commands do, part by part.
