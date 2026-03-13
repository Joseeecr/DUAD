const names1 = [
  "Ana",
  "Luis",
  "Carlos",
  "Maria",
  "Luis",
  "Sofia",
  "Ana",
  "Pedro"
];

const names2 = [
  "Sofia",
  "Jorge",
  "Carlos",
  "Elena",
  "Ana",
  "Jorge",
  "Luis",
  "Elena"
];


const showNames = (newArray) => {
  console.log(newArray);
}

const repeatedNames = (array1, array2, callBack) => {
  const newArray = [];

  for(const name1 of array1){
    if(array2.includes(name1) && !newArray.includes(name1)){
      newArray.push(name1);
    }
  }
  callBack(newArray)
}

repeatedNames(names1, names2, showNames);