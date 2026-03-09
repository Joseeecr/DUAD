function addNum(num){
  num.innerHTML = Number(num.innerHTML) + 1;
}

function subNum(num){
  if(Number(num.innerHTML) > 0){
    
    num.innerHTML = Number(num.innerHTML) - 1;
  }
}


function init(){
  const addBtn = document.getElementById("addbtn");
  const subBtn = document.getElementById("subbtn");
  const number = document.getElementById("number");
  
  addBtn.addEventListener("click", () =>{
    addNum(number);
  });

  subBtn.addEventListener("click", () =>{
    subNum(number);
  });
}

init();