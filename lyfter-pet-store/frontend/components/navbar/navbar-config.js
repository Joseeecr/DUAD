import { navbar } from './navbar.js'

const navbarConfig = {

  brandName: 'PawStore',

  links: [
    {
      label: 'Inicio',
      href: '/frontend/pages/home/index.html'
    },

    {
      label: 'Productos',
      href: '/frontend/pages/products/index.html'
    },

    {
      label: 'Contacto',
      href: '/frontend/pages/contact/index.html'
    }
  ]
}

const container = document.querySelector('[data-component="navbar"]')

container.innerHTML = navbar(navbarConfig)