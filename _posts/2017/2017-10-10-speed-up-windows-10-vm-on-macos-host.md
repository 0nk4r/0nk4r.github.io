---
layout: post
title: Speed up Windows 10 VM on macOS host
date: 2017-10-10
tags: [Tools]
---

While using Windows 10 Guest on macOS host, I found that Windows was running
really slow. I first tried increasing the RAM to 6GB but there was no
significant improvement in performance. I started tweaking a few settings and
found that enabling 2D and 3D acceleration results in significant performance
improvements.
<!-- more -->
![VM Settings](/assets/images/20171010/windows10vm.png)
