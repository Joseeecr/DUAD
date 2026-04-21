const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}


const getUserById = async (userId) => {
  try {
    const response = await fetch(`https://api.restful-api.dev/collections/user/objects/${userId}`, {
      headers: {
        "x-api-key": "00053352-bbae-4292-9162-72082d42b80b"
      }
    });

    if (!response.ok) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: response.statusText,
        status: response.status
      });
    }

    const result = await response.json();
    return formatResponse(true, result, null);

  } catch (error) {
    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}


const updateUserData = async (userId, data) => {
  try {
    const response = await fetch(`https://api.restful-api.dev/collections/user/objects/${userId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": "00053352-bbae-4292-9162-72082d42b80b"
      },

      body: JSON.stringify({
        data
      })
    });


    if (!response.ok) {
      return formatResponse(false, null, {
        type: "HTTP_ERROR",
        message: response.statusText,
        status: response.status
      });
    }

    const result = await response.json();
    return formatResponse(true, result, null);

  } catch (error) {
    return formatResponse(false, null, {
      type: "NETWORK_ERROR",
      message: error.message,
      status: null
    });
  }
}



const handleUpdateUserAddress = async (userId, newAddress) => {
  const user =  await getUserById(userId);

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


const result = await handleUpdateUserAddress("ff8081819d3fcc30019d4a318dc01238", "otro");

console.log(result)