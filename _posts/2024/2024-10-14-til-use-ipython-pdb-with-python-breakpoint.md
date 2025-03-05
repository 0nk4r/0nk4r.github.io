---
layout: post
date: '2024-10-14 18:04 -0700'
last_modified_at: '2024-10-14 18:04 -0700'
published: true
title: 'TIL: Use IPython PDB with python breakpoint()'
tags:
  - TIL
  - python
---

Often when I am debugging python code, I like to sprinkle around `breakpoint()` to quickly evaluate statements or print values. By default, `breakpoint()` drops you into python pdb repl. Python pdb is great but it lacks snazzy features like multi line editing, history, syntax highlighting and autocomplete.

I recently found that you can override the default repl that `breakpoint()` executes by setting the environment variable `PYTHONBREAKPOINT`. 

To setup python breakpoint to use ipdb, add `export PYTHONBREAKPOINT="ipdb.set_trace` to your 	`.bashrc` or `.zshrc`. 

