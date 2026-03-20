function cleanInputField(){
  return document.getElementById("user-input").value = "";
}

function init(){
  const button = document.getElementById("send-button");
  button.addEventListener("click", cleanInputField);
}

init();