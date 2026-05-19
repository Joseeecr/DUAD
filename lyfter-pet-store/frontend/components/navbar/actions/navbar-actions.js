import { userButton } from './user-button.js'
import { cartButton } from './cart-button.js'

export function navbarActions() {
  return `
    <div class="navbar-actions">
      ${userButton()}
      ${cartButton()}
    </div>
  `
}      