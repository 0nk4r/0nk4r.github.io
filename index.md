---
layout: default
title: Home
---

<section class="hero">
  <div class="hero-content">
    <h1>Onkar Koli</h1>
    <p class="subtitle">Product Security Engineer</p>
    <p class="description">Building secure software and protecting digital assets through innovative security solutions.</p>
    <div class="hero-links">
      <a href="/blog" class="primary-button">Read Blog</a>
      <a href="/about" class="secondary-button">About Me</a>
    </div>
  </div>
</section>

<section class="featured-posts">
  <h2>Latest Insights</h2>
  <div class="posts-grid">
    {% for post in site.posts limit:3 %}
      <article class="post-card">
        <div class="post-content">
          <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>
          <div class="post-meta">
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
            {% if post.tags %}
              <span class="post-tags">
                {% for tag in post.tags %}
                  <span class="tag">{{ tag }}</span>
                {% endfor %}
              </span>
            {% endif %}
          </div>
        </div>
      </article>
    {% endfor %}
  </div>
  <div class="view-all">
    <a href="/blog" class="view-all-link">View All Posts →</a>
  </div>
</section>

<style>
.hero {
  text-align: center;
  padding: 6rem 2rem;
  background: linear-gradient(to bottom, rgba(23, 71, 52, 0.05), transparent);
  border-radius: 0 0 2rem 2rem;
  margin-bottom: 4rem;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 3.5rem;
  color: var(--primary);
  margin: 0;
  font-weight: 800;
  letter-spacing: -1px;
}

.subtitle {
  font-size: 1.5rem;
  color: var(--accent);
  margin: 1rem 0;
  font-weight: 500;
}

.description {
  font-size: 1.2rem;
  color: var(--light-text);
  max-width: 600px;
  margin: 1.5rem auto;
  line-height: 1.6;
}

.hero-links {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.primary-button, .secondary-button {
  padding: 0.8rem 2rem;
  border-radius: 100px;
  text-decoration: none;
  font-weight: 500;
  transition: transform 0.2s, box-shadow 0.2s;
}

.primary-button {
  background: var(--primary);
  color: white;
}

.secondary-button {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
}

.primary-button:hover, .secondary-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(23, 71, 52, 0.15);
}

.featured-posts {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.featured-posts h2 {
  text-align: center;
  color: var(--primary);
  font-size: 2rem;
  margin-bottom: 3rem;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.post-card {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.2s, box-shadow 0.2s;
}

.post-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(23, 71, 52, 0.12);
}

.post-content {
  padding: 1.5rem;
}

.post-content h3 {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
}

.post-content h3 a {
  color: var(--primary);
  text-decoration: none;
}

.post-excerpt {
  color: var(--light-text);
  font-size: 0.95rem;
  margin: 0 0 1rem 0;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--light-text);
}

.post-tags {
  display: flex;
  gap: 0.5rem;
}

.tag {
  background: rgba(23, 71, 52, 0.1);
  color: var(--primary);
  padding: 0.2rem 0.6rem;
  border-radius: 100px;
  font-size: 0.75rem;
}

.view-all {
  text-align: center;
  margin-top: 2rem;
}

.view-all-link {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.view-all-link:hover {
  color: var(--accent);
}

@media (max-width: 768px) {
  .hero {
    padding: 4rem 1rem;
  }
  
  .hero h1 {
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1.25rem;
  }
  
  .description {
    font-size: 1.1rem;
  }
  
  .hero-links {
    flex-direction: column;
  }
  
  .posts-grid {
    grid-template-columns: 1fr;
  }
}
</style>