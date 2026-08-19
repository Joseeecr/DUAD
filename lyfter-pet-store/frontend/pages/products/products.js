import { baseApiUrlInstance } from "../../config/api.js";
import { createCardConfig } from "../../components/cards/cards-config.js";
import {createCard} from '../../components/cards/cards.js'
import {createPagination} from '../../components/pagination/pagination.js'

const PRODUCTS_PER_PAGE = 6;
let currentPage = 1;

async function getProducts() {
  try {
    const response = await baseApiUrlInstance.get("/products/");
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

function counterProducts(){

}

const products = await getProducts();
const productsCardsContainer = document.querySelector('[data-component="products-cards"]');
const productsPaginationContainer = document.querySelector('[data-component="pagination"]');
const productsHeaderContainer = document.querySelector('[data-component="products-header"]');

function renderPage(){
  const currentProducts  = getProductsForPage(products, currentPage, PRODUCTS_PER_PAGE);
  const totalPages = calculateTotalPages(products);
  const pagination = createPagination(totalPages, currentPage);

  productsHeaderContainer.innerHTML = `<p>Mostrando <strong>${currentProducts.length} productos</strong></p>`
  
  productsPaginationContainer.innerHTML = pagination

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