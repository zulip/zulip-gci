# German translation style guide (Deutsche Übersetzungsrichtlinien)

The purpose of this guide is to provide an overview of useful terms and phrases
for anyone interested in contributing to the German translation.

## Note (Anmerkung)

General notes and guidelines on translating the Zulip documentation
can be found [here](general-notes.md).

## Terms (Begriffe)

* Message - **Nachricht**

*"Nachricht" (Facebook, WhatsApp, Transifex)*

* Private Message (PM) - **Private Nachricht (PN)**

Since we try to avoid concatenating words whenever possible, don't use
"Privatnachricht" . PN is the officially used abbreviation for
"Private Nachricht" and is used in many German chat forums.

*"Private Nachricht" (Youtube, Transifex)*

* Starred Message - **Markierte Nachricht**

We go with "markiert" instead of "gesternt" (which is not even a proper
German word) here, since it comes closer to the original meaning of "starred".

*"Markierte Nachricht" (GMail, Transifex),
"Nachricht mit Stern" (WhatsApp)*

* Realm - **Realm** (Developer documentation)

**The term "realm" is discouraged in the user documentation and should not be
used there anymore.** However, because of its relevance for the developer
documentation, we still have it included in this list.

* Realm - **Organisation** (User documentation)

While the literal translation for "realm" is "Königreich", it is referring to
different domains/organisations on a Zulip server. Since the German term
"Bereich" is a little vague, "Organisation" is preferable here.

*"Bereich" (Transifex), "Community" (Google+)*

* Stream - **Stream**

Even though the term **Stream** is not commonly used in German web applications,
it is both understood well enough by many Germans with only little English
skills, and the best choice for describing Zulip's chat hierarchy. The term
"Kanal" wouldn't fit here, since it translates to "channel" - these are used
by other chat applications with a simple, flat chat hierarchy, that is,
no differentiation between streams and topics.

*"Stream" (Transifex), "Kanal" (KDE IRC documentation, various
small German forums)*

* Topic - **Thema**

*(Gmail - for email subjects, Transifex)*

* Invite-Only Stream - **Geschlossener Stream**

For users to be able to join to an "invite-only" stream, they must have been
invited by some user in this stream. This type of stream is equivalent to
Facebook's "closed" groups, which in turn translates to "geschlossen" in German.
This translation seems to be appropriate, for example [Linguee](
http://www.linguee.de/englisch-deutsch/uebersetzung/invite-only.html)
search returns only paraphrases of this term.

*"Geschlossener Stream" (Transifex), "Geschlossene Gruppe" (Facebook),
paraphrases (Linguee)*

* Public Stream - **Öffentlicher Stream**

While some might find this direct translation a tad long, the alternative
"Offener Stream" can be ambiguous - especially users who are inexperienced
with Zulip could think of this as streams that are online.

*"Öffentlicher Stream" (Transifex)*

* Bot - **Bot**

Not only is "bot" a short and easily rememberable term, it is also widely used
in German technology magazines, forums, etc.

*"Bot" (Transifex, Heise, Die Zeit)*

* Integration - **Integration**

While the German translation of "Integration" is spelled just like the English
version, the translation is referring to the German term. For this reason,
use "Integrationen" instead of "Integrations" when speaking of multiple
integrations in German. There aren't many German sources available for this
translation, but "Integration" has the same meaning in German and English.

*"Integration/-en" (Transifex)*

* Notification - **Benachrichtigung**

Nice and easy. Other translations for "notification" like
"Erwähnung", "Bescheid" or "Notiz" don't fit here.

*"Benachrichtigung" (Facebook, Gmail, Transifex, Wikipedia)*

* Alert Word - **Signalwort**

This one is tricky, since one might initially think of "Alarmwort" as a proper
translation. "Alarm", however, has a negative connotation, people link it to
unpleasant events. "Signal", on the other hand, is neutral, just like
"alert word". Nevertheless, [Linguee](
http://www.linguee.de/deutsch-englisch/search?source=auto&query=alert+word)
shows that some websites misuse "Alarm" for the translation.

*"Signalwort" (Transifex), "Wort-Alarm" (Linguee)*

* View - **View** (Developer documentation)

Since this is a Zulip-specific term for 
> every path that the Zulip server supports (doesn’t show a 404 page for),

and there is no German equivalent, talking of "Views" is preferable in the
developer documentation and makes it easier to rely on parts of the German
*and* parts of the English documentation.

* View - **Ansicht** (User documentation)

For the user documentation, we want to use "Ansicht" instead of "view", as
"Ansicht" provides a translated description for what you think of when hearing
"view". "Ansicht" is not desirable for the developer documentation, since it
does not emphasize the developing aspects of views (in contrast to anglicisms,
which Germans often link to IT-related definitions).

*"Ansicht" (Transifex)*

* Home - **Startseite**

Nice and easy. "Zuhause" obviously doesn't fit here ;).

*"Startseite" (Facebook, Transifex)*

* Emoji - **Emoji**

"Emoji" is the standard term for Emojis. Any other Germanized translation like
"Bildschriftzeichen" (which exists!) would sound stiff and outdated. "Emoticon"
works as well, but is not that common in German.

*"Emoji" (Facebook, WhatsApp), "Emoticon" (Google+)*

## Phrases (Ausdrücke)

* Subscribe/Unsubscribe - **Abonnieren/Deabonnieren**

This translation is unambiguous.

*"Deabonnieren" (Youtube, Transifex)*

* Narrow to - **Begrenzen auf**

Transifex has two different translations for "Narrow to" -
"Schränke auf ... ein." and "Begrenze auf ... ." Both sound a bit strange to a
German speaker, since he would expect grammatically correct sentences when
using the imperative (e.g. "Schränke diesen Stream ein auf ... .") Since this
would be too long for many labels, the infinitive "begrenzen auf" is preferable.
"einschränken auf" sounds equally good, but Transifex shows more use cases for
"begrenzen auf".

*"Schränke auf ... ein." (Transifex) "Begrenze auf ... ." (Transifex)*

* Filter - **Filtern**

A direct translation is fine here. Watch out to to use the infinitive instead
of the imperative, e.g. "Nachrichten filtern" instead of "Filtere Nachrichten".

*"Filtern" (Thunderbird, LinkedIn)*

* Mute/Unmute - **Stummschalten/Lautschalten**

"Lautschalten" is rarely used in German, but so is "Stummschaltung
deaktivieren". Since anyone can understand the idea behind "Lautschalten", it is
preferable due to its brevity.

* Deactivate/Reactivate - **Deaktivieren/Reaktivieren**

*"Deaktivieren/Reaktivieren" (Transifex)*

* Search - **Suchen**

*"Suchen" (Youtube, Google, Facebook, Transifex)*

* Pin/Unpin - **Anpinnen/Loslösen**

While "pinnen" is shorter than "anpinnen", "anpinnen" sweeps any amiguity out of
the way. This term is not used too often on Zulip, so the length shouldn't be a
problem.

*"Anpinnen/Ablösen" (Transifex), "Pinnen" (Pinterest)*

* Mention/@mention - **Erwähnen/"@-Erwähnen**

Make sure to say "@-erwähnen", but "die @-Erwähnung" (capitalized).

*"Erwähnen/@-Erwähnen" (Transifex)*

* Invalid - **Ungültig**

*"Ungültig" (Transifex)*

* Customization - **Anpassen**

The literal translation "Anpassung" would sound weird in most cases, so we use
the infinitive form "anpassen".

* I want - **Ich möchte**

"Ich möchte" is the polite form of "Ich will".

*"Ich möchte" - (Transifex, general sense of politeness)*

* User - **Nutzer**

"Benutzer" would work as well, but "Nutzer" is shorter and more commonly
used in web applications.

*"Nutzer" (Facebook, Gmail), "Benutzer" (Transifex)*

* Person/People - Nutzer/Personen

We use "Personen" instead of plural "Nutzer" for "people", as "Nutzer" stays
the same in plural.

*"Nutzer/Personen" (Transifex)*

## Other (Verschiedenes)

* You - **Du**

Why not "Sie"? In brief, Zulip and other web applications tend to use a rather
informal language. If you would like to read more about the reasoning behind
this, refer to the [general notes](general-notes.md#formal-or-informal) for
translating German.

*"Du" (Google, Facebook), "Sie" (Transifex)*

* We - **Wir** (rarely used)

German guides don't use "wir" very often - they tend to reformulate the
phrases instead.

*"Wir" (Google, Transifex)*

