---
layout: post
title: How to build reliable Software
date: 2024-01-13 06:33 +0000
last_modified_at: 2024-05-26 21:57:26 +0000
tags: [systems]
published: true
external-url: https://martin-thoma.com/reliable-software/
---

> NSI/IEEE 1991 defines reliability as "the probability of failure-free software operation for a specified period of time in a specified environment". That sounds pretty much like my definition of availability.

### Notes

- Ensure every branch of your code is tested
- Ensure all exceptions are caught and properly handled
- Prefer `Result<T, E>` over `Option<T>` for error handling

