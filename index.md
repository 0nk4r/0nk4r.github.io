---
layout: default
title: Home
---

<div style="text-align:center; margin-bottom: 1.5rem;">
  <img src="/assets/profile.jpg" alt="Onkar Koli" style="width: 120px; height: 120px; object-fit: cover; border-radius: 50%; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border: 2px solid var(--border-color); margin-top: 1.2rem;">
</div>

*Product Security Engineer*

Learning how machines work ! 

---

### Areas of Work

Exploring the security of anything that computes, connects, or occasionally combusts — from IoT to WTF, firmware to the cloud, and everything in between. Whether it blinks, boots, or just barely functions, I'm usually in there somewhere armed with curiosity, a slightly overworked debugger, and a deep need to ask: "What happens if I do this?" 

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