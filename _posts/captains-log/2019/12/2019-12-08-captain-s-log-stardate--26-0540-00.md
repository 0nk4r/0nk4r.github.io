---
layout: post
title: Captain's log, stardate [-26]0540.00
date: 2019-12-08 12:02:43 +0000
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Captain's log, weekly]
---

This week in review: Dynamically loading `*.so`, resolving local domains with
mDNS, Code Quality, and be kinder.

<!-- more -->

### Tue, 10 Dec 2019

When dynamically loading plug-in objects, create a dependency graph, find
the lowest common ancestor and start loading the objects from there. This
prevents objects failing to load due to unsatisfied dependencies.▣

If you are not able to resolve local hosts with `hostname.local`, you can try
removing `[NOTFOUND=continue]` from `/etc/nsswitch.conf`. This may or may not
help. This asks the mDNS resolver to quit if it cannot resolve.  
TODO: Lookup how Avahi daemon works.▣

### Fri, 13 Dec 2019

To maintain code quality, monitor 3 things

1. Readability
2. Buildability
3. Testability

This will help you avoid pain down the line. You must also think about
refactoring as part of your project planning.▣

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">WE ARE JUST THE WRECKED AND BROKEN TROJAN HORSES OF OUR DREAMS. That&#39;s how our dreams invade the cities.</p>&mdash; Robert Montgomery (@MontgomeryGhost) <a href="https://twitter.com/MontgomeryGhost/status/426810086242414593">January 24, 2014</a></blockquote>
<!-- <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> -->

I saw this quote earlier today and it seemed interesting. I can't disagree
with this, my dreams have significantly diverged from my life right now.▣

### Sat, 14 Dec 2019

Interesting list of projects to try out[^1]. I am particularly interested in the
compiler - Tiny BASIC and mini operating system ones.▣

My version of The Joel Test[^2]

1. Do you use version control?
2. Can you make a build in one step and are use a CI system?
3. Do you use an Issue tracking system?
4. Do you fix existing bugs before writing new code?
5. Do you have an up to date schedule?
6. Do you have a spec?
7. Do you use the best tools money can buy?
8. Do new candidates write code during interview?

This is not an exhaustive list. I am still trying to understand what is important
for different types of teams. This core list might be valid for all but you might
need additional tests for a team working on frontend development or a team
building a compiler.▣

<blockquote><p>Be kinder to yourself</p>&mdash; magsheer</blockquote>

[^1]: <http://web.eecs.utk.edu/~azh/blog/challengingprojects.html>
[^2]: <https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/>
