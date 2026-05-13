export function navbarTemplate(options) {
  return `
    <nav class="navbar">

      <a href="/" class="brand-logo">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="120 115 60 60" width="24" height="24" title="brand-icon">
            <path fill="#254dda" d="M149.34 136.99c7.69-.49 10.06 8.54 14.69 13.01 1.8 1.75 4.3 4.6 5.27 6.89-2.68 3.93-9.44 7.66-14.12 8.29-1.13.15-2.94.07-4.13.05-3.98-.01-6.52.44-10.29-1.13-4.07-1.69-7.18-3.75-10.01-7.16 1.49-3.73 4.9-6.06 7.27-9.17 3.49-4.57 5.06-9.54 11.32-10.78Z"/>
            <path fill="#254dda" d="M130.57 129.81a6.08 6.08 0 1 1-2.84 11.82 6.08 6.08 0 0 1 2.84-11.82Z"/>
            <path fill="#254dda" d="M167.25 129.8a6.08 6.08 0 1 1-2.95 11.8 6.08 6.08 0 0 1 2.95-11.8Z"/>
            <path fill="#254dda" d="M141.44 120.04a6.08 6.08 0 1 1-2.91 11.8 6.08 6.08 0 0 1 2.91-11.8Z"/>
            <path fill="#254dda" d="M156.02 120.04a6.08 6.08 0 1 1-2.76 11.87 6.08 6.08 0 0 1 2.76-11.87Z"/>
        </svg>
        <span class="brand-name">PawStore</span>
      </a>

      <ul class="navbar-links">
        <li class="navbar-link"><a href="/">Inicio</a></li>
        <li class="navbar-link"><a href="/products">Productos</a></li>
        <li class="navbar-link"><a href="/contact">Contacto</a></li>
      </ul>

      <div class="header-actions">
        <a href="/login" class="user-profile-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" title="user-profile-icon"" 
          stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-user">
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path d="M8 7a4 4 0 1 0 8 0a4 4 0 0 0 -8 0" /><path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" /></svg>
        </a>
    
    
        <a href="/carrito" class="shopping-cart-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
            fill="none" title="shopping-cart-icon" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" 
            class="icon icon-tabler icons-tabler-outline icon-tabler-shopping-cart">
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path d="M4 19a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
            <path d="M15 19a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
            <path d="M17 17h-11v-14h-2" />
            <path d="M6 5l14 1l-1 7h-13" />
          </svg>
          <span class="cart-count"></span>
        </a>
      </div>
      ${
        options.showSearchBar
        ? `
          <form class="search" method="GET">
            <label for="search-bar"></label>
            <input
                type="text"
                placeholder="Buscar"
                id="search-bar"
              >
          <form/>
          `

          : " "
      }
    </nav>
  `;
}