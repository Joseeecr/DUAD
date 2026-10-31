import { baseApiUrlInstance } from "../../config/api.js";
import { BASE_API_URL } from "../../config/api.js"
import {showErrorMessage} from '../../components/status-message/status-message.js'

const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get("id");
const statusElement = document.querySelector(".status-element");
const productImage = document.querySelector('[data-component="product-image-container"]');
const productInfoContainer = document.querySelector('[data-component="product-info-container"]');


async function getProduct() {
  const response = await baseApiUrlInstance.get(`/products/${myParam}`);
  return response.data;
}


function renderPage(product){

  productImage.innerHTML = `<image class="product-image" src=${BASE_API_URL}${product.image}></image>`;

  productInfoContainer.innerHTML = `<h1 class="product-title">${product.name}</h1> 
                                    <span class="product-price">$${product.price}</span>
                                    <p class="product-description">${product.description}</p>
                                    <a class="add-to-cart btn" href="#">Añadir al carrito</a>
                                    <a class="back-to-products btn" href="/frontend/pages/products/index.html">Volver al catálogo</a>
                                    `
}


async function initPage() {
  try {
    let product = await getProduct();
    renderPage(product);
    productImage.classList.remove("is-hidden");
    productInfoContainer.classList.remove("is-hidden");
    statusElement.hidden = true
  } 

  catch (error) {
    console.log(error.response || error);

    if(!error.response){
      showErrorMessage(statusElement, "No pudimos conectar con el servidor. Comprueba tu conexión e inténtalo de nuevo.");
    }

    else if(error.response.status === 404) {
      showErrorMessage(statusElement, "No encontramos el producto que buscas.");
    }

    else if(error.response.status >= 500) {
      showErrorMessage(statusElement, "Ocurrió un problema al cargar el producto. Inténtalo de nuevo.");
    }
  }
}

initPage();