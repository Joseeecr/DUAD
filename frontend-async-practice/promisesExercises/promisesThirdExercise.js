const words = ["very", "dogs", "cute", "are"];

const times = {
  "very": 3000,
  "dogs": 1000,
  "cute": 4000,
  "are": 2000
};

const coolPromise = words.map((word) => 
  new Promise((resolve) => setTimeout(() => resolve(word), times[word]))
)

const resultado = [];

coolPromise.forEach((promise) => {
  promise.then((word) =>{
    resultado.push(word);

    if (resultado.length === words.length){
      console.log(resultado.join(" "));
    }
  });
});