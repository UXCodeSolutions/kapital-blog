<template>
  <main class="site-main">
    <div class="container" style="max-width: 800px; margin: 0 auto; padding: 4rem 2rem;">
      <h1>Política de Privacidad</h1>
      <p class="legal-updated">Última actualización: Marzo 2026</p>

      <h3>1. Introducción</h3>
      <p>KapitalBlog es un portal digital independiente de noticias financieras operado de forma anónima. Nos tomamos la privacidad de nuestros lectores con suma seriedad. Esta política describe qué información recopilamos, cómo la utilizamos y cuáles son tus derechos.</p>

      <h3>2. Información que Recopilamos</h3>
      <p>Recopilamos información mínima y solo cuando es proporcionada de forma voluntaria por el usuario:</p>
      <ul>
        <li><strong>Email de suscripción:</strong> Si decides suscribirte a nuestro boletín informativo, almacenaremos tu dirección de correo electrónico exclusivamente para el envío del newsletter.</li>
        <li><strong>Datos de contacto:</strong> Si nos escribes a través del formulario de contacto, almacenaremos tu nombre, email y mensaje para poder responderte.</li>
        <li><strong>Datos de navegación:</strong> Recopilamos datos anónimos de uso del sitio (páginas visitadas, tiempo de sesión) a través de cookies analíticas con el fin de mejorar la experiencia de usuario.</li>
      </ul>

      <h3>3. Uso de la Información</h3>
      <p>La información recopilada se utiliza exclusivamente para:</p>
      <ul>
        <li>Enviar boletines informativos periódicos a los suscriptores.</li>
        <li>Responder consultas recibidas a través del formulario de contacto.</li>
        <li>Mejorar el contenido editorial y la experiencia de navegación del sitio.</li>
        <li>Mostrar anuncios contextuales relevantes a los lectores.</li>
      </ul>

      <h3>4. Compartición de Datos</h3>
      <p>No vendemos, alquilamos ni compartimos tus datos personales con terceros, salvo cuando sea requerido por ley o para operar servicios esenciales del sitio (como proveedores de email o plataformas de análisis).</p>

      <h3>5. Tus Derechos</h3>
      <p>Puedes solicitar la eliminación de tus datos en cualquier momento enviando un correo a través de nuestro formulario de contacto. También puedes desuscribirte del newsletter en cualquier momento usando el enlace incluido en cada correo.</p>

      <h3>6. Contacto</h3>
      <p>Para cualquier consulta relacionada con esta política, utiliza nuestro <router-link to="/contacto" style="color: var(--purple);">formulario de contacto</router-link>.</p>

      <div style="background: var(--surface); padding:1.5rem; text-align:center; border-radius:4px; margin-top: 3rem; border: 1px dashed var(--border);">
        <span style="color: var(--muted); font-size:0.9rem;">[Espacio Publicitario]</span>
      </div>
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
