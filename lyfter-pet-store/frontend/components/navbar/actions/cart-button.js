import {cartIcon} from "../icons/cart-icon.js"

export function cartButton() {
  return `
  <a href="#" class="cart-button">
    ${cartIcon()}
  </a>
  `
}