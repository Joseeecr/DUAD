
export function navLink({ label, href }) {
  const active =
    window.location.pathname === href
      ? 'active'
      : ''

  return `
    <li class="navbar-link">

      <a
        href="${href}"
        class="${active}"
      >
        ${label}
      </a>

    </li>
  `
}