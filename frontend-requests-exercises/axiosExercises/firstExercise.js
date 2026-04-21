const { default: axios } = require("axios");

const getData = async () => {
  const response = await axios.get("https://api.restful-api.dev/objects");
  return response.data;
}


const elementsWithData = async () => {
  const data = await getData();
  return data.filter((element) => element.data);
}


const createString = async () => {
  const elements = await elementsWithData();
  for(const element of elements){
    const entries = Object.entries(element.data);
    const printFormattedList = entries.map((item) => `${item[0]}: ${item[1]}`);
    console.log(`${element.name} (${printFormattedList.join(", ")})`);
  }
  
}

createString()