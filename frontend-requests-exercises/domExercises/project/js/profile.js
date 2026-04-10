const userInstance = axios.create({
  baseURL: "https://api.restful-api.dev/",
  headers:{
    "x-api-key": "77adaabc-9a83-469f-baaa-9973f9b8a14c"
  }
});
const userContainer = document.getElementById("user-container");
const logoutBtn = document.getElementById("logout-btn");

const isUserLoggedIn = () => {
  return Boolean(localStorage.getItem("loggedUserId"));
}


const getLoggedUserId = () => {
  return localStorage.getItem("loggedUserId");
}


const redirectIfNotLoggedIn = () => {
  if(!isUserLoggedIn()){
    window.location.href = "./login.html";
    return false
  }
  return true
}


const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


const getUserById = async (userId) => {
  try {
    const response = await userInstance.get(`collections/users/objects/${userId}`);
    
    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {
      const details = error.response?.data?.error || null

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


const logoutUser = () => {
  localStorage.removeItem("loggedUserId");
  window.location.href = "./login.html";
}

const protectProfilePage = async ()  => {
  if(!redirectIfNotLoggedIn()){
    return;
  }

  const userId = getLoggedUserId();

  const userData = await getUserById(userId);

  if(userData.success){
  const card = document.createElement("div");
  card.className = "card";
  card.innerHTML = `
  <h3>Name: ${userData.data.name}</h3> 
  <p>Email: ${userData.data.data.email}</p>
  <p>Address: ${userData.data.data.address}</p>
  `;
  userContainer.replaceChildren();
  userContainer.append(card);
  } else {
    alert(`Error loading user data: ${user.error.details || user.error.message}`)
  }
}


async function initProfilePage() {
  await protectProfilePage();
  logoutBtn.addEventListener("click", logoutUser);
}

initProfilePage();