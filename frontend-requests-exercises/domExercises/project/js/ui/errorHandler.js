export const showErrorElement = (element ,message) => {
  element.textContent = message;
}


export const showErrorAlert = (message) => {
  alert(message);
}

export const clearError = (element) => {
  element.textContent = "";
}