function isEvenWithFor(array){
  const evenNumbersArray = [];

  for (const element of array) {
    if (element % 2 === 0){
      evenNumbersArray.push(element);
    }
  }

  return evenNumbersArray;
}


function isEvenWithFilter(element){
  return element % 2 === 0;
}


const testingArray = [1,2,3,5,6,6,7,8,19,10,12,15,14];

const resultFunctionUsingFor = isEvenWithFor(testingArray);

const resultFunctionUsingFilter = testingArray.filter(isEvenWithFilter);

console.log(resultFunctionUsingFor);
console.log(resultFunctionUsingFilter);