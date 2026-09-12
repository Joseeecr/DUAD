export function createProductsCounter(productCount, totalProducts) {
  return `<span>Mostrando <strong>${productCount}</strong> de <strong>${totalProducts} productos</strong></span>`
}


function createSortOptions(currentSort){
  const sortOptions = [
    { value: "newest", label: "Más recientes" },
    { value: "oldest", label: "Menos recientes" },
    { value: "price-asc", label: "Precio: Menor a Mayor" },
    { value: "price-desc", label: "Precio: Mayor a Menor" }
  ];

  const options = sortOptions.map((option) => {
    const selected = option.value === currentSort ? "selected" : "";
    return `<option value="${option.value}" ${selected}>${option.label}</option>`}).join("")
  }

export function createProductsSortSelect(currentSort){
  const test =  createSortOptions(currentSort);
  console.log(test)
  return `<div class="sort-by-container">
          <label for="sort-by">Ordenar por:</label>
          <select name="sort-by" id="sort-by">
          ${createSortOptions(currentSort)}
          </select>
          </div>`
          
}

export function createProductsHeader(productCount, totalProducts, currentSort) {
    return `  
        ${createProductsCounter(productCount, totalProducts)}
  
        ${createProductsSortSelect(currentSort)}
    `
}
