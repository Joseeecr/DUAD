const getUser = async (userId) => {
  const response = await fetch(`https://reqres.in/api/users/${userId}`, {
    headers: {
      "x-api-key": "reqres_c74b74633d994fcfa03b335248813bf7"
    }
  });

  const data = await response.json();
  return data;
};


const showResults = async () => {
  const user2 = await getUser(2)
  console.log(user2.data)
  const user3 = await getUser(3)
  console.log(user3.data)
  const user4 = await getUser(4)
  console.log(user4.data)
}

showResults()