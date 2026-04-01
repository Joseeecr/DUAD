async function createUser(name, email, password, address) {
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
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const result = await response.json();
    console.log("Success:", result);
    return result;

  } catch (error) {
    console.error("Error:", error);
  }
}

const init = async () => {
  await createUser("Jose1", "test@domain.com", "abc123", "New York");
}

init()
