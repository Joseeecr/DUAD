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


const createUser = async (name, email, password, address) => {
  try {
    const response = await userInstance.post("", {
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


const getUser = async (userId) => {
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


const init = async () => {
  const user = await createUser("Jose1", "test@domain.com", "abc123", "New York");

  if(!user.success){
    console.log(user.error);
    return;
  }

  const result = await getUser(user.data.id);
  // const result = await getUser("1234");

  if (result.success){
    console.log(result);
  } else {
    console.log(result.error)
  }
}


init()