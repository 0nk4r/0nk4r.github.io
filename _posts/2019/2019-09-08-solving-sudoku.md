---
layout: post
title: Solving Sudoku
date: 2019-09-08 00:36 -0700
tags: [Optimization, Maths]
mathjax: true
---

Sudoku is a simple/easy to define problem. You have a 9 x 9 grid
and you have to fill the numbers 1 to 9 in such a way that no number is
repeated in any row, column, or sub grid. This problem has been explored by a
number of people in a number of different ways. Most popular of them all is
Peter Norvig's [Solving Every Sudoku Puzzle](https://norvig.com/sudoku.html).

<!-- more -->

Sudoku is a [Constraint Satisfaction
Problem (CSP)](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem).
Most popular techniques for solving a CSP are Backtracking, Constraint
Propagation and Search. In this post, we will explore solving Sudoku as a
Mixed-Integer Programming problem using CVXPY. We will also use a SAT Solver to
solve the problem.

In the MIP method, we use a dummy objective function to trick the solver
into satisfying the constraints.

A SAT Solver is designed for problems like this. SAT is short for
`SATISFYABILITY` or Boolean satisfiability problem.

### Sudoku as MIP


### Sudoku as SAT Problem

### References
[http://profs.sci.univr.it/~rrizzi/classes/PLS2015/sudoku/doc/497_Olszowy_Wiktor_Sudoku.pdf](http://profs.sci.univr.it/~rrizzi/classes/PLS2015/sudoku/doc/497_Olszowy_Wiktor_Sudoku.pdf)
- [https://towardsdatascience.com/using-integer-linear-programming-to-solve-sudoku-puzzles-15e9d2a70baa](https://towardsdatascience.com/using-integer-linear-programming-to-solve-sudoku-puzzles-15e9d2a70baa)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2019/08/finding-central-point-in-point-cloud.html](http://yetanothermathprogrammingconsultant.blogspot.com/2019/08/finding-central-point-in-point-cloud.html)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2018/08/sudoku.html](http://yetanothermathprogrammingconsultant.blogspot.com/2018/08/sudoku.html)
- [https://yetanothermathprogrammingconsultant.blogspot.com/2016/10/mip-modeling-from-sudoku-to-kenken.html](https://yetanothermathprogrammingconsultant.blogspot.com/2016/10/mip-modeling-from-sudoku-to-kenken.html)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2019/01/presolving-killer-sudokus.html](http://yetanothermathprogrammingconsultant.blogspot.com/2019/01/presolving-killer-sudokus.html)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2019/02/the-8-queens-problem-without-binary.html](http://yetanothermathprogrammingconsultant.blogspot.com/2019/02/the-8-queens-problem-without-binary.html)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2018/11/chess-and-solution-pool.html](http://yetanothermathprogrammingconsultant.blogspot.com/2018/11/chess-and-solution-pool.html)
- [http://yetanothermathprogrammingconsultant.blogspot.com/2019/06/assignment-scipy-vs-cplex.html](http://yetanothermathprogrammingconsultant.blogspot.com/2019/06/assignment-scipy-vs-cplex.html)