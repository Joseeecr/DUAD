import { cardStock } from "./card-stock.js"


export function cardImage(image, stock) {
  return `
  <div class="card-image-container">
    <image class="card-image" src=${image}></image>
    ${cardStock(stock)}
  </div>`
}