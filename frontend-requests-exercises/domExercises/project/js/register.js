import { createUser } from "./services/userService.js";
import { saveLoggedUserId } from "./auth/session.js";
import { isEmpty, isEmailValid, isPasswordValid, doPasswordsMatch } from "./validations/validations.js";
const form = document.getElementById("register-form");
const errorMessage = document.getElementById("error-message");


const showError = (message) => {
  errorMessage.textContent = message;
}


const clearError = () => {
  errorMessage.textContent = "";
}


const validateRequiredFields = (inputValues) => {
  for(const item of inputValues){
    if(isEmpty(item.value)){
      return `${item.label} should not be empty`;
    }
  }
  return null;
}


const getRegisterFormData = () => {
  const name  = form.elements["name"].value.trim();
  const email  = form.elements["email"].value.trim();
  const password  = form.elements["password"].value.trim();
  const confirmPassword  = form.elements["confirmPassword"].value.trim();
  const address  = form.elements["address"].value.trim();

  return {
    name,
    email,
    password,
    confirmPassword,
    address
  };
}


const validateRegisterForm = ({name, email, password, confirmPassword, address}) => {
  const inputValues = [
    {label: "Name", value: name},
    {label: "Email", value: email},
    {label: "Password", value: password},
    {label: "Confirm Password", value: confirmPassword},
    {label: "Address", value: address},
  ]

  const fieldsError = validateRequiredFields(inputValues);

  if(fieldsError){
    return fieldsError;
  }

  if(!isEmailValid(email)){
    return "Invalid email structure. Use something like this 'email@example.com'";
  }

  if(!isPasswordValid(password)){
    return "Password must be at least 8 characters long";
  }

  if(!doPasswordsMatch(password, confirmPassword)){
    return "Passwords do not match";
  }

  return null;
}


const handleRegisterError = (userData) => {

  if(!userData.success && userData.error.type === "NETWORK_ERROR"){
    return "Something went wrong";
  }

  if(!userData.success){
    return `An error occurred while creating the user: ${userData.error.details || userData.error.message}`;
  }

  return null;
}


const handleRegisterSuccess = (userData) => {
  alert(`User created successfully! Your id is ${userData.data.id}`);
  saveLoggedUserId(userData.data.id);
  window.location.href = './profile.html';
}


const handleRegisterSubmit = async (event) => {
  event.preventDefault();
  clearError();

  const formData = getRegisterFormData();

  const error = validateRegisterForm(formData);

  if(error){
    showError(error);
    return;
  }

  const userData = await createUser(formData.name, formData.email, formData.password, formData.address);

  const registerError = handleRegisterError(userData);

  if(registerError){
    showError(registerError)
    return;
  }

  handleRegisterSuccess(userData)
}


const setupRegisterForm =  () => {
  form.addEventListener("submit", handleRegisterSubmit)
}

setupRegisterForm();