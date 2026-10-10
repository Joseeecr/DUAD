import { cardTitle } from "./card-title.js"
import { cardPrice } from "./card-price.js"
import { cardImage } from "./card-image.js"
import { cardButton } from "./card-button.js"


export function createCard(props) {
  return `
    <div class="product-card">
      ${cardImage(props.productImage, props.card.stock)}
      <div class="card-info">
        ${cardTitle(props.card.title)}
        ${cardPrice(props.card.price)}
        ${cardButton(props.card.button, props.card.productLink)}
      </div>
    </div>
  `
}