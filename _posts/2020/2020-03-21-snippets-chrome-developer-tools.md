---
layout: post
title: 'Snippets: Chrome Developer Tools'
date: 2020-03-21 07:29 +0000
last_modified_at: 2020-03-21 08:10:25 +0000
tags: [Productivity, Tools]
published: true
---

Useful snippets reference while using Chrome Developer Tools.

<!-- more -->

I routinely find myself needing to extract a bunch of content from a website
and paste it in to google sheets. I use xpath in the console a lot for this.
The snippet below makes it easy to print all the data in one line so that I can
easily paste it into sheets and process the data.[^1]

```javascript
console.log($x('//<your xpath>').map(function(el){return el.data.trim()}).join("\n"))
```

[^1]: <https://stackoverflow.com/a/58923853>
