---
layout: post
title: How to fix _wait_for_tstate_lock
date: 2022-12-14 08:19 +0000
last_modified_at: 2023-08-13 01:57:50 +0000
tags: [python, How To]
published: true
---

If we ever try to exit server with objects in the Multiprocessing Queue, we could
end up in a race condition that causes a deadlock with `_wait_for_tstate_lock`.
One way to avoid it is to clear the queue before exit.

### Debugging
To figure out which queue is not empty,

```python
import multiprocessing
import inspect

# initialize a queue
q = multiprocessing.Queue(10)

# get function where the queue is created or where we are adding objects to queue
# so that we can identify which queue it is
caller = inspect.getframeinfo(inspect.stack()[1][0])
thread_name = f"MultiQueue_{caller.filename}:{caller.lineno}"

# add new object
q.put("hello")

# set thread name
q._thread.name = thread_name
```

`QueueFeederThread` is stared after you put an object into the queue.
After the first time you put an object into the queue, you can set a name to the thread.
You can then use `py-spy` to figure out which thread is preventing your program from exiting.

```bash
py-spy dump -p <pid>
```

### References

- <https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues>

