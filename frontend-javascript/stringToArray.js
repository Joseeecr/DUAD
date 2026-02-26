function isLetter(char){
  return /^[a-zA-Z]$/.test(char);
}

function stringToArray(sentence){
  let currentWord = "";
  const wordsArray = [];

  for (const char of sentence)

    if (!isLetter(char)) {
      wordsArray.push(currentWord);
      currentWord = "";
    }

    else {
      currentWord += char;
    }

    if (currentWord){
      wordsArray.push(currentWord);
    }

    return wordsArray;
}

const sentence = "This is a string!";

const result = stringToArray(sentence);

console.log(result)