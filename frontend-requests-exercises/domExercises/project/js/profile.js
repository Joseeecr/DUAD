import { getUserById } from "./services/userService.js";
import { getLoggedUserId, removeLoggedUserId, isUserLoggedIn } from "./auth/session.js";
import { showErrorAlert } from "./ui/errorHandler.js"

const userContainer = document.getElementById("user-container");
const logoutBtn = document.getElementById("logout-btn");
const editBtn = document.getElementById("edit-btn");

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


const editUser = () => {
  window.location.href = "./update-user-data.html";
}


const renderUserProfile = (userData) => {
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
    <h3>Name: ${userData.name}</h3> 
    <p>Email: ${userData.data.email}</p>
    <p>Address: ${userData.data.address}</p>
  `;
  userContainer.replaceChildren();
  userContainer.append(card);
}


const handleUserProfileResult = (userResult) => {
  if(userResult.success){
    renderUserProfile(userResult.data);
  } else {
    showErrorAlert(`Error loading user data: ${userResult.error.details || userResult.error.message}`);
  }
}


const protectProfilePage = async ()  => {
  if(!redirectIfNotLoggedIn()){
    return;
  }

  const userId = getLoggedUserId();

  const userResult = await getUserById(userId);

  handleUserProfileResult(userResult);
}


const initProfilePage = async () => {
  await protectProfilePage();

  logoutBtn.addEventListener("click", logoutUser);

  editBtn.addEventListener("click", editUser);
}

initProfilePage();