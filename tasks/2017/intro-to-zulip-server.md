# GCI Tasks: Intro to Zulip server development

## Prerequisites

* A working Zulip development environment. See
  https://github.com/zulip/zulip-gci/blob/master/README.md for instructions
  on how to set one up.

* Update your working copy of Zulip and then create a feature branch. [Learn
  how](../../before-every-task.md).

### Practice Running Zulip

Run your Zulip server using
```
tools/run-dev.py
```

Visit your Zulip server at `http://<hostname>:9991`, where `<hostname>` is
either `localhost` or the hostname of your remote VM, and verify that you
can log in by clicking on one of the accounts.

### Grep for code

Find the `check_send_message` function by going to the `zulip/` directory
and entering `git grep 'def check_send_message'`.

#### Modify the code

Modify `check_send_message` so that anytime a user sends a message which says
`welcome`, we convert the content to become `Welcome to Zulip :octopus:`
before `check_send_message` calls `check_message`.

**Hint**: You will want to look at the incoming parameters to the function
and take a guess at which one needs to be modified.  (If you are unsure,
you can add statements like `print(message_to)` to the code and see
what shows up in the server output.)

Test that your change works in the browser, and take a screenshot.

### Add Some Tests

Add some tests to the bottom of `zerver/tests/test_messages.py` to make sure
we do not accidentally break this behavior in the future.

```
class OctopusTest(ZulipTestCase):
    def test_change_welcome_message(self) -> None:
        sender = get_user('iago@zulip.com', get_realm('zulip'))
        client = make_client(name="test suite")
        message_id = check_send_message(sender, client, "stream", ["Verona"], "Zulip Octopus test", "welcome")
        self.assertEqual(
            Message.objects.values_list("content", flat=True).get(id=message_id),
            "Welcome to Zulip :octopus:")

    def test_leave_welcome_message_alone(self) -> None:
        sender = get_user('iago@zulip.com', get_realm('zulip'))
        client = make_client(name="test suite")
        message_id = check_send_message(sender, client, "stream", ["Verona"], "Zulip Octopus test", "Welcome everyone!")
        self.assertEqual(
            Message.objects.values_list("content", flat=True).get(id=message_id),
            "Welcome everyone!")
```
You should also import the `check_send_message` function from `zerver/lib/actions.py`
because this is used in `test_change_welcome_message` and `test_leave_welcome_message_alone`.

Then run
```
tools/test-backend zerver/tests/test_messages.OctopusTest
```
to make sure your code passes the tests you just added. If it doesn't,
fix any brokenness in your code until it does. Take a screenshot of
your terminal.

Run
```
./tools/test-all
```
to verify that your code still passes the entire test suite.

`tools/test-all` is a suite of several tests, and can take a while to run. For
interactive debugging, one often wants to just run a single test in the suite. Run
```
cat tools/test-all
```
and figure out how to run just the lint tests for backend and do so (there should be no
output). Add an extra space to the beginning of any line of code and run the
lint tests again. You should see a bunch of output in red. Take a screenshot of
your terminal.

### Submit

Submit the three screenshots using the GCI tasks interface.
