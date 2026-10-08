import { baseApiUrlInstance } from "../../config/api.js";
import { createCardConfig } from "../../components/cards/cards-config.js";
import {createCard} from '../../components/cards/cards.js'
import {createPagination} from '../../components/pagination/pagination.js'
import {createProductsHeader} from '../../components/products-header/products-header.js'

const PRODUCTS_PER_PAGE = 6;
let currentPage = 1;
let currentSort = "newest";
let selectedCategoryIds  = [];

async function getProducts(filters) {
  try {
    const response = await baseApiUrlInstance.get("/products/", {
      params: {
        sort: filters.sortParameter,
        category_id: filters.categoryIds
      },
      paramsSerializer: {
        indexes: null
      }
    });

    return response.data;

  } catch (error) {
    console.log(error.response || error);
    return error.response || error;
  };
}


function getProductsForPage(totalProducts, currentPage, productsPerPage) {
  const currentIndex = (currentPage - 1) * productsPerPage ;

  return totalProducts.slice(currentIndex, (currentIndex + productsPerPage));
}


function calculateTotalPages(products){
  return Math.ceil(products.length / PRODUCTS_PER_PAGE);
}


function renderProducts(products, productsCardsContainer){

  const config = products.map((product) => createCardConfig(product));

  productsCardsContainer.innerHTML = config.map((card) => createCard(card)).join(" ");
}


let products = await getProducts({
    sortParameter: currentSort,
    categoryIds: selectedCategoryIds
  });

const productsCardsContainer = document.querySelector('[data-component="products-cards"]');
const productsPaginationContainer = document.querySelector('[data-component="pagination"]');
const productsHeaderContainer = document.querySelector('[data-component="products-header"]');
const checkboxesContainer = document.querySelector('.aside-checkbox-categories');


function renderPage(){
  const currentProducts  = getProductsForPage(products, currentPage, PRODUCTS_PER_PAGE);
  const totalPages = calculateTotalPages(products);
  const pagination = createPagination(totalPages, currentPage);
  const productsHeader = createProductsHeader(currentProducts.length, products.length, currentSort);

  productsHeaderContainer.innerHTML = productsHeader;

  productsPaginationContainer.innerHTML = pagination;

  renderProducts(currentProducts, productsCardsContainer);
}

renderPage()

productsPaginationContainer.addEventListener("click", (event) => {
  const button = event.target;

  if (button.tagName === "BUTTON"){
    currentPage = Number(button.dataset.page)
    renderPage()
  }
})


productsHeaderContainer.addEventListener("change", async (event) => {
  currentSort = event.target.value;
  products = await getProducts({
    sortParameter: currentSort,
    categoryIds: selectedCategoryIds
  });
  currentPage = 1;
  renderPage();
});




checkboxesContainer.addEventListener("change", async (event) => {
  if (event.target.classList.contains('category-filter')) {
    const categoryCheckboxes  = checkboxesContainer.querySelectorAll('.category-filter')

    const selectedCategoryCheckboxes  = [...categoryCheckboxes].filter((checkbox) => checkbox.checked)

    selectedCategoryIds  = selectedCategoryCheckboxes.map((checkbox) => checkbox.value)
    
    products = await getProducts({
      sortParameter: currentSort,
      categoryIds: selectedCategoryIds
    });

    currentPage = 1;
    renderPage();
  }
})