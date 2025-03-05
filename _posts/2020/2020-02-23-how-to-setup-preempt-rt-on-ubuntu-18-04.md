---
layout: post
title: How to setup PREEMPT RT on Ubuntu 18.04
date: 2020-02-23 06:11 +0000
last_modified_at: 2023-08-13 01:57:50 +0000
tags: [How To, Realtime, Robotics]
published: true
---

These are my notes on how to install install preempt_rt patch for linux kernel
on Ubuntu 18.04. I am doing this for a robot control application where
non-determinism can cause damage to life or property. I will be writing more
blog posts about real time implementation for robotic applications.

<!-- more -->

We will be installing RT-PREEMPT kernel on ubuntu 18.04. Kernel version I am
choosing is 5.4 since it is the latest LTS release.

**NOTE**: <https://ubuntu.com/blog/real-time-ubuntu-is-now-generally-available>

## Install Dependencies

Install compilers required for building the kernel

```bash
sudo apt install build-essential git libssl-dev libelf-dev
```

## Download and patch

Download the `linux-5.4.17` kernel from [kernel.org](http://kernel.org) and the
rt patch

```bash
wget https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-5.4.19.tar.xz
wget https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/5.4/patch-5.4.19-rt11.patch.xz
```

Extract the archive and apply the patch

```bash
xz -cd linux-5.4.19.tar.xz | tar xvf -
cd linux-5.4.19
xzcat ../patch-5.4.19-rt11.patch.xz | patch -p1
```

## Configuration

copy over your old config and use that to configure your new kernel

```bash
kautilya@johnny-5:~/factory/linux-5.4.19/ > cp /boot/config-5.3.0-40-generic .config
kautilya@johnny-5:~/factory/linux-5.4.19/ > make oldconfig
```

when asked for Preemption Model, select the option "Fully Preemptible Kernel"
and accept the default value for the rest.

Alternatively, you could use the graphical interface to configure it using
menuconfig.

menuconfig requires flex and bison dependencies

```bash
sudo apt install flex bison
```

open config editor using

```bash
make menuconfig
```

search for `PREEMPT_RT` and set it to "Fully Preemptible Kernel (RT)".

## Build and Install

Build the kernel as a debian package using make command

```bash
$ make -j8 deb-pkg
...

$ sudo dpkg -i ../linux-headers-5.4.19-rt11_5.4.19-rt11-1_amd64.deb ../linux-image-5.4.19-rt11_5.4.19-rt11-1_amd64.deb ../linux-libc-dev_5.4.19-rt11-1_amd64.deb
...
```

## Verification

Reboot your system and check the kernel. It should show `PREEMPT_RT`

```bash
kautilya@johnny-5:~/factory/linux-5.4.19/ > uname -a
Linux johnny-5 5.4.19-rt11 #1 SMP PREEMPT_RT Fri Feb 21 12:54:56 PST 2020 x86_64 x86_64 x86_64 GNU/Linux
```

## Additional Configuration

### Security settings

Add your user to `realtime` group

```bash
$ sudo groupadd realtime
...

$ sudo usermod -aG realtime $USER
...
```

add the following to `/etc/security/limits.d/99-realtime.conf`

```bash
$ sudo nano /etc/security/limits.d/99-realtime.conf

@realtime soft rtprio 99
@realtime soft priority 99
@realtime soft memlock 102400
@realtime hard rtprio 99
@realtime hard priority 99
@realtime hard memlock 102400
```

### CPU Scaling

disable cpu scaling by setting the cpu governer to `performance` using
cpufrequtils.

```bash
$ sudo apt install cpufrequtils
...
```

Check the available cpufreq governers using `cpufreq-info`, in my case they
were performance and powersave

```bash
kautilya@johnny-5:~/ > cpufreq-info
cpufrequtils 008: cpufreq-info (C) Dominik Brodowski 2004-2009
Report errors and bugs to cpufreq@vger.kernel.org, please.
analyzing CPU 0:
    driver: intel_pstate
    CPUs which run at the same hardware frequency: 0
    CPUs which need to have their frequency coordinated by software: 0
    maximum transition latency: 4294.55 ms.
    hardware limits: 800 MHz - 4.60 GHz
    available cpufreq governors: performance, powersave
    current policy: frequency should be within 800 MHz and 4.60 GHz.
                    The governor "performance" may decide which speed to use
                    within this range.
    current CPU frequency is 4.40 GHz.
```

set the cpu frequency to performance using the following

```bash
$ sudo systemctl disable ondemand
...

$ sudo systemctl enable cpufrequtils
...

$ sudo sh -c 'echo "GOVERNOR=performance" > /etc/default/cpufrequtils'
...

$ sudo systemctl daemon-reload && sudo systemctl restart cpufrequtils
...
```

### CPU Partitioning

I want to run a few programs that do not have a low latency requirements and
would like to isolate them from the real time programs. For this, I am going to
partition 2 of my 4 CPU cores to real time and other 2 to non realtime.

You can also set exclusively which CPU your program runs on by setting its
CPU affinity.


### Additional References

- [https://rt.wiki.kernel.org/index.php/HOWTO:_Build_an_RT-application](https://rt.wiki.kernel.org/index.php/HOWTO:_Build_an_RT-application)
- [https://elinux.org/RT-Preempt_Tutorial](https://elinux.org/RT-Preempt_Tutorial)
- [https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/](https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/)
- [https://rt.wiki.kernel.org/index.php/Frequently_Asked_Questions](https://rt.wiki.kernel.org/index.php/Frequently_Asked_Questions)
- [http://www.staroceans.org/kernel-and-driver/Embedded Linux System Design and Development.pdf](http://www.staroceans.org/kernel-and-driver/Embedded%20Linux%20System%20Design%20and%20Development.pdf)
- [http://linuxrealtime.org/index.php/Main_Page](http://linuxrealtime.org/index.php/Main_Page)
- [https://wiki.archlinux.org/index.php/Realtime_kernel_patchset](https://wiki.archlinux.org/index.php/Realtime_kernel_patchset)
- [https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html](https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html)
- [https://computing.llnl.gov/tutorials/pthreads/](https://computing.llnl.gov/tutorials/pthreads/)
- [https://www.cs.auckland.ac.nz/references/unix/digital/APS33DTE/DOCU_002.HTM](https://www.cs.auckland.ac.nz/references/unix/digital/APS33DTE/DOCU_002.HTM)
- [https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base](https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base)
- [https://github.com/OpenEtherCATsociety/SOEM/issues/171](https://github.com/OpenEtherCATsociety/SOEM/issues/171)
- [https://github.com/machines-in-motion/real_time_tools/blob/master/src/timer.cpp](https://github.com/machines-in-motion/real_time_tools/blob/master/src/timer.cpp)

- [https://github.com/machines-in-motion/ubuntu_installation_scripts](https://github.com/machines-in-motion/ubuntu_installation_scripts)
- [https://github.com/mikekaram/ether_ros](https://github.com/mikekaram/ether_ros)
- [https://index.ros.org/doc/ros2/Tutorials/Building-Realtime-rt_preempt-kernel-for-ROS-2/](https://index.ros.org/doc/ros2/Tutorials/Building-Realtime-rt_preempt-kernel-for-ROS-2/)

- [https://index.ros.org/doc/ros2/Tutorials/Building-Realtime-rt_preempt-kernel-for-ROS-2/](https://index.ros.org/doc/ros2/Tutorials/Building-Realtime-rt_preempt-kernel-for-ROS-2/)
- [https://index.ros.org/doc/ros2/Tutorials/Intra-Process-Communication/](https://index.ros.org/doc/ros2/Tutorials/Intra-Process-Communication/)
- [https://index.ros.org/doc/ros2/Tutorials/Allocator-Template-Tutorial/](https://index.ros.org/doc/ros2/Tutorials/Allocator-Template-Tutorial/)
- [https://index.ros.org/doc/ros2/Tutorials/Real-Time-Programming/](https://index.ros.org/doc/ros2/Tutorials/Real-Time-Programming/)
- [http://design.ros2.org/articles/realtime_background.html](http://design.ros2.org/articles/realtime_background.html)
- [https://github.com/machines-in-motion/real_time_tools](https://github.com/machines-in-motion/real_time_tools)
- [https://elinux.org/Main_Page](https://elinux.org/Main_Page)
- [http://www.cs.utah.edu/~regehr/hourglass/](http://www.cs.utah.edu/~regehr/hourglass/)
- [https://wiki.archlinux.org/index.php/Realtime_kernel_patchset](https://wiki.archlinux.org/index.php/Realtime_kernel_patchset)
- [https://pdfs.semanticscholar.org/54e4/34dde5fefd1bf54c22574cac20469f48184b.pdf](https://pdfs.semanticscholar.org/54e4/34dde5fefd1bf54c22574cac20469f48184b.pdf)
- [https://www.linuxfoundation.org/blog/2013/03/intro-to-real-time-linux-for-embedded-developers/](https://www.linuxfoundation.org/blog/2013/03/intro-to-real-time-linux-for-embedded-developers/)
- [https://rt.wiki.kernel.org/index.php/RT_PREEMPT_HOWTO](https://rt.wiki.kernel.org/index.php/RT_PREEMPT_HOWTO)
- [https://hackernoon.com/real-time-linux-communications-2faabf31cf5e](https://hackernoon.com/real-time-linux-communications-2faabf31cf5e)
- [http://www.best-of-robotics.org/wiki/images/1/18/FRI_Brics_2010_07_19.pdf](http://www.best-of-robotics.org/wiki/images/1/18/FRI_Brics_2010_07_19.pdf)
- [https://wiki.linuxfoundation.org/realtime/rtl/blog#guest-blog-post-from-bmw-car-itreal-time-linux-continues-its-way-to-main-line-development-and-beyond](https://wiki.linuxfoundation.org/realtime/rtl/blog#guest-blog-post-from-bmw-car-itreal-time-linux-continues-its-way-to-main-line-development-and-beyond)
- [https://rt.wiki.kernel.org/index.php/Main_Page](https://rt.wiki.kernel.org/index.php/Main_Page)
- [https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/preemptrt_setup](https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/preemptrt_setup)
- [https://www.kernel.org/doc/Documentation/kbuild/kconfig.txt](https://www.kernel.org/doc/Documentation/kbuild/kconfig.txt)
- [https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/](https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/)
- [https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base](https://wiki.linuxfoundation.org/realtime/documentation/howto/applications/application_base)
- [https://elinux.org/RT-Preempt_Tutorial](https://elinux.org/RT-Preempt_Tutorial)
- [http://www.armadeus.org/wiki/index.php?title=Preempt-rt](http://www.armadeus.org/wiki/index.php?title=Preempt-rt)
- [https://www.osadl.org/fileadmin/events/rtlws-2007/Sampath.pdf](https://www.osadl.org/fileadmin/events/rtlws-2007/Sampath.pdf)
- [https://hackernoon.com/towards-a-distributed-and-real-time-framework-for-robots-469ba77d6c42](https://hackernoon.com/towards-a-distributed-and-real-time-framework-for-robots-469ba77d6c42)
- [https://hackernoon.com/@vmayoral](https://hackernoon.com/@vmayoral)
- [https://ennerf.github.io/2016/09/20/A-Practical-Look-at-Latency-in-Robotics-The-Importance-of-Metrics-and-Operating-Systems.html](https://ennerf.github.io/2016/09/20/A-Practical-Look-at-Latency-in-Robotics-The-Importance-of-Metrics-and-Operating-Systems.html)
- [https://blog.cloudflare.com/how-to-achieve-low-latency/amp/](https://blog.cloudflare.com/how-to-achieve-low-latency/amp/)
- [https://gist.github.com/ennerf/0ddc4396d15852d28e4eca4a8a923eb7](https://gist.github.com/ennerf/0ddc4396d15852d28e4eca4a8a923eb7)
- [https://gist.github.com/ennerf/36a57d432bcff20a58efcdee10f91bd9](https://gist.github.com/ennerf/36a57d432bcff20a58efcdee10f91bd9)
- [https://gist.github.com/ennerf/45809ef405a4a56a285b](https://gist.github.com/ennerf/45809ef405a4a56a285b)
- [https://gist.github.com/ennerf/7d59a9765da25ed7c02117da1805551c](https://gist.github.com/ennerf/7d59a9765da25ed7c02117da1805551c)
- [https://gist.github.com/ennerf/b349c56d320da1db89b298fd807f00e4](https://gist.github.com/ennerf/b349c56d320da1db89b298fd807f00e4)
- [https://github.com/giltene/jHiccup](https://github.com/giltene/jHiccup)
- [https://github.com/LatencyUtils/LatencyUtils](https://github.com/LatencyUtils/LatencyUtils)
- [https://github.com/leandromoreira/linux-network-performance-parameters](https://github.com/leandromoreira/linux-network-performance-parameters)
- [https://github.com/OpenEtherCATsociety/SOEM/issues/330](https://github.com/OpenEtherCATsociety/SOEM/issues/330)

