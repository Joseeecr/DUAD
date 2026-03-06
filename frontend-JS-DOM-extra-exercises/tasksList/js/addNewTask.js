function checkIfClassExist(className){
  return document.querySelector(`.${className}`);
};


function isEmpty(task) {
  const isEmptyValue = !task.trim();

  if(isEmptyValue){
    alert("You must enter some text");
  }

  return isEmptyValue;
};


function createElementIfNotExist(className, button){
  if (!checkIfClassExist(className)){
    const list = document.createElement("ul");
    list.className = className;
    button.after(list);
  }
};


function addListContainer(className){
  const list = checkIfClassExist(className);

  const listContainer = document.createElement("div");
  listContainer.className = "list-container";
  list.append(listContainer);
  return listContainer;
};


function addListItem(task){
  const listContainer = addListContainer("tasks-list");

  const item = document.createElement("li");
  item.className = "item-list"
  item.innerHTML = task.value;

  const buttonToRemoveItem = document.createElement("button");
  buttonToRemoveItem.className = "button-to-remove-item";
  buttonToRemoveItem.innerHTML = "Click to delete task";

  listContainer.append(item);
  listContainer.append(buttonToRemoveItem);
};


function addNewTask(task, button){

  if(isEmpty(task.value)){
    return;
  }

  createElementIfNotExist("tasks-list", button);

  addListItem(task);
};


function init(){
  const button = document.getElementById("add-task-btn");
  const taskInput = document.getElementById("task-input");

  button.addEventListener("click", () => {
    addNewTask(taskInput, button);
  });
};

init();