---
layout: post
title: 'Snippets: Homebrew'
date: 2020-03-08 04:01 +0000
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Productivity, Tools]
published: true
---

Useful snippets reference while using Homebrew the unofficial macos package
manager.

<!-- more -->

## Backup and Restore

```bash
# backup
# this command creates Brewfile which contains all your
# currently installed packages.
brew bundle dump

# restore
# in the directory containing Brewfile
brew bundle
```

## Uninstall everything

```bash
brew remove --force $(brew list) --ignore-dependencies
```

## List Installed packages

### creates a Brewfile with all packages and taps

```bash
brew bundle dump
```

### list all installed packages

```bash
brew list
```

### list only top level packages

```bash
brew leaves
```

## Cleanup

```bash
# remove old installation files
brew cleanup

# remove cache of currently installed packages
brew cleanup -s

# remove files older than $x days
brew cleanup --prune $x
```
