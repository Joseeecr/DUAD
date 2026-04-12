const { default: axios } = require("axios");

const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


async function createUser(name, email, password, address) {
  try {
    const response = await axios.post("https://api.restful-api.dev/objects", {
        name: name,
        data: {
          email: email,
          password: password,
          address: address
        }
      });
    if (!response.status >= 200 && response.status < 300 ) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: response.statusText,
        status: response.status
      });
    }

    return formatResponse(true, response, null);

  } catch (error) {
    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}

const init = async () => {
  const user = (await createUser("Jose1", "test@domain.com", "abc123", "New York"));
  console.log(user.data.data)
}

init()
