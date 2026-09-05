export function createProductsCounter(productCount, totalProducts) {
  return `<span>Mostrando <strong>${productCount}</strong> de <strong>${totalProducts} productos</strong></span>`
}

export function createProductsSortSelect(){
  return `<div class="order-by">
          <label for="select-date">Ordenar por:</label>
          <select name="date" id="select-date">
          <option value="desc">Más recientes</option>
          <option value="asc">Menos recientes</option>
          </select>
          </div>`
          
}

export function createProductsHeader(productCount, totalProducts) {
    return `  
        ${createProductsCounter(productCount, totalProducts)}
  
        ${createProductsSortSelect()}
    `
}
