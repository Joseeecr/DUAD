const user = fetch("https://reqres.in/api/users/23", {
    headers: {
      "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
    }
  });

user.then((response) => { 
  if(!response.ok){
    throw("User not found");
  }
  return response.json();
  }).then((data) => {
    console.log(data.data);
  }).catch((error) => {
    console.log(error);
});