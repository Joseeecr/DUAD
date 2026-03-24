async function getUser() {
  const response = await fetch("https://reqres.in/api/users/2", {
    headers: {
      "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
    }
  });

  const result = await response.json();
  console.log(result.data);
}


getUser();