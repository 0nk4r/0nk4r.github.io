---
layout: post
title: Docker CPU Isolation
date: 2022-09-11 02:26 +0000
last_modified_at: 
tags: [docker, linux]
published: true
---

I recently ran into an issue where I needed to run a docker container with realtime
priority but couldn't use isolcpus or PREEMPT-RT patch. You can use cgroups to isolate
a docker container to specific cores and prevent other processes from using that particular code.
This is different from cpu pinning where other processes can still use the core that the
process is pinned to. 


```bash
#!/usr/bin/env bash

# install cset
pip install git+https://github.com/lpechacek/cpuset.git future

# delete existing cgroup
cset set -d docker

# create a new cgroup with two cores
cset shield --userset=ur_executor --cpu 0,1  -k on

# tell docker to use system cgroup
/bin/cat <<EOF > /etc/docker/daemon.json
{
    "cgroup-parent": "system"
}
EOF

service docker restart

echo "SETUP SUCCESSFUL"
```

while running the docker container, add `--cgroup-parent=ur_executor` to isolate container
to `ur_executor` cgroup


I didn't end up using this method because it had a very high jitter. There could be some other
settings that could reduce jitter but haven't done a deep dive. [docker-realtime](https://github.com/2b-t/docker-realtime)

### References
- <https://www.codeblueprint.co.uk/2019/10/08/isolcpus-is-deprecated-kinda.html>
- <https://documentation.suse.com/sle-rt/15-SP2/single-html/SLE-RT-shielding/index.html>
- <https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/cpusets.html>
- <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch01>
- <https://manpages.ubuntu.com/manpages/xenial/man7/cpuset.7.html>
- <https://www.suse.com/c/cpu-isolation-introduction-part-1/>
- <https://stackoverflow.com/questions/11111852/how-to-shield-a-cpu-from-the-linux-scheduler-prevent-it-scheduling-threads-onto>
- <https://juliaci.github.io/BenchmarkTools.jl/dev/linuxtips/>
- <https://releases.llvm.org/7.0.1/docs/Benchmarking.html>
- <https://www.redhat.com/en/blog/world-domination-cgroups-part-1-cgroup-basics>
- <https://hasura.io/blog/decreasing-latency-noise-and-maximizing-performance-during-end-to-end-benchmarking/>
- <https://speakerdeck.com/kentatada/cpu-shielding-on-docker-and-kubernetes?slide=20>
- [CASE2020_Puck_Setup_ROS2_preprint.pdf](https://www.researchgate.net/publication/344842072_Distributed_and_Synchronized_Setup_towards_Real-Time_Robotic_Control_using_ROS2_on_Linux)
- <https://github.com/lpechacek/cpuset/blob/master/doc/tutorial.txt>
