import { userInstance } from "./api/apiClient.js";

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


const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


const createUser = async (name, email, password, address) => {
  try {
    const response = await userInstance.post("collections/users/objects", {
        name: name,
        data: {
          email: email,
          password: password,
          address: address
        }
      });

    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {

      const details = error.response?.data?.error || error
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: error.response.statusText,
        status: error.response.status,
        details: details
      });
    }

    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
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

    const user = await createUser(name, email, password, address);

    if(user.success){
      alert(`User created successfully! Your id is ${user.data.id}`)
      localStorage.setItem("loggedUserId", user.data.id)
      window.location.href = './profile.html'
    }else {
      alert(`An error occurred while creating the user: ${user.error.details || user.error}`)
      console.log("Im details", user.error.details)
      console.log("Im error", user.error)
    }
  })
}

setupRegisterForm();


