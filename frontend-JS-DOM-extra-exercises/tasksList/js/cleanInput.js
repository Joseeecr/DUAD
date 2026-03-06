function cleanInputField(){
  return document.getElementById("task-input").value = "";
}

function init(){
  const button = document.getElementById("add-task-btn");
  button.addEventListener("click", cleanInputField);
}

init();