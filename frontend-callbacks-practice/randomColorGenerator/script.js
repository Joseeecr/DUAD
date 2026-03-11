const button = document.getElementById("change-color-btn")
const divBox = document.getElementById("div-box")
const colors = [
  { hex: "#FF5733", name: "orange" },
  { hex: "#33FF57", name: "green" },
  { hex: "#3357FF", name: "blue" },
  { hex: "#F5FF33", name: "yellow" },
  { hex: "#FF33F6", name: "pink" }
];


const checkIfClassExist = (className) =>{
  return document.querySelector(`.${className}`);
};


const showColor = (color) =>{

  if(!checkIfClassExist("text")){
    const text = document.createElement("p");
    text.className = "text";
    divBox.append(text);
  }

  const textElement = checkIfClassExist("text");  
  textElement.innerHTML = color.name;
}


const changeColor = (callback) =>{
  const color = Math.floor(Math.random() * colors.length);
  console.log(colors[color].name);
  const randomColor = colors[color];
  divBox.style.backgroundColor = randomColor.hex;
  
  callback(randomColor);
}


button.addEventListener("click", () => {
  changeColor(showColor);
});