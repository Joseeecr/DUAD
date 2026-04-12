import { getUserById } from "./services/userService.js";
import { getLoggedUserId } from "./auth/session.js";
import { removeLoggedUserId } from "./auth/session.js";

const userContainer = document.getElementById("user-container");
const logoutBtn = document.getElementById("logout-btn");

const isUserLoggedIn = () => {
  return Boolean(localStorage.getItem("loggedUserId"));
}


const redirectIfNotLoggedIn = () => {
  if(!isUserLoggedIn()){
    window.location.href = "./login.html";
    return false
  }
  return true
}


const logoutUser = () => {
  removeLoggedUserId();
  window.location.href = "./login.html";
}

const protectProfilePage = async ()  => {
  if(!redirectIfNotLoggedIn()){
    return;
  }

  const userId = getLoggedUserId();

  const userData = await getUserById(userId);

  if(userData.success){
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
  <h3>Name: ${userData.data.name}</h3> 
  <p>Email: ${userData.data.data.email}</p>
  <p>Address: ${userData.data.data.address}</p>
  `;
  userContainer.replaceChildren();
  userContainer.append(card);
  } else {
    alert(`Error loading user data: ${userData.error.details || userData.error.message}`)
  }
}


async function initProfilePage() {
  await protectProfilePage();
  logoutBtn.addEventListener("click", logoutUser);
}

initProfilePage();