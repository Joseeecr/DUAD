import { validateRequiredFields } from "./validations/validations.js";
import { getSession } from "./auth/session.js";
import { getUserById } from "./services/userService.js";
import { showErrorElement, clearError } from "./ui/errorHandler.js";
import { updateUserData } from "./services/userService.js";

const editUserProfileForm = document.getElementById("edit-user-profile-form");
const errorMessage = document.getElementById("error-message");

const renderCurrentUserInfo = async () => {
  const session = getSession();
  const userData = await getUserById(session.userId);

  editUserProfileForm.elements["name"].value = userData.data.name
  editUserProfileForm.elements["address"].value = userData.data.data.address
}


const getEditUserProfileFormData = () => {
  const name  = editUserProfileForm.elements["name"].value.trim();
  const address  = editUserProfileForm.elements["address"].value.trim();

  return {
    name,
    address
  };
}


const validateEditUserProfileForm = ({name, address}) => {
  const inputValues = [
    {label: "name", value: name},
    {label: "address", value: address},
  ]

  const fieldsError = validateRequiredFields(inputValues);

  if(fieldsError){
    return fieldsError;
  }

  return null;
}


const handleEditUserProfileError = (userData) => {
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
  return "An error occurred while updating the profile"
}


const handleEditUserProfileSuccess = () => {
  alert("Data updated");
  window.location.href = "./profile.html";
}


const handleEditUserProfileSubmit = async (event) => {
  event.preventDefault();
  clearError(errorMessage);

  const formData = getEditUserProfileFormData();
  const formError = validateEditUserProfileForm(formData);

  if(formError){
    showErrorElement(errorMessage, formError);
    return;
  }
  const session = getSession();
  const userData = await getUserById(session.userId);

  const editUserDatadError = handleEditUserProfileError(userData);
  
  if(editUserDatadError){
    showErrorElement(errorMessage, editUserDatadError);
    return;
  }

  const editUserProfileResult = await updateUserData(userData.data.id, {
    name: formData.name,
    data: {
      email: userData.data.data.email,
      password: userData.data.data.password,
      address: formData.address
    }
  });

  const editUserProfileResultError = handleEditUserProfileError(editUserProfileResult);

  if(editUserProfileResultError){
    showErrorElement(errorMessage, editUserProfileResultError);
    return;
  }

  handleEditUserProfileSuccess();
}

const initUpdateProfilePage = async () => {
  await renderCurrentUserInfo();
  editUserProfileForm.addEventListener("submit", handleEditUserProfileSubmit);
}


initUpdateProfilePage();