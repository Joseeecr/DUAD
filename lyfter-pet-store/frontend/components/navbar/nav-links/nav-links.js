import { navLink } from "./nav-link.js";


export function navLinks(links){
  const items = links
    .map(link => navLink(link))
    .join('')

  return `
    <ul class="navbar-links">
      ${items}
    </ul>
  `
}