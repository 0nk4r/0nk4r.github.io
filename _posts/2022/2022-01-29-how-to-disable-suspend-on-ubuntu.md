---
layout: post
title: How to disable suspend on Ubuntu
date: 2022-01-29 21:55 +0000
last_modified_at: 
tags: [linux, How To]
published: true
---

Whenever my laptop wakes from suspend, wifi stops working. I could restart
the network manager using `sudo service network-manager restart` but I ran 
into issues with VPN or the DNS. I decided to just disable suspend permanently.

I did a couple of differnt things to disable suspend. I am not sure which one
finally worked but I am just listing them here as a note to self.

### Gnome Tweak Tool

Gnome tweak tool has an option to disable suspend when lid is closed.
Install and run it using the following command.

```bash
sudo apt install gnome-tweaks
gnome-tweaks
```

Turn off `suspend when laptop lid is closed` option.


### logind.conf

Ignore lid close in logind

```bash
sudo nano /etc/systemd/logind.conf
```

and change `HandleLidSwitch` to `ignore`. Restart systemd-logind.

```bash
sudo systemctl restart systemd-logind
```

### UPower.conf

Edit the `Upower.conf` to change the `ignoreLid` to `true`

```bash
sudo nano /etc/UPower/UPower.conf
```

and then restart 

```bash
sudo service upower restart
```
