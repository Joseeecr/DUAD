const promise1 = fetch("https://pokeapi.co/api/v2/pokemon/1").then((response) => response.json()).then((data) => {console.log(data.name)});
const promise2 = fetch("https://pokeapi.co/api/v2/pokemon/2").then((response) => response.json()).then((data) => {console.log(data.name)});
const promise3 = fetch("https://pokeapi.co/api/v2/pokemon/3").then((response) => response.json()).then((data) => {console.log(data.name)});



const test = Promise.all([promise1, promise2, promise3]);


