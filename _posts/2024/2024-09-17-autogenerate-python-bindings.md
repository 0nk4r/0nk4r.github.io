---
layout: post
date: '2024-09-17 18:12 -0700'
last_modified_at: '2024-09-17 18:12 -0700'
published: true
title: Autogenerate Python bindings
tags:
  - python
---

We have been writing a lot of python bindings for C++ code at work. Someone asked me why we need to write a lot of boilerplate code in pybind11 to create these python bindings. I personally prefer the level of configurability that pybind provides in the bindings. But it also made me think, a lot of the time my bindings are just the function name converted from CamelCase to snake_case. I went out to search for tools that automate this binding generation. I found two tools that seem to be actively maintained

1. [Binder](https://cppbinder.readthedocs.io/en/latest/index.html) 
> Binder is a tool for automatic generation of Python bindings for C++11 projects using Pybind11 and Clang LibTooling libraries. That is, Binder, takes a C++ project and compiles it into objects and functions that are all usable within Python. Binder is different from prior tools in that it handles special features new in C++11.

2. [litgen](https://pthom.github.io/litgen/litgen_book/00_00_intro.html)
> litgen, also known as Literate Generator, is an automatic python bindings generator for humans who like nice code and APIs.  
> It can be used to bind C++ libraries into documented and discoverable python modules using pybind11.  
> It can also be used as C++ transformation/refactoring tool.


I haven't tried these out but look very promising.
