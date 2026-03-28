const getUser = async (userId) => {

    const response = await fetch(`https://reqres.in/api/users/${userId}`, {
      headers: {
        "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
      }
    });

    if (!response.ok){
      throw("An error occured");
    }

    const data = await response.json();
    return data;
};


const showResults = async () => {
  try{
    const user2 = await getUser(2)
    console.log(user2.data)
    const user3 = await getUser(3)
    console.log(user3.data)
    const user4 = await getUser(43)
    console.log(user4.data)
  }catch(e){
    console.log(e)
  }

}

showResults()