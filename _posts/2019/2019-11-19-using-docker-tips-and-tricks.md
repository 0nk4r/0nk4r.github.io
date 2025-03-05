---
layout: post
title: 'Using Docker: Tips and Tricks'
date: 2019-11-19 11:34 -0800
last_modified_at: 2020-02-23 06:54:57 +0000
tags: [Docker]
---

Docker jargon
- **Image** contains all the additional file changes required to run your
application. This is likely a union of your os files + your application files.
- **Container**
- **Docker Daemon**
- **Docker Client**
- **Docker Hub**
- **DockerFile**

Docker uses *Copy on Write* and *union file system* to optimize resource usage.
It uses Overlayfs filesystem architecture as one of the storage driver
to manage file changes[^1]. 

**Docker Compose** is a tool with which you can define multiple containers
that your application needs and launch all of them with one command.
For example, if your application has a HTTP Server, SQL Database, and a logging
framework, you can define all of them in separate containers and launch them
using Docker Compose.

[^1]: <https://jvns.ca/blog/2019/11/18/how-containers-work--overlayfs/>
