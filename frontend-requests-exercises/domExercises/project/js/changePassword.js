import { getUserById } from "./services/userService.js";
import { updateUserData } from "./services/userService.js";

const changePasswordForm = document.getElementById("change-password-form");


const changePassword =  () => {
  changePasswordForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    const userId  = changePasswordForm.elements["userId"].value.trim();
    const currentPassword  = changePasswordForm.elements["currentPassword"].value.trim();
    const newPassword  = changePasswordForm.elements["newPassword"].value.trim();
    const confirmPassword  = changePasswordForm.elements["confirmPassword"].value.trim();

    const userData = await getUserById(userId);

    if(!userData.success && userData.error.type === "NETWORK_ERROR"){
      alert("Something went wrong")
      return;
    }

    if(!userData.success){
      alert("User id incorrect");
      return;
    }

    if(currentPassword !== userData.data.data.password){
      alert("Password incorrect");
      return;
    }

    if(newPassword !== confirmPassword){
      alert("Passwords do not match");
      return;
    }

    await updateUserData(userId, {
        email: userData.data.data.email,
        password: newPassword,
        address: userData.data.data.address
    });

    window.location.href = "./login.html";
  });
};

changePassword();