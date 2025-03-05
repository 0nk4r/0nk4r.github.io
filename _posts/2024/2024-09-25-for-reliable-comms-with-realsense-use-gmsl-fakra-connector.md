---
layout: post
date: '2024-09-25 07:06 -0700'
last_modified_at: '2024-09-25 07:06 -0700'
published: true
title: 'For reliable comms with Realsense, use GMSL/FAKRA connector'
tags:
  - Robotics
external-url: ''
---

I have had a lot of trouble with the Realsense cameras over USB in the past. Lot of times it is connection drops due to vibration or bandwith saturation in the USB Bus. I recently found out about the FAKRA connector from a friend. I need to do more reading about this but looks like this could solve some of the issues I was seeing.

### References
- <https://www.intelrealsense.com/depth-camera-d457/>
- [Introducing the RealSense D457 GMSL/FAKRA stereo camera](https://github.com/IntelRealSense/librealsense/issues/10964)
- [A Comprehensive Guide to FAKRA Connectors](https://community.element14.com/technologies/experts/b/comprehensive-guides/posts/a-comprehensive-guide-to-fakra-connectors "A Comprehensive Guide to FAKRA Connectors")
