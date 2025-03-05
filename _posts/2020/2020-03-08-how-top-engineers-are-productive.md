---
layout: post
title: How Top Engineers Are Productive
date: 2020-03-08 03:27 +0000
last_modified_at: 2024-06-23 21:55:25 +0000
tags: [Productivity, Link]
published: true
external-url: https://news.ycombinator.com/item?id=21870889
---

These are some of the comments I found interesting on HN. I am reproducing them
here as a reference for myself.

<!-- more -->

## ericb

* Better googling. Time-restricted, url restricted, site restricted searches.
  Search with the variant parts of error messages removed.
* Read the source of upstream dependencies. Fix or fork them if needed.
* They're better at finding forks with solutions and gleaning hints from
  semi-related issues.
* Formulate more creative hypothesis when obvious lines of investigation run
  out. The best don't give up.
* Dig in to problems with more angles of investigation.
* Have more tools in their tool-belt for debugging like adding logging,
  monkey-patching, swapping parts out, crippling areas to rule things out,
  binary search of affected code areas.
* Consider the business.
* Consider user-behavior.
* Assume hostile users (security-wise).
* Understand that the UI is not a security layer. Anything you can do with
  PostMan your backend should handle.
* Whitelist style-security over blacklist style.
* See eventual problems implied by various solutions.
* "The Math."

## stickfigure

I boil it down to two things:

* **Rapidly Climb Learning Curves**

  The ability to quickly learn enough about new subjects to be useful. New
  technologies or APIs; new algorithms; mathematical or statistical subjects;
  and most importantly, your problem domain. Some of this ability is a skill,
  "knowing how to learn", which covers google-fu, reading comprehension,
  prioritization, time management, etc. Some of this ability comes from having
  enough aggregate experience that new information just clicks into place like
  jigsaw puzzle pieces. Some of this ability comes from the confidence of having
  climbed enough seemingly insurmountable learning curves that this next one is
  "just another day at the office".

  A sign you're doing this wrong: "I need training!"

* **Understand The Customer**

  IMHO, the best engineers are half product managers. You can easily get a 10X
  improvement in productivity by building the right features and not building the
  wrong ones. Yes, professional product managers are great, but technical
  limitations often impact product design. A great engineer knows when to push
  back or suggest alternatives. This requires empathy not only for the customer,
  but for the product management team. This ability is also tightly coupled with
  #1 - you need to quickly come up to speed on the problem domain, whatever that
  may be. If you wan't to be a great engineer, don't study algorithms (until you
  need an algorithm, of course), study the particular business that you're in.

  A sign you're doing this wrong: "Whatever, just tell me how you want it and
  I'll make it that way!"

## tetek

* Don't bitch about legacy software
* Are willing to help with getting proper requirements
* Don't need a JIRA task for everything
* Don't say they are done if something is untestable
* Are willing to do stuff other than their skill (eg. one of the graphics
  required for the project is too big, top engineer opens up gimp, resizes and
  continue. Bad engineer will report to manager that design team did shitty job,
  reassign JIRA ticket, write two emails and wait for new a graphic)
* Top programmers deliver well packed, documented software, keep repository
clean with easy setup steps accessible for everyone.
* Top engineers enjoy what they do, and are making the project enjoyable for
everyone, keep high morales and claim responsibility

## honkycat

* NEVER practice Coincidence driven development.

  If you get lost, and no longer know why something is not working, do not just
  keep fiddling and changing things.

  Simplify the problem. Disable all confounding variables and observe your
  changes. Open up a repl and try to reproduce the issue in your repl.

  Read the source code of your dependencies. I have seen this a lot: People
  fiddle with dependencies trying to get them to work. Crack the code open and
  read it.

* Choose your battles. Not every hill can be the one you die on. You cannot
  control every part of a code-base when you are working on a team. People are
  going to move your cheese and you need to learn to not let that affect you.

* Learn to lose. Similar to the last one. Treat technical discussions as
  discussions, not a competition. Use neutral language that frames your ideas as
  NOT your ideas, but just other options. Keep an open mind and let the best
  idea win.

* Write tests. There are outliers here, but the majority of talented engineers
  I have worked with are all on the same page: If you don't have tests, you cannot
  safely refactor your code[^1]. If you cannot safely refactor your code, you
  cannot improve your codebase. If you cannot improve your codebase, it turns to
  mush.

* Simplicity is golden. Keep your projects simple, doing the bare minimum of
  what you need, and do not refer to your crystal ball for what you might need
  later. Single responsibility principle. Keep your Modules and your functions
  simple and small, and combine them to create more complicated behavior.

* Quit shitty jobs. If you are not learning at a job, or they are abusing you,
  you need to get the hell out of there. Burn-out is real. Burn out on something
  cool that helps YOU, not pointless toil for some corporate overlord.

## kthejoker2

I can't recommend Gary Klein's Sources of Power enough, it is stuffed with
awesome mental models, real life parables, research findings, and one quotable
passage after another on expert decision making.

From the book, things experts do more/better/faster/etc than novices.

* Identify patterns faster and successfully predict future events more often.
* Recognize anomalies - especially negative anomalies i.e. something didn't
  happen that should - quickly and take appropriate actions.
* Identify leverage points within their architecture to solve new problems and
  deliver new features faster and with less effort.
* Make finer discriminations of events and data, at a level of detail novices
  don't consider.
* Understand the tradeoffs and consequences of an option.
* (I like this one) Recognize expertise in others and defer as many decisions
  as possible to that expertise.
* Their ability to "context switch" when describing a situation to other experts
  vs novices vs non-participants.

And one that's not explicitly from the book but is contained in its wisdom:

* Skate where the puck is going, not where it is.

[^1]: Martin Fowler's Refactoring 2nd edition
