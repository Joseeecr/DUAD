import { brand } from "../brand/brand.js"

export function footer(props) {
  return `
    <div class="footer-container">
      ${brand(props.brandName)}
      <p class="footer-tagline">Cuidamos de tus compañeros con el amor y la calidad que se merecen</p>
      <p class="footer-copyright">© 2026 PawStore. Todos los derechos reservados.</p>
    </div>
  `
}

  // ${navLinks(props.links)}