const buttonToDisplay = document.getElementById("display-information");


function isEmpty(textToDisplay) {
  const isEmptyValue = !textToDisplay.trim();
  if(isEmptyValue){
    alert("You must enter some text");
  }
  return isEmptyValue;
}


function checkIfClassExist(className){
  return document.querySelector(`.${className}`);
}


function createElementIfNotExist(className, buttonToDisplay){
  if (!checkIfClassExist(className)){
    const item = document.createElement("p");
    item.className = className;
    buttonToDisplay.after(item);
  }
} 


function addText(textToDisplay, className){
  const element = checkIfClassExist(className);
  element.innerHTML = textToDisplay;
}


function cleanInputField(){
  return document.getElementById("input-information").value = "";
}


const userInput = () => {
  const textToDisplay = document.getElementById("input-information").value;

  if(isEmpty(textToDisplay)){
    return;
  }

  createElementIfNotExist("userText", buttonToDisplay);

  addText(textToDisplay, "userText");

  cleanInputField();
}


buttonToDisplay.addEventListener("click", userInput);