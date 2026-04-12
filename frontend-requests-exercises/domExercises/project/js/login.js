import { getUserById } from "./services/userService.js";
import { saveLoggedUserId } from "./auth/session.js";
const loginForm = document.getElementById("login-form");


const setupLoginForm =  () => {
  loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const userId  = loginForm.elements["user-id"].value.trim();
    const password  = loginForm.elements["password"].value.trim();
    const userData = await getUserById(userId);
    
    if(!userData.success && userData.error.type === "NETWORK_ERROR"){
      alert("Something went wrong")
      return;
    }

    if(!userData.success){
      alert("Password or user id incorrect")
      return;
    }

    if(password !== userData.data.data.password){
      alert("Password or user id incorrect")
      return;
    }

    saveLoggedUserId(userData.data.id);
    window.location.href = "./profile.html";
  })
}

setupLoginForm();