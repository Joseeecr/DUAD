
const fetchData = async () => {
  const response = await fetch("https://api.restful-api.dev/objects");
  const data = await response.json();
  return data;
}


const elementsWithData = async () => {
  const data = await fetchData();
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