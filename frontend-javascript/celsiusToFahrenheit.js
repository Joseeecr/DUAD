function celsiusToFahrenheit(celsiusDegrees){
  return (celsiusDegrees * 1.8) + 32; 
}

const arrayDegrees = [10, 20, 30];

const result = arrayDegrees.map(celsiusToFahrenheit);

console.log(result);