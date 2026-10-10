export function cardButton(detailsText, link) {
  return `
  <button class="btn see-details">
    ${detailsText}
    <a class="product-link" href=${link}></a>
  </button>
  `
}
