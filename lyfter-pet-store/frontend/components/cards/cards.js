import { cardTitle } from "./card-title.js"
import { cardPrice } from "./card-price.js"

export function createCard(props) {
  return `
    <div class="product-card">

      ${cardTitle(props.card.title)}
      ${cardPrice(props.card.price)}
      <button>${props.card.button}</button>

    </div>
  `
}