import { baseApiUrlInstance } from "../../config/api.js";
import { createCardConfig } from "../../components/cards/cards-config.js";
import {createCard} from '../../components/cards/cards.js'
import {createPagination} from '../../components/pagination/pagination.js'


export async function getProducts() {
  try {
    const response = await baseApiUrlInstance.get("/products/");
    return response.data;

  } catch (error) {
    console.log(error.response || error);
    return error.response || error;
  };
}

const products = await getProducts();

const config = products.map((product) => createCardConfig(product));

const productsContainer = document.querySelector('.products-listing')

const productsCards = document.querySelector('[data-component="products-cards"]')

const pagination = createPagination()

productsCards.innerHTML = config.map((card) => createCard(card)).join(" ");

productsContainer.insertAdjacentHTML('beforeend', pagination)