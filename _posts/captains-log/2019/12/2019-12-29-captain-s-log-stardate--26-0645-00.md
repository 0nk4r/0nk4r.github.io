---
layout: post
title: Captain's log, stardate [-26]0645.00
date: 2019-12-29 12:03:10 +0000
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Captain's log, weekly]
---

This week in review: decade is over, tmux and vscode, fools and fanatics.

<!-- more -->

### Tue, 31 Dec 2019

End of a Decade!

TODO: figure out what I did for the past 10 years.▣

### Thu, 02 Jan 2020

I use tmux in my workflow and recently have had to use VS Code as part of my
dev environment. VS Code injects couple of environment variables into the shell
to setup WSL server that talks to the windows native code editor. Since, I was
launching tmux at startup, I ran into the issue of tmux missing env variables
required for VS Code and its WSL server. Here is a hack I am currently using
to get around this issue.

```bash
if [[ -z "$TMUX" ]] ;then
    # get the id of a detached session
    ID="$( tmux ls | grep -vm1 attached | cut -d: -f1 )"
    if [[ "$TERM_PROGRAM" == "vscode" ]]; then
        tmux new-session -s vscode-$(date +%s)
    elif [[ -z "$ID" ]] ;then  # if not available create a new one
        tmux new-session
    else
        tmux attach-session -t "$ID"  # if available attach to it
    fi
fi
```

▣

<blockquote>
<p>The whole problem with the world is that fools and fanatics are always so
certain of themselves, and wiser people so full of doubts.</p>
&mdash; Bertrand Russell
</blockquote>

I've recently come to a self-realization that I often act as one of the "fools
and fanatics" by being overly confident in my views. I have been actively
trying to recognize this and have been trying to get better at listening.
I am hoping 2020 is the year of transformation. I am setting this as one of my
goals for the year.▣
