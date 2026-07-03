export function createCardConfig(product) {
  return {
    productImage: product.image,

    card: {
      title: product.name,
      price: product.price,
      button: 'Ver detalles'
    }
  };
}