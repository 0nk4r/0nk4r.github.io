---
layout: post
title: Captain's log, stardate [-26]0785.00
date: 2020-01-26 12:02:44 +0000
last_modified_at: 2020-11-28 07:38:36 +0000
tags: [Captain's log, weekly]
---

This week in review: Real time communication and safety.

<!-- more -->

### Mon, 27 Jan 2020

TCP/IP protocol sucks if you want to do realtime communication.
▣

### Wed, 29 Jan 2020

Black Channel vs White Channel concepts for safety are two ideas of how to
implement a Safety system network.[^1] [^2] [^3]

In a Black Channel system, you assume that your medium of communication is not
safety rated and you perform additional checks at your application layer to
ensure data reliability. In a system like this, we can use regular network
hardware and treat it as a black box and perform error and data integrity checks
on the application side. This is a much more cost effective option and it is
the type of system a lot of safety system manufacturers use.

In a White Channel system, your entire system is safety rated, down to the last
coupler. This makes it very hard to design and a lot more expensive.▣

[^1]: <https://journals.sagepub.com/doi/pdf/10.1177/002029400704001003>
[^2]: <https://www.controlglobal.com/articles/2011/hiddennetwork1102/>
[^3]: <https://ez.analog.com/b/engineerzone-spotlight/posts/functional-safety-and-networking>
