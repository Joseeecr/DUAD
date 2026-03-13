const fs = require('fs');


fs.readFile('showHiddenMessage/firstText.txt', 'utf8', (error, data1) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  const words1 = data1.split("\r\n");
  const finalResult = []

  fs.readFile('showHiddenMessage/secondText.txt', 'utf8', (error, data2)=> {
    if (error) {
      console.error('Error reading file:', error);
      return;
    }

    const words2 = data2.split("\r\n");

    for(word of words1){
      if(words2.includes(word))
        finalResult.push(word)
    }

    console.log(finalResult.join(" "))
  });
});