const promise1 = fetch("https://pokeapi.co/api/v2/pokemon/10").then((response) => response.json()).then((data) => {console.log(`Promise 1: ${data.name}`); return data;});
const promise2 = fetch("https://pokeapi.co/api/v2/pokemon/15").then((response) => response.json()).then((data) => {console.log(`Promise 2: ${data.name}`); return data;});
const promise3 = fetch("https://pokeapi.co/api/v2/pokemon/1").then((response) => response.json()).then((data) => {console.log(`Promise 3: ${data.name}`); return data;});


Promise.any([promise1, promise2, promise3])
  .then((value) => {console.log(`The promise that was resolved first is: ${value.name}`)});