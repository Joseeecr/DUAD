const getElement = (element) => {
  return document.getElementById(element);
} 


const chooseColor = (colors) => {
  const color = Math.floor(Math.random() * colors.length);
  return colors[color];
}


const setColor = (element) => {
  const colors = ["red", "blue", "green", "yellow", "cyan", "pink"];
  const color = chooseColor(colors);

  for(const word of colors){
    if(element.classList.contains(word)){
      element.classList.remove(word);
    }
  }

  element.classList.add(color);
}


const changeColor = () => {
  const element = getElement("text-to-change");
  setColor(element);
}



function init(){
  const changeColorBtn = document.getElementById("change-text-color-btn");
  changeColorBtn.addEventListener("click", changeColor); 
}

init()