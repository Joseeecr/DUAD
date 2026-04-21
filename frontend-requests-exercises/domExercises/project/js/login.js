import { getUserById } from "./services/userService.js";
import { saveLoggedUserId } from "./auth/session.js";
import { validateRequiredFields, doPasswordsMatch } from "./validations/validations.js";
import { showErrorElement, clearError } from "./ui/errorHandler.js";
const loginForm = document.getElementById("login-form");
const errorMessage = document.getElementById("error-message");

const getLoginFormData = () => {
  const userId  = loginForm.elements["user-id"].value.trim();
  const password  = loginForm.elements["password"].value.trim();

  return {
    userId,
    password
  };
}


const validateLoginForm =  ({userId, password}) => {
  const inputValues = [
    {label: "userId", value: userId},
    {label: "password", value: password},
  ]

  const fieldsError = validateRequiredFields(inputValues);
  if(fieldsError){
    return fieldsError;
  }

  return null;
}


const validateLoginCredentials = (password, userData) => {

  if(!doPasswordsMatch(password, userData.data.data.password)){
    return "ID or password incorrect";
  }
  return null;
}


const handleLoginError = (userData) => {
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
    return "ID or password incorrect";
  }

  console.log(error);
  return "An error occurred while login"
}


const handleLoginSuccess = (userData) => {
  saveLoggedUserId(userData.data.id);
  window.location.href = './profile.html';
}


const handleLoginSubmit = async (event) => {
  event.preventDefault();
  clearError(errorMessage);

  const formData = getLoginFormData();

  const formError = validateLoginForm(formData);

  if(formError){
    showErrorElement(errorMessage, formError);
    return;
  }

  const userData = await getUserById(formData.userId);

  const loginError = handleLoginError(userData);

  if(loginError){
    showErrorElement(errorMessage, loginError);
    return;
  }

  const validateLoginCredentialsError = validateLoginCredentials(formData.password, userData);

  if(validateLoginCredentialsError){
    showErrorElement(errorMessage, validateLoginCredentialsError);
    return;
  }

  handleLoginSuccess(userData);
}


const setupLoginForm =  () => {
  loginForm.addEventListener("submit", handleLoginSubmit);
}

setupLoginForm();