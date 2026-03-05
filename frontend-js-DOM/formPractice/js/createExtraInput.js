function isChecked(button){
  return button.checked;
}


function checkIfClassExist(className){
  return document.querySelector(`.${className}`);
}


function createExtraInput(button, radioButtons){

  if(isChecked(button) && !checkIfClassExist("extra-input")){
    const newInput = document.createElement("input");
    newInput.className = "input-information extra-input";
    newInput.placeholder = "Enter your job";
    newInput.required = true;
    radioButtons.after(newInput);
  }
}


function removeExtraInput(button){
  const elementToRemove = checkIfClassExist("extra-input"); 
  if(isChecked(button) && elementToRemove){
    elementToRemove.remove();
  }
}


function init(){

  const employedRadioButton = document.getElementById("employed");
  const unemployedRadioButton = document.getElementById("unemployed");
  const isEmployedRadioButtons = document.getElementById("is-employed-radio-buttons");

  employedRadioButton.addEventListener("click", () => {
    createExtraInput(employedRadioButton, isEmployedRadioButtons);
  });

  unemployedRadioButton.addEventListener("click", () => {
    removeExtraInput(unemployedRadioButton);
  });
}

init();