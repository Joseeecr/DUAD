async function getUser() {
  try {
    const response = await fetch("https://reqres.in/api/users/23", {
      headers:{
        "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
      }
    });

    if (!response.ok){
      throw("User not found");
    }
    const result = await response.json();
    console.log(result.data);

  }catch(e){
    console.log(e)
  }
}


getUser();