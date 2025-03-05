---
layout: default
title: Art
tags: [page]
layout: null
redirect_to:
  - https://kautilya.art
---

Rules

1. Don't end the week with nothing
2. Canvas size must be square
3. Any image is art

If I keep this up for 100 days, I will buy myself a [pen plotter](https://shop.evilmadscientist.com/productsmenu/846)

{% for post in site.posts %}
{% if post.tags contains "art" %}
  <article class="post">
  <li>
      <p>
      <a href="{{ post.url }}">{{ post.title }}</a>
      </p>
  </li>
  </article>
{% endif %}
{% endfor %}
