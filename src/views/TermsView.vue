<template>
  <main class="site-main">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 4rem 2rem;">
      <h1>Términos y Condiciones</h1>
      <p class="legal-updated">Última actualización: Marzo 2026</p>

      <h3>1. Aceptación de los Términos</h3>
      <p>Al acceder y utilizar KapitalBlog, aceptas estos términos y condiciones en su totalidad. Si no estás de acuerdo con alguno de estos términos, te pedimos que no utilices el sitio.</p>

      <h3>2. Naturaleza del Contenido</h3>
      <p>Todo el contenido publicado en KapitalBlog es exclusivamente periodístico e informativo. <strong>No constituye asesoramiento financiero, comercial, legal ni de inversión.</strong> El contenido publicado refleja el análisis editorial de la redacción y no debe interpretarse como una recomendación para tomar decisiones financieras.</p>

      <h3>3. Exención de Responsabilidad</h3>
      <p>KapitalBlog no se hace responsable de:</p>
      <ul>
        <li>Decisiones financieras o de inversión tomadas a partir de la información publicada en este sitio.</li>
        <li>Pérdidas económicas derivadas del uso de la información aquí presentada.</li>
        <li>La exactitud o puntualidad de la información en tiempo real, ya que los mercados financieros son intrínsecamente volátiles.</li>
      </ul>

      <h3>4. Propiedad Intelectual</h3>
      <p>Todo el contenido editorial, diseño gráfico, marca y logotipos de KapitalBlog son propiedad del sitio. Queda prohibida su reproducción total o parcial sin autorización previa por escrito.</p>

      <h3>5. Publicidad</h3>
      <p>KapitalBlog puede mostrar anuncios de terceros. No somos responsables del contenido de dichos anuncios ni de los productos o servicios que promocionan. La presencia de un anuncio no implica respaldo editorial.</p>

      <h3>6. Modificaciones</h3>
      <p>Nos reservamos el derecho de modificar estos términos en cualquier momento. Las modificaciones entrarán en vigor desde su publicación en esta página.</p>

      <h3>7. Contacto</h3>
      <p>Para cualquier consulta sobre estos términos, utiliza nuestro <router-link to="/contacto" style="color: var(--purple);">formulario de contacto</router-link>.</p>
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
