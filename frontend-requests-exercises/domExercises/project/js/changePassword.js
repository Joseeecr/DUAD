import { userInstance } from "./api/apiClient.js";
const changePasswordForm = document.getElementById("change-password-form");


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
      const details = error.response?.data?.error || error

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


const updateUserData = async (userId, data) => {
  try {
    const response = await userInstance.patch(`collections/users/objects/${userId}`, {data});
    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: error.response.statusText,
        status: error.response.status,
        details: error.response.data.error
      });
    }

    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}



const changePassword =  () => {
  changePasswordForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const userId  = changePasswordForm.elements["userId"].value.trim();
    const currentPassword  = changePasswordForm.elements["currentPassword"].value.trim();
    const newPassword  = changePasswordForm.elements["newPassword"].value.trim();
    const confirmPassword  = changePasswordForm.elements["confirmPassword"].value.trim();

    const userData = await getUserById(userId);
    
    if(!userData.success){
      alert("User id incorrect")
      return;
    }

    if(currentPassword !== userData.data.data.password){
      alert("Password incorrect")
      return;
    }

    if(newPassword !== confirmPassword){
      alert("Passwords do not match")
      return;
    }

    await updateUserData(userId, {
        email: userData.data.data.email,
        password: newPassword,
        address: userData.data.data.address
    })

    window.location.href = "./login.html"
  })
}

changePassword();