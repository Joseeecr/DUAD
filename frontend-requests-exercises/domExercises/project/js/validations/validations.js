import { formatLabel } from "../utils/formatResponse.js";

export const isEmpty = (element) => {
  return element.trim() === "";
}


export const isEmailValid = (email) => {
  const validEmail = email.split("@");

  if((validEmail.length === 2) && (validEmail[0].length > 0) && (validEmail[1].length > 0)){
    return true;
  }

  return false;
}


export const isPasswordValid = (password) => {
  if(password.length >= 8){
    return true;
  }

  return false;
}


export const doPasswordsMatch = (password, confirmPassword) => {
  if(password === confirmPassword){
    return true;
  }
  return false;
}


export const validateRequiredFields = (inputValues) => {
  for(const item of inputValues){
    if(isEmpty(item.value)){
      return `${formatLabel(item.label)} should not be empty`;
    }
  }
  return null;
}