import { cardStock } from "./card-stock.js"


export function cardImage(image, stock) {
  return `
  <div class="card-image-container">
    <img class="card-image" src=${image}/>
    ${cardStock(stock)}
  </div>`
}