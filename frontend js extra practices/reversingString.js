function reverseString(str){
  let word = ""

  for(let char = str.length -1; char >= 0; char--){
    word += str[char]
  }

  console.log(word);
}

reverseString("JavaScript")