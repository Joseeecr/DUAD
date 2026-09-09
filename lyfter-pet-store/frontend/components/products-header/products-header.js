export function createProductsCounter(productCount, totalProducts) {
  return `<span>Mostrando <strong>${productCount}</strong> de <strong>${totalProducts} productos</strong></span>`
}

export function createProductsSortSelect(){
  return `<div class="sort-by-container">
          <label for="sort-by">Ordenar por:</label>
          <select name="sort-by" id="sort-by">
          <option value="newest">Más recientes</option>
          <option value="oldest">Menos recientes</option>
          <option value="price-asc">Precio: Menor a Mayor</option>
          <option value="price-desc">Precio: Mayor a Menor</option>
          </select>
          </div>`
          
}

export function createProductsHeader(productCount, totalProducts) {
    return `  
        ${createProductsCounter(productCount, totalProducts)}
  
        ${createProductsSortSelect()}
    `
}
