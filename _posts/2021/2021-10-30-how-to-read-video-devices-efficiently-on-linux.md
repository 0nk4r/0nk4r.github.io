---
layout: post
title: How to read video devices efficiently on Linux
date: 2021-10-30 18:54 +0000
last_modified_at: 2021-11-06 02:36:46 +0000
tags: [v4l2, VideoCapture, opencv, linux, How To]
published: false
---

Using OpenCV VideoCapture on linux uses very high cpu to fetch frames from 
video4linux2 devices and offers low frame rates. 

<!-- more -->

use imageio-ffmpeg instead

Install v4l-utils from apt

```
# to list all devices
v4l2-ctl --list-devices

# list all supported formats by this device
v4l2-ctl --device /dev/video0 --list-formats-ext

# same as above but through ffmpeg
ffmpeg -f v4l2 -list_formats all -i /dev/video0
```
