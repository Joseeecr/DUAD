function wait(seconds){
  const coolPromise = new Promise((resolve) =>{
    const miliseconds = seconds * 1000;
    setTimeout(() => resolve(`Ha pasado ${seconds} segundos`), miliseconds);
  })
  return coolPromise;
}


async function showResult(seconds) {
  const result = await wait(seconds);
  console.log(result);
}


async function init(){
  await showResult(2);
  await showResult(3);
  await showResult(1);
}

init();