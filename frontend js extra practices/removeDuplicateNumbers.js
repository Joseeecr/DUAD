function removeDuplicates(array){
  const newArray = [];

  for(const number of array){
    if (!newArray.includes(number))
      newArray.push(number);
  }

  return newArray
}


const array = [1,2,3,2,4,1,5];
const newArray = removeDuplicates(array);

console.log(newArray)
