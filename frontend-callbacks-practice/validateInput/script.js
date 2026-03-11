const positiveNumberCallBack = (number) => {
  console.log(`"Valid number: ${number}"`);
}


const zeroOrNegativeNumberCallBack = (number) => {
  console.log(`"Invalid  number: ${number}"`);
}


function validateInput(number, positiveCallBack, negativeCallBack){

  if(number > 0){
    positiveCallBack(number);
  }

  else{
    negativeCallBack(number)
  }
}


validateInput(1, positiveNumberCallBack, zeroOrNegativeNumberCallBack)