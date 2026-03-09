document.addEventListener("click", function(event) {
  if (event.target.classList.contains("button-to-remove-item")){
    event.target.closest(".list-container").remove();
  }
});