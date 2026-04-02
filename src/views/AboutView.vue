<template>
  <main class="site-main about-view">
    <div class="container about-container">
      <section class="about-hero">
        <h1>About Kapital</h1>
        <p class="about-lead">The daily pulse of the financial, economic and business world. No filters, no middlemen.</p>
      </section>

      <section class="about-content">
        <div class="about-block">
          <h2>Our Mission</h2>
          <p>KapitalBlog is an independent digital news portal whose sole purpose is to inform. We curate and analyze the most relevant news in macroeconomics, stock markets, real estate, financial technology and digital adoption to keep you up to date with the global flow of capital.</p>
          <p>We do not offer financial services, trading strategies, or investment recommendations of any kind. We are market observers who translate corporate complexity into clear, accessible reading pieces.</p>
        </div>

        <div class="about-block">
          <h2>What We Cover</h2>
          <div class="topics-grid">
            <div class="topic-card">
              <span class="topic-icon" aria-hidden="true">
                <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 1v22"></path>
                  <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7H14a3.5 3.5 0 0 1 0 7H6"></path>
                </svg>
              </span>
              <h3>Budget</h3>
              <p>News on fiscal policies, government budgets and capital flows</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon" aria-hidden="true">
                <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 10h18" />
                  <path d="M4 10V20" />
                  <path d="M20 10v10" />
                  <path d="M7 20v-6" />
                  <path d="M12 20v-6" />
                  <path d="M17 20v-6" />
                  <path d="M2 10l10-6 10 6" />
                </svg>
              </span>
              <h3>Savings</h3>
              <p>Trends in interest rates, banking products and sector movements</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon" aria-hidden="true">
                <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 3v18h18"></path>
                  <path d="M7 14l4-4 3 3 6-6"></path>
                </svg>
              </span>
              <h3>Investing</h3>
              <p>Coverage of stock markets, cryptocurrencies and alternative assets</p>
            </div>
            <div class="topic-card">
              <span class="topic-icon" aria-hidden="true">
                <svg class="icon" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="6" width="18" height="12" rx="2" />
                  <path d="M3 10h18" />
                  <path d="M7 15h4" />
                </svg>
              </span>
              <h3>Credit</h3>
              <p>Analysis of the credit landscape, regulations and financial products</p>
            </div>
          </div>
        </div>

        <div class="about-block">
          <h2>Our Approach</h2>
          <p>We operate as a collaborative, decentralized newsroom. Information is bigger than any individual, and therefore we publish under Kapital's unique editorial seal, ensuring that the protagonist is always the news, the data and the stories — not the person who writes them.</p>
          <ul class="principles-list">
            <li><strong>Clarity over jargon:</strong> We simplify complex concepts without oversimplifying them.</li>
            <li><strong>Data-driven independence:</strong> Our analyses are based on verifiable empirical metrics.</li>
            <li><strong>News only:</strong> We do not give financial advice or investment recommendations.</li>
          </ul>
        </div>

        <div class="about-block about-cta">
          <h2>Want to get in touch?</h2>
          <p>For press releases, corrections or general inquiries to our editorial desk.</p>
          <router-link to="/contact" class="btn-cta">Contact Us →</router-link>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.about-view { padding: 60px 0 80px; }
.about-container { max-width: 860px; margin: 0 auto; }

.about-hero { text-align: center; margin-bottom: 60px; }
.about-hero h1 { font-size: 44px; font-weight: 800; letter-spacing: -1px; margin: 0 0 16px; }
.about-lead { font-size: 20px; color: var(--muted); line-height: 1.6; max-width: 600px; margin: 0 auto; }

.about-content { display: flex; flex-direction: column; gap: 48px; }
.about-block h2 { font-size: 24px; font-weight: 800; margin: 0 0 16px; letter-spacing: -0.5px; }
.about-block p { color: var(--muted); font-size: 16px; line-height: 1.7; margin: 0 0 12px; }

.topics-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 20px; }
.topic-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
  padding: 24px; transition: transform 0.2s;
}
.topic-card:hover { transform: translateY(-2px); }
.topic-icon { font-size: 32px; display: block; margin-bottom: 12px; }
.topic-card h3 { font-size: 18px; margin: 0 0 8px; }
.topic-card p { color: var(--muted); font-size: 14px; margin: 0; }

.principles-list { list-style: none; padding: 0; margin-top: 16px; }
.principles-list li {
  margin-bottom: 16px; font-size: 16px; line-height: 1.7; color: var(--muted);
  border-left: 3px solid var(--purple); padding-left: 16px;
}

.about-cta { text-align: center; background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 48px 24px; }
.btn-cta {
  display: inline-block; background: var(--purple); color: white; padding: 14px 28px;
  border-radius: 10px; font-weight: 700; font-size: 16px; margin-top: 8px;
  transition: background 0.2s; text-decoration: none;
}
.btn-cta:hover { background: var(--purple-2); text-decoration: none; }

@media (max-width: 768px) {
  .topics-grid { grid-template-columns: 1fr; }
}
</style>
