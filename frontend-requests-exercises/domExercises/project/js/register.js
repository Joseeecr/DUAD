import { createUser } from "./services/userService.js";
const form = document.getElementById("register-form");


const isEmpty = (element) => {
  return element.trim() === "";
}


const areFieldsValid = (inputValues) => {
  for(const item of inputValues){
    if(isEmpty(item.value)){
      alert(`${item.label} should not be empty`);
      return false;
    }
  }
  return true;
}


const isEmailValid = (email) => {
  const validEmail = email.split("@");

  if((validEmail.length === 2) && (validEmail[0].length > 0) && (validEmail[1].length > 0)){
    return true;
  }

  return false;
}


const isPasswordValid = (password) => {
  if(password.length >= 8){
    return true;
  }

  return false;
}


const doPasswordsMatch = (password, confirmPassword) => {
  if(password === confirmPassword){
    return true;
  }
  return false;
}


const setupRegisterForm =  () => {
  form.addEventListener("submit", async function(event) {
    event.preventDefault();
    const name  = form.elements["name"].value.trim();
    const email  = form.elements["email"].value.trim();
    const password  = form.elements["password"].value.trim();
    const confirmPassword  = form.elements["confirmPassword"].value.trim();
    const address  = form.elements["address"].value.trim();

    const inputValues = [
      {label: "Name", value: name},
      {label: "Email", value: email},
      {label: "Password", value: password},
      {label: "Confirm Password", value: confirmPassword},
      {label: "Address", value: address},
    ]

    if(!areFieldsValid(inputValues)){
      return;
    }

    if(!isEmailValid(email)){
      alert("Invalid email structure. Use something like this 'email@example.com'")
      return;
    }

    if(!isPasswordValid(password)){
      alert("Password must be at least 8 characters long")
      return;
    }

    if(!doPasswordsMatch(password, confirmPassword)){
      alert("Passwords do not match")
      return;
    }

    const userData = await createUser(name, email, password, address);


    if(!userData.success && userData.error.type === "NETWORK_ERROR"){
      alert("Something went wrong")
      return;
    }

    if(!userData.success){
      alert(`An error occurred while creating the user: ${user.error.details || user.error}`)
      return;
    }

    alert(`User created successfully! Your id is ${userData.data.id}`)
    localStorage.setItem("loggedUserId", userData.data.id)
    window.location.href = './profile.html'
  })
}

setupRegisterForm();