function evenMessage(){
    console.log("The number is even!");
}


function oddMessage(){
    console.log("The number is odd!");
}


function main(number, callBackEven, callBackOdd){
  if (number % 2 === 0){
    callBackEven(number);
  }
  else{
    callBackOdd(number);
  }
}

main(1, evenMessage, oddMessage);