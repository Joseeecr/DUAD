import { createUser } from "./services/userService.js";
import { saveSession } from "./auth/session.js";
import { validateRequiredFields, isEmailValid, isPasswordValid, doPasswordsMatch } from "./validations/validations.js";
import { showErrorElement, clearError } from "./ui/errorHandler.js";

const form = document.getElementById("register-form");
const errorMessage = document.getElementById("error-message");


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
    {label: "name", value: name},
    {label: "email", value: email},
    {label: "password", value: password},
    {label: "confirmPassword", value: confirmPassword},
    {label: "address", value: address},
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
  saveSession(userData.data.id);
  window.location.href = './profile.html';
}


const handleRegisterSubmit = async (event) => {
  event.preventDefault();
  clearError(errorMessage);

  const formData = getRegisterFormData();

  const error = validateRegisterForm(formData);

  if(error){
    showErrorElement(errorMessage, error);
    return;
  }

  const userData = await createUser(formData.name, formData.email, formData.password, formData.address);

  const registerError = handleRegisterError(userData);

  if(registerError){
    showErrorElement(errorMessage, registerError)
    return;
  }

  handleRegisterSuccess(userData)
}


const setupRegisterForm =  () => {
  form.addEventListener("submit", handleRegisterSubmit)
}

setupRegisterForm();