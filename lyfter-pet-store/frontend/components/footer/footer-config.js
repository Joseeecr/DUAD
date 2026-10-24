import { footer } from './footer.js'

const footerConfig = {

  brandName: 'PawStore',

  links: [
    {
      label: 'Contacto',
      href: '/frontend/pages/contact/index.html'
    }
  ]
}

const container = document.querySelector('[data-component="footer"]')

container.innerHTML = footer(footerConfig)