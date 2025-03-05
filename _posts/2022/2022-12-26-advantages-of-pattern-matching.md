---
layout: post
title: Advantages of Pattern Matching
date: 2022-12-26 08:21 +0000
last_modified_at: 2024-06-23 21:55:25 +0000
tags: [rust, link]
published: true
external-url: https://web.archive.org/web/20201109043148/http://fsharpnews.blogspot.com/2009/08/advantages-of-pattern-matching.html
---

I was discussing with a friend earlier today about the need for pattern matching
and I remembered this particular blog that I read few years ago.

> - Pattern matches can act upon ints, floats, strings and other types as well as objects. Method dispatch requires an object.
> - Pattern matches can act upon several different values simultaneously: parallel pattern matching. Method dispatch is limited to the single this case in mainstream languages.
> -Patterns can be nested, allowing dispatch over trees of arbitrary depth. Method dispatch is limited to the non-nested case.
> - Or-patterns allow subpatterns to be shared. Method dispatch only allows sharing when methods are from classes that happen to share a base class. Otherwise you must manually factor out the commonality into a separate member (giving it a name) and then manually insert calls from all appropriate places to this superfluous function.
> - Pattern matching provides exhaustiveness and redundancy checking which catches many errors and is particularly useful when types evolve during development. Object orientation provides exhaustiveness checking (interface implementations must implement all members) but not redundancy checking.
> - Non-trivial parallel pattern matches are optimized for you by the F# compiler. Method dispatch does not convey enough information to the compiler's optimizer so comparable performance can only be achieved in other mainstream languages by painstakingly optimizing the decision tree by hand, resulting in unmaintainable code.
> - Active patterns allow you to inject custom dispatch semantics.

