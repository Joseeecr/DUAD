import { baseApiUrlInstance } from "../../config/api.js";
import { createCardConfig } from "../../components/cards/cards-config.js";
import {createCard} from '../../components/cards/cards.js'
import {createPagination} from '../../components/pagination/pagination.js'
import {createProductsHeader} from '../../components/products-header/products-header.js'
import {showErrorMessage} from '../../components/status-message/status-message.js'

const productsCardsContainer = document.querySelector('[data-component="products-cards"]');
const productsPaginationContainer = document.querySelector('[data-component="pagination"]');
const productsHeaderContainer = document.querySelector('[data-component="products-header"]');
const checkboxesContainer = document.querySelector('.aside-checkbox-categories');
const statusElement = document.querySelector('.status-element');
const PRODUCTS_PER_PAGE = 6;
let currentPage = 1;
let currentSort = "newest";
let selectedCategoryIds  = [];
let products = []


async function getProducts(filters) {
  
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


function renderPage(){
  const currentProducts  = getProductsForPage(products, currentPage, PRODUCTS_PER_PAGE);
  const totalPages = calculateTotalPages(products);
  const pagination = createPagination(totalPages, currentPage);
  const productsHeader = createProductsHeader(currentProducts.length, products.length, currentSort);

  productsHeaderContainer.innerHTML = productsHeader;

  productsPaginationContainer.innerHTML = pagination;

  renderProducts(currentProducts, productsCardsContainer);
}


productsPaginationContainer.addEventListener("click", (event) => {
  const button = event.target;

  if (button.tagName === "BUTTON"){
    currentPage = Number(button.dataset.page)
    renderPage()
  }
})


productsHeaderContainer.addEventListener("change", (event) => {
  currentSort = event.target.value;
  currentPage = 1;
  loadProducts();
});


checkboxesContainer.addEventListener("change", async (event) => {
  if (event.target.classList.contains('category-filter')) {
    const categoryCheckboxes  = checkboxesContainer.querySelectorAll('.category-filter')

    const selectedCategoryCheckboxes  = [...categoryCheckboxes].filter((checkbox) => checkbox.checked)

    selectedCategoryIds  = selectedCategoryCheckboxes.map((checkbox) => checkbox.value)
    currentPage = 1;
    loadProducts();
  }
})


async function loadProducts() {
  try {
    products = await getProducts({
      sortParameter: currentSort,
      categoryIds: selectedCategoryIds
    });

    renderPage()
    statusElement.hidden = true
  }

  catch (error) {
    console.log(error.response || error);

    if(!error.response){
      showErrorMessage(statusElement, "No pudimos conectar con el servidor. Comprueba tu conexión e inténtalo de nuevo.");
    }

    else if(error.response.status === 404) {
      showErrorMessage(statusElement, "No encontramos los productos que buscas.");
    }

    else if(error.response.status >= 500) {
      showErrorMessage(statusElement, "Ocurrió un problema al cargar el producto. Inténtalo de nuevo.");
    }
  }
}

loadProducts();