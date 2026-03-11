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


const showNames = (name) => {
  console.log("Match found:", name);
}

const repeatedNames = (array1, array2, callBack) => {
  for(const name1 of array1){
    for(const name2 of array2){
      if(name1 === name2) {
        callBack(name1);
      }
    }
  }
}

repeatedNames(names1, names2, showNames);