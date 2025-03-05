---
layout: post
title: Few Puzzles and Their Analysis
date: 2014-08-30 17:55 +0530
last_modified_at: 2020-02-23 06:54:57 +0000
tags: [Puzzles]
mathjax: true
---

These are a few puzzles from IISC Summer School 2013 which I
accidentally stumbled up on. The original PDF can be found
[here](http://events.csa.iisc.ernet.in/summerschool2013/slides/problem-sheet.pdf "problem sheet").
There may be many other ways of solving the same problem so if you have
a better solution to the same problem do comment below and let me know.

<!-- more -->

### Puzzle 1
*You are given a basket of 80 identical balls, out of which all except
one have the same weight. What is the minimum number of times you will
have to use a given weighing balance before finding the odd ball in
the basket?*

Here we have to remember that they have not given if the defective ball
is lighter or heavier than the rest of the balls. So we have to find out
if the ball is heavier or lighter too! Lets split the balls into 3
sections say **A** = 30, **B** = 30, and **C** = 20 and weigh **A** and
**B** on the weighing balance. This is the first trail and has 3
different outcomes.

1.  Condition when **A** = **B** when **A** == **B** we can confirm that
    the defective ball isn't part of either **A** or **B**. Then we can
    go on and test the section **C** by splitting it further into three
    sections and repeat similar process. And finally when you arrive at
    two balls add them to a section of known balls and weigh them to
    find the one that isn't equal.

2.  Condition when **A** \> **B** or **A** \< **B** we need to first
    find which section has the defective ball, so we split **C** into
    two and add balls from **A** and **B** separately to form new
    sections. Since we know that the balls from section **C** do not
    contain the defective ball we can now shortlist the number of balls
    to be weighed from this step.

These two conditions can be looped to obtain the final answer. Based on
the solution provided by [Charles
Naumann](http://www.mathsisfun.com/puzzles/weighing-pool-balls-solution.html "Math is Fun"),
and the number of balls in our problem, there are almost 160 possible
correct combinations. This problem will be solved later in another post.

### Puzzle 2
*Find all integers $$x \neq y$$, such that $$x^y = y^x$$*

The solution is quite simple and can be obtained by trial and error
method. This condition is satisfied only for $$x = 2$$ & $$y = 4$$ or 
$$x = 4$$ & $$y = 2$$

### Puzzle 3
*You are given two identical eggs and have access to a 100-storey
building. If an egg does not break on being dropped from a given floor
of the building, it will survive a fall from all lower floors;
similarly, if an egg breaks on being dropped from a floor, it will
break when dropped from all higher floors. You are required to find
the highest floor from which an egg on being dropped will not break.
Note that an egg once broken cannot be reused; however, an egg which
survives a fall can be used again. What will be your strategy to find
a solution to this problem? Note that your strategy should require
minimum number of egg drops; if there are n floors, what will be the
number of egg drops required by your strategy in the worst case.*

When I first read this problem the first idea that struck me was a
binary tree. The idea was to first test it at half the height and if it
breaks the answer must be lower else its on the top half of the
building. The problem with this strategy was that there aren't enough
eggs to test it.The solution should use minimum number of eggs drops
using two eggs!

For this lets assume that we drop the egg on every 10th floor, so that
if the egg breaks on the 10th floor, we can start from the first floor
and drop the second egg at every floor from then on. This way we will
have a worst case number of drops as 19.

A better solution for this problem can be found
[here](http://datagenetics.com/blog/july22012/index.html "The Two Egg Problem")
where the worst case number of drops is just 14!
