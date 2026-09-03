import { cardTitle } from "./card-title.js"
import { cardPrice } from "./card-price.js"
import { cardImage } from "./card-image.js"

export function createCard(props) {
  return `
    <div class="product-card">
      ${cardImage(props.productImage)}
      <div class="card-info">
        ${cardTitle(props.card.title)}
        ${cardPrice(props.card.price)}
        <button class="btn see-details">${props.card.button}</button>
      </div>
    </div>
  `
}