<template>
  <main class="site-main">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 4rem 2rem;">
      <h1>Cookie Policy</h1>
      <p class="legal-updated">Last updated: March 2026</p>

      <h3>1. What Are Cookies?</h3>
      <p>Cookies are small text files stored on your device when you visit a website. They help us remember your preferences and understand how you interact with our content.</p>

      <h3>2. Cookies We Use</h3>
      <ul>
        <li><strong>Essential cookies:</strong> Enable basic site functionality, such as remembering your theme preference (dark/light).</li>
        <li><strong>Analytical cookies:</strong> Help us understand how you navigate the site (most visited pages, session duration) to improve the editorial experience.</li>
        <li><strong>Advertising cookies:</strong> Used by our advertising partners to show you relevant ads based on your browsing interests.</li>
      </ul>

      <h3>3. Managing Cookies</h3>
      <p>You can configure your browser to reject all cookies or to alert you when a cookie is being sent. Please note that some site features may be affected if you disable essential cookies.</p>

      <h3>4. Third-Party Cookies</h3>
      <p>Some third-party services (such as advertising or analytics platforms) may set their own cookies. KapitalBlog does not control these cookies and we recommend consulting the privacy policies of those services.</p>

      <h3>5. Contact</h3>
      <p>For questions about our cookie policy, please use our <router-link to="/contact" style="color: var(--purple);">contact form</router-link>.</p>
    </div>
  </main>
</template>

<style scoped>
h1 { font-size: 2.5rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 8px; }
.legal-updated { color: var(--muted); font-size: 0.9rem; margin-bottom: 2rem; }
h3 { margin-top: 2rem; font-size: 1.2rem; font-weight: 700; }
p, li { color: var(--text); font-size: 1rem; line-height: 1.8; margin-bottom: 0.8rem; }
ul { padding-left: 1.5rem; margin-bottom: 1rem; }
</style>
