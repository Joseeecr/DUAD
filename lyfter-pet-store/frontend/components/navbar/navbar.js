import { brand } from './brand/brand.js'
import { navbarActions } from './actions/navbar-actions.js'
import { navLinks } from './nav-links/nav-links.js'

export function navbar(props) {
  return `
    <nav class="navbar">

      ${brand(props.brandName)}

      ${navLinks(props.links)}

      ${navbarActions()}

    </nav>
  `
}