import { baseApiUrlInstance } from "../../config/api.js";
import { BASE_API_URL } from "../../config/api.js"

let loadingState = "loading";
const urlParams = new URLSearchParams(window.location.search);
const myParam = urlParams.get("id");

async function getProduct() {
  try {
    const response = await baseApiUrlInstance.get(`/products/${myParam}`);

    return response.data;

  } catch (error) {
    console.log(error.response || error);
    return error.response || error;
  };
}


let product = await getProduct()

const productContainer = document.querySelector('[data-component="product-content"]');
const productImage = document.querySelector('[data-component="product-image-container"]');
const productInfoContainer = document.querySelector('[data-component="product-info-container"]');

function renderPage(){

  productImage.innerHTML = `<image class="product-image" src=${BASE_API_URL}${product.image}></image>`;

  productInfoContainer.innerHTML = `<h1 class="product-title">${product.name}</h1> 
                                    <span class="product-price">$${product.price}</span>
                                    <p class="product-description">${product.description}</p>
                                    <a class="add-to-cart btn" href="#">Añadir al carrito</a>
                                    <a class="back-to-products btn" href="/frontend/pages/products/index.html">Volver al catálogo</a>
                                    `

}

renderPage();