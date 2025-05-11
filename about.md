---
layout: default
title: About
---

<section class="about-section">
  <div class="about-content">
    <div class="about-header">
      <h1>About Me</h1>
      <p class="subtitle">Product Security Engineer at SolarWinds</p>
    </div>

    <div class="about-grid">
      <div class="about-main">
        <p class="lead">I'm a Product Security Engineer passionate about building secure software and protecting digital assets. My expertise lies in application security, secure development practices, and security architecture.</p>

        <h2>Expertise</h2>
        <div class="expertise-grid">
          <div class="expertise-item">
            <h3>Application Security</h3>
            <p>Implementing and maintaining robust security controls in software applications</p>
          </div>
          <div class="expertise-item">
            <h3>Secure Development</h3>
            <p>Integrating security throughout the software development lifecycle</p>
          </div>
          <div class="expertise-item">
            <h3>Security Architecture</h3>
            <p>Designing and implementing secure system architectures</p>
          </div>
          <div class="expertise-item">
            <h3>Threat Modeling</h3>
            <p>Identifying and mitigating potential security threats</p>
          </div>
        </div>

        <h2>Connect</h2>
        <div class="connect-links">
          <a href="mailto:contact@onkark.com" class="connect-link">
            <i class="fas fa-envelope"></i>
            <span>Email</span>
          </a>
          <a href="https://linkedin.com/in/0nk4r" class="connect-link">
            <i class="fab fa-linkedin"></i>
            <span>LinkedIn</span>
          </a>
          <a href="https://github.com/0nk4r" class="connect-link">
            <i class="fab fa-github"></i>
            <span>GitHub</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
.about-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

.about-header {
  text-align: center;
  margin-bottom: 4rem;
}

.about-header h1 {
  color: var(--primary);
  font-size: 2.5rem;
  margin: 0;
  font-weight: 800;
}

.about-header .subtitle {
  color: var(--accent);
  font-size: 1.25rem;
  margin: 1rem 0 0;
}

.about-grid {
  display: grid;
  gap: 4rem;
}

.about-main {
  max-width: 800px;
  margin: 0 auto;
}

.lead {
  font-size: 1.25rem;
  line-height: 1.6;
  color: var(--light-text);
  margin-bottom: 3rem;
}

h2 {
  color: var(--primary);
  font-size: 1.75rem;
  margin: 2.5rem 0 1.5rem;
}

.expertise-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.expertise-item {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: var(--shadow);
}

.expertise-item h3 {
  color: var(--primary);
  font-size: 1.25rem;
  margin: 0 0 0.75rem;
}

.expertise-item p {
  color: var(--light-text);
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.connect-links {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.connect-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--primary);
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  border: 2px solid var(--primary);
  border-radius: 100px;
  transition: all 0.2s;
}

.connect-link:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(23, 71, 52, 0.15);
}

.connect-link i {
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .about-section {
    padding: 3rem 1rem;
  }

  .about-header h1 {
    font-size: 2rem;
  }

  .lead {
    font-size: 1.1rem;
  }

  .expertise-grid {
    grid-template-columns: 1fr;
  }

  .connect-links {
    justify-content: center;
  }
}
</style> 