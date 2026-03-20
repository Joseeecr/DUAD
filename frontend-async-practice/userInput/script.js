function checkIfClassExist(className){
  return document.querySelector(`.${className}`);
};


function isEmpty(userId) {
  const isEmptyValue = !userId.trim();

  if(isEmptyValue){
    return true;
  }
  return isEmptyValue;
};


function createElementIfNotExist(element, className){
  const existentClass = checkIfClassExist(className);
  if(existentClass){
    return existentClass;
  }else{
    const newElement = document.createElement(element);
    newElement.className = className;
    return newElement;
  }
};


const getUserInput = () => {
  const userInput = document.getElementById("user-input");

  return userInput.value;
}


const displayUserInfo = (user) => {
  const userInfo = createElementIfNotExist("div", "user-info");
  const button = document.getElementById("send-button")
  
  button.after(userInfo);

  userInfo.innerHTML = `<b>First name:</b> ${user.first_name} <br> <b>Last name:</b> ${user.last_name} <br> <b>Email:</b> ${user.email}`;
}


async function showUser() {
  const userId = getUserInput();

  if(isEmpty(userId)){
    alert("Enter a valid user id");
    return;
  }

  try {

    const response = await fetch(`https://reqres.in/api/users/${userId}`, {
      headers:{
        "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
      }
    });

    if (!response.ok){
      throw("User not found");
    }

    const result = await response.json();
    displayUserInfo(result.data);

  }catch(e){
    alert(e)
  }
}


function init(){
  const sendButton = document.getElementById("send-button");

  sendButton.addEventListener("click", () =>{
    showUser()
  })
}


init()