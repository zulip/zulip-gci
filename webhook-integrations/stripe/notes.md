#Stripe webhook integration
---
-Event description follow the pattern `resource.event`
..- `resource` is the type of data that the event relates to eg. invoice, customer
..- `event` is the actual event that took place eg. created, updated, failed etc.

All event Http requests have the following data:
- `id` - a unique string id
- `object` - a string with the value `event`
- `api_version` - The version of the stripe api that sent the event
- `created` - a timestamp of when it was created
- `data` - a hash with the actual data related to the event
- `livemode` - a timestamp of when it was created
- `pending_webhooks` - the number of webhooks left undelivered
- `request` - the id of the api request that caused the event
- `type` - The description of the event. See above

In `data` the following attributes are stored:
- `object` - The actual content of the event. This is a resource - see above. For example a `customer.something` event has a customer object
- `previous_attributes` - A hash with the names of changed attributes and their old values. -Only used for `something.updated` events


The list of events is extensive, but ones that are likely to be relevant to Zulip are:
- `balance.available` - sent when the account balance is updated
- `charge.x` - updates related to you charging a credit card
- `customer.x` - updates about a customer
- `invoice.x` - updates about an invoice
- `order.x` - updates about an order
- `transfer.x` - updates about a transfer

I was only able to generate these events in test mode, as creating a full account requires a full signup with credit card/bank/business details. Thus there is only blank and boring info in the events.
