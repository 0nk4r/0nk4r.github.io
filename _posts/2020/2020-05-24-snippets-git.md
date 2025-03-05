---
layout: post
title: 'Snippets: Git'
date: 2020-05-24 16:30 +0000
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Productivity, Tools]
published: true
---

Snippets that make my life little bit easier while working with Git.

Here's a list of Git puns

"Git on with it"

"A little Git of everything!"

"The Git that keeps on giving."

<!-- more -->

## Working with remote

When you have a fork of a repository, you might want to sync it with one another.
This can be done using git remotes

```bash
# list all remotes
git remote -v

# change remote url
git remote set-url <name of remote> <new url>

# Add new remote url
git remote add <name of remote> <url>

# rename remote
git remote rename <old name> <new name>

```
