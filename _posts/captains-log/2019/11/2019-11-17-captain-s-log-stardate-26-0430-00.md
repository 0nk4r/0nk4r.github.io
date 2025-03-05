---
layout: post
title: Captain's log, stardate [-26]0430.00
date: 2019-11-17 12:00 -0800
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Captain's log, weekly]
---

This week in review: testing and debugging across the stack, early and late
binding, GNU Parallel!

<!-- more -->

### Mon, 18 Nov 2019

`vstest.console.exe` is a great tool to run tests from the command line. I have
been using this to automate some of my workflows. The command line arguments
are a little cumbersome. One option that I found useful was `/TestCaseFilter1`.
This option can be used to run specific tests by substring search and filter.
For example,

```Batchfile
vstest.console.exe bin\Release\MyTests.dll /TestCaseFilter:"(FullyQualifiedName~ProdTest)|(FullyQualifiedName~DevTest.SALT)"
```
{: .code-wrap}

More information about the options and usage can be found at [^1] and [^2].  
▣

Debugging on Linux[^3] [^7] [^8]

`ldd` is short for list dynamic dependencies which does exactly that, it lists
all the dynamic libraries that your program/library depends on. It is useful to
debug symbol not found errors. Also check `LD_LIBRARY_PATH` if you get this
type of errors.

`strace` lists all system calls a program makes till it stops

`ltrace` lists all library calls a program makes till it stops

`nm` lists symbols from object files  
▣

Real world applications that use popular algorithms[^4]  
▣

### Tue, 19 Nov 2019

Tia Newhall's[^5] CS and Unix Links page contains a lot of useful
resources for working with the Unix OS.  
▣

Early binding vs Late Binding

Binding is the process of converting identifiers[^6] into addresses.
Binding for functions occurs either during compile time or runtime.

Early binding or compile time polymorphism is when the function call is resolved
during compile time. This is done using overloading of functions or operators.

Late binding or runtime polymorphism is when the function call is resolved at
runtime of the program. This is done using virtual functions.  
▣

### Wed, 20 Nov 2019

GNU Parallel

```bash
find . -name '*.dat' | parallel -j8 python ./process_dat.py {} \;
```

▣

[^1]: <https://docs.microsoft.com/en-us/visualstudio/test/vstest-console-options?view=vs-2019>
[^2]: <https://blogs.msdn.microsoft.com/vikramagrawal/2012/07/23/running-selective-unit-tests-in-vs-2012-rc-using-testcasefilter/>
[^3]: <https://www.cs.swarthmore.edu/~newhall/unixhelp/debuggingtips_C++.html>
[^4]: <https://cstheory.stackexchange.com/questions/19759/core-algorithms-deployed/19773#19773>
[^5]: <https://www.cs.swarthmore.edu/~newhall/unixlinks.html>
[^6]: <https://en.cppreference.com/w/cpp/language/identifiers>
[^7]: <https://www.cs.swarthmore.edu/~newhall/unixhelp/compilecycle.html>
[^8]: <https://www.cs.swarthmore.edu/~newhall/unixhelp/binaryfiles.html>
