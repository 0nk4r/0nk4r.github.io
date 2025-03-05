---
layout: post
date: '2024-10-26 13:03 -0700'
last_modified_at: '2024-10-26 13:03 -0700'
published: true
title: Python subprocess.Popen fails silently
tags:
  - python
---

If you are using python's `subprocess.Popen` with any of stdout/stderr as pipes, you need to regularly clear the output of those pipes else, python the command will be blocked silently. The default limit on this buffer is from system which you can read using `io.DEFAULT_BUFFER_SIZE`. You can increase this by setting your own value through `bufsize` param.

References

- <https://stackoverflow.com/a/3991132>