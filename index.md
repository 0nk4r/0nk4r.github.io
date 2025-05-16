---
layout: default
title: Home
---

## Onkar Koli

*Building resilient software with a quiet eye on the threat landscape.*

**Product Security Engineer**

I work at the quiet intersection of code and security — where thoughtful design meets unseen defenses.  
It’s less about locking things down, and more about building software that’s ready for the real world.

---

### Areas of Work
Exploring the security of anything that computes, connects, or occasionally combusts — from IoT to WTF, firmware to the cloud, and everything in between. Whether it blinks, boots, or just barely functions, I’m usually in there somewhere armed with curiosity, a slightly overworked debugger, and a deep need to ask: “What happens if I do this?” 

---

### Work

<div class="post-list-home">
{% for post in site.posts limit:3 %}
  <article class="post-item">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
    <p>{{ post.excerpt | strip_html | truncatewords: 35 }}</p>
  </article>
{% endfor %}
</div>

<p style="text-align: center; margin-top: 2rem;"><a href="/blog">View All Posts &rarr;</a></p>

---

## Connect

You can find me on:

**[LinkedIn](https://linkedin.com/in/0nk4r)**   **[GitHub](https://github.com/0nk4r)**   **[Email](mailto:contact@onkark.com)**

<style>
/* Add specific styles for home page elements if needed, 
   but prefer styles defined in default.html for consistency */
.post-list-home .post-item {
  margin-bottom: 2.5rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  background: var(--code-bg);
  border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  transition: box-shadow 0.18s, transform 0.18s;
}
.post-list-home .post-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
}
.post-list-home .post-item:hover {
  box-shadow: 0 6px 24px rgba(0,86,179,0.10);
  transform: translateY(-4px);
}
.post-list-home h3 {
  margin-top: 0.5em;
  margin-bottom: 0.2em;
  font-size: 1.3rem; /* Slightly smaller than H2 */
}
.post-list-home h3 a {
  color: var(--heading-color);
  text-decoration: none;
}
.post-list-home h3 a:hover {
  color: var(--accent-color);
  text-decoration: underline;
}
.post-meta {
  font-size: 0.9rem;
  color: var(--muted-color);
  margin-bottom: 0.8em;
  font-family: var(--heading-font); /* Use sans-serif for meta */
}
</style>