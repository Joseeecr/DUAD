import { getUserById } from "./services/userService.js";
import { updateUserData } from "./services/userService.js";
import { validateRequiredFields, doPasswordsMatch, isPasswordValid } from "./validations/validations.js";
import { showErrorElement, clearError } from "./ui/errorHandler.js";

const changePasswordForm = document.getElementById("change-password-form");
const errorMessage = document.getElementById("error-message");

const getChangePasswordFormData = () => {
  const userId  = changePasswordForm.elements["userId"].value.trim();
  const currentPassword  = changePasswordForm.elements["currentPassword"].value.trim();
  const newPassword  = changePasswordForm.elements["newPassword"].value.trim();
  const confirmPassword  = changePasswordForm.elements["confirmPassword"].value.trim();

  return {
    userId,
    currentPassword,
    newPassword,
    confirmPassword
  };
}


const validateChangePasswordForm =  ({userId, currentPassword, newPassword, confirmPassword}) => {
  const inputValues = [
    {label: "userId", value: userId},
    {label: "currentPassword", value: currentPassword},
    {label: "newPassword", value: newPassword},
    {label: "confirmPassword", value: confirmPassword},
  ]

  const fieldsError = validateRequiredFields(inputValues);
  if(fieldsError){
    return fieldsError;
  }

  return null;
}


const handleChangePasswordError = (userData) => {
  if(userData.success){
    return null;
  }

  const error = userData.error;
  
  if(error.type === "NETWORK_ERROR"){
    console.log(error);
    return "Something went wrong";
  }

  if(error.status === 403){
    console.log(error);
    return "Access denied";
  }

  if(error.status === 404){
    console.log(error);
    return "Requested resource was not found";
  }

  console.log(error);
  return "An error occurred while updating the password"
}


const validateCurrentPassword = (currentPassword, userData) => {
  if(!doPasswordsMatch(currentPassword, userData.data.data.password)){
    return "Current Password incorrect";
  }
  return null;
}


const validateNewPassword = (newPassword, confirmPassword) => {
  if(!doPasswordsMatch(newPassword, confirmPassword)){
    return "Passwords do not match";
  }
  
  if(!isPasswordValid(newPassword)){
    return "New password must be at least 8 characters long";
  }

  return null;
}


const handleChangePasswordSuccess = () => {
  alert("Password Changed! Your password has been changed successfully. Use your new password to log in.");
  window.location.href = "./login.html";
}


const handleChangePasswordSubmit = async (event) => {
  event.preventDefault();
  clearError(errorMessage);

  const formData = getChangePasswordFormData();

  const formError = validateChangePasswordForm(formData);

  if(formError){
    showErrorElement(errorMessage, formError);
    return;
  }

  const userData = await getUserById(formData.userId);

  const changePasswordError = handleChangePasswordError(userData);

  if(changePasswordError){
    showErrorElement(errorMessage, changePasswordError);
    return;
  }

  const validateCurrentPasswordError = validateCurrentPassword(formData.currentPassword, userData);

  if(validateCurrentPasswordError){
    showErrorElement(errorMessage, validateCurrentPasswordError);
    return;
  }

  const validateNewPasswordError = validateNewPassword(formData.newPassword, formData.confirmPassword);
  if(validateNewPasswordError){
    showErrorElement(errorMessage, validateNewPasswordError);
    return;
  }

  const updateUserDataResult = await updateUserData(formData.userId, {
    data: {
      email: userData.data.data.email,
      password: formData.newPassword,
      address: userData.data.data.address
    }
  });

  const updateUserDataResultError = handleChangePasswordError(updateUserDataResult);

  if(updateUserDataResultError){
    showErrorElement(errorMessage, updateUserDataResultError);
    return;
  }
  handleChangePasswordSuccess();
}


const setupChangePasswordForm =  () => {
  changePasswordForm.addEventListener("submit", handleChangePasswordSubmit);
}

setupChangePasswordForm();