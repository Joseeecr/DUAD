const formatResponse = (success, data, error) => {
  return {
    success,
    data,
    error
  }
}

const createUser = async (name, email, password, address) => {
  try {
    const response = await fetch("https://api.restful-api.dev/collections/user/objects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": "00053352-bbae-4292-9162-72082d42b80b"
      },
      body: JSON.stringify({
        name: name,
        data: {
          email: email,
          password: password,
          address: address
        }
      })
    });

    if (!response.ok) {
      return formatResponse(false, null, `${response.statusText} - ${response.status}`);
    }

    const result = await response.json();
    return formatResponse(true, result, null);

  } catch (error) {
    return formatResponse(false, null, error.message);
  }
}


const getUser = async (userId) => {
  try {
    const response = await fetch(`https://api.restful-api.dev/collections/user/objects/${userId}`, {
      headers: {
        "x-api-key": "00053352-bbae-4292-9162-72082d42b80b"
      }
    });

    if (response.status === 404) {
      return formatResponse(false, null, "User not found");
    }

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return formatResponse(true, result, null);

  } catch (error) {
    return formatResponse(false, null, error.message);
  }
}

const init = async () => {
  const user = await createUser("Jose1", "test@domain.com", "abc123", "New York");

  if(!user.success){
    console.log(user.error);
    return;
  }

  // const result = await getUser(user.data.id);
  const result = await getUser("1234");

  if (result.success){
    console.log(result.data);
  } else {
    console.log(result.error)
  }
}

init()