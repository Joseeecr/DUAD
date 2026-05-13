import { navbarTemplate } from "./navbar.template.js";

export function renderNavbar(container, options) {
  container.innerHTML = navbarTemplate(options);
}