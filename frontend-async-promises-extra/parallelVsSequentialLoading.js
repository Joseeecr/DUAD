function loadResource(resource, time) {
  const coolPromise = new Promise((resolve) => {
    setTimeout(() => resolve(resource), time)
  })
  return coolPromise
}


async function showParallelResults() {
  const arrayOfPromises = await Promise.all([loadResource("image1", 1000), loadResource("image2", 2000), loadResource("image3", 3000)])
  console.log(arrayOfPromises)
}


async function showSequentialResults() {
  const script1 = await loadResource("script1", 1000)
  console.log(script1)

  const script2 = await loadResource("script2", 2000)
  console.log(script2)

  const script3 = await loadResource("script3", 1000)
  console.log(script3)
}


async function init()  {
  await Promise.all([showParallelResults(), showSequentialResults()])
  console.log("All loaded")
}

init()