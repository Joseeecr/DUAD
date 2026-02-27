function isLetter(char){
  return /^[a-zA-Z]$/.test(char);
}


function cleaningSentence(sentence){
  let currentWord = "";
  const wordsArray = [];

  for (const char of sentence){
    if (isLetter(char)) {
      currentWord += char;
      continue;
    }

    if (currentWord){
      wordsArray.push(currentWord);
      currentWord = "";
    }
  }

  if (currentWord){
    wordsArray.push(currentWord);
  }

  return wordsArray;
}


function wordsCounter(sentence){
  const counter = {};

  const wordsArray = cleaningSentence(sentence);

  for(const word of wordsArray){
    if(!(word.toLowerCase() in counter)){
      counter[word.toLowerCase()] = 1;
    }
    else{
      counter[word.toLowerCase()] += 1;
    }
  }

  return counter;
}

const result = wordsCounter("This is a test. This test is simple.");

console.log(result);