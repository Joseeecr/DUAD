const user = fetch("https://reqres.in/api/users/2", {
    headers: {
      "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
    }
  });

user.then((response) => { 
  return response.json();
}).then((data) => {
  console.log(data.data);
});