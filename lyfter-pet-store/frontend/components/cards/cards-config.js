import { BASE_API_URL } from "../../config/api.js"

export function createCardConfig(product) {
  return {
    productImage: `${BASE_API_URL}${product.image}`,

    card: {
      title: product.name,
      price: product.price,
      button: 'Ver detalles'
    }
  };
}