import { userInstance } from "./api/apiClient.js";
const loginForm = document.getElementById("login-form");

const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


const getUserById = async (userId) => {
  try {
    const response = await userInstance.get(`collections/users/objects/${userId}`);
    
    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {
      const details = error.response?.data?.error || null

      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: error.response.statusText,
        status: error.response.status,
        details: details
      });
    }

    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}


const setupLoginForm =  () => {
  loginForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const userId  = loginForm.elements["user-id"].value.trim();
    const password  = loginForm.elements["password"].value.trim();
    const userData = await getUserById(userId);
    
    if(!userData.success){
      alert("Password or user id incorrect")
      return;
    }

    if(password !== userData.data.data.password){
      alert("Password or user id incorrect")
      return;
    }

    localStorage.setItem("loggedUserId", userData.data.id)
    window.location.href = "./profile.html"
  })
}

setupLoginForm();