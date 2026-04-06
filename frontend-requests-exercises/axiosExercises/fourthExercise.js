const { default: axios } = require("axios");

const userInstance = axios.create({
  baseURL: "https://api.restful-api.dev/collections/user/objects",
  headers: {
    "x-api-key": "00053352-bbae-4292-9162-72082d42b80b"
  }
});

const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


const getUserById = async (userId) => {
  try {
    const response = await userInstance.get(`/${userId}`);

    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: error.response.statusText,
        status: error.response.status,
        details: error.response.data.error
      });
    }

    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}


const updateUserData = async (userId, data) => {
  try {
    const response = await userInstance.put(`/${userId}`, {data});
    return formatResponse(true, response.data, null);

  } catch (error) {
    if (error.response) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: error.response.statusText,
        status: error.response.status,
        details: error.response.data.error
      });
    }

    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}


const handleUpdateUserAddress = async (userId, newAddress) => {
  const user =  await getUserById(userId);
  console.log(user)
  if(!user.success){
    return user;
  }


  const currentData = user.data.data;

  const newData = {
    email: currentData.email,
    password: currentData.password,
    address: newAddress
  };

  return await updateUserData(userId, newData);
}

const init = async () => {
  const result = await handleUpdateUserAddress("ff8081819d62221a019d6434d27b04d2", "otro");
  console.log(result)
}

init()