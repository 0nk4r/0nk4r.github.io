---
layout: post
title: MSYS2 - Fix Slow Startup
date: 2019-09-11 15:41 -0700
tags: [Link, Windows]
external-url: http://bjg.io/guide/cygwin-ad/
---

I am currently using an MSYS2 installation instead of Git for Windows. I chose
MSYS2 because it comes with pacman and am able to use other familiar tools like
vim, awk and grep. I noticed that my MSYS2 startup is really slow. Googling it
brought up the above link which explains the problem is a great detail and
gives you a good solution. I am posting the link here for reference.

1. Create `/etc/passwd` and `/etc/group`
2. modify `/etc/nsswitch.conf` to use only file

This prevents MSYS2 to query Active Directory for login information.

```bash
mkpasswd -l -c > /etc/passwd
mkgroup -l -c > /etc/group
sed -i '/^passwd:/ s/.*/passwd:         files/' /etc/nsswitch.conf
sed -i '/^group:/ s/.*/group:          files/' /etc/nsswitch.conf
```
