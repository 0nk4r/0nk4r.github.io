---
layout: post
title: Thats one way of thinking about Garbage Collection
date: 2020-02-22 19:11 +0000
last_modified_at: 2024-06-23 21:55:25 +0000
tags: [Link, Tech]
published: true
external-url: https://groups.google.com/forum/message/raw?msg=comp.lang.ada/E9bNCvDQ12k/1tezW24ZxdAJ
---

> I was once working with a
> customer who was producing on-board software for a missile.  In my analysis
> of the code, I pointed out that they had a number of problems with storage
> leaks.  Imagine my surprise when the customers chief software engineer said
> "Of course it leaks".  He went on to point out that they had calculated the
> amount of memory the application would leak in the total possible flight time
> for the missile and then doubled that number.  They added this much
> additional memory to the hardware to "support" the leaks.  Since the missile
> will explode when it hits it's target or at the end of it's flight, the
> ultimate in garbage collection is performed without programmer intervention.
> <footer>Kent Mitchell</footer>

As long as the system is reasonably deterministic, I guess it doesn't matter,
since the application calls for eventual destruction of the memory.
