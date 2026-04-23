const apiUrlInstance = axios.create({
  baseURL: "https://api.restful-api.dev/",
});

const nextPage = document.getElementById("next-page");
const previousPage = document.getElementById("previous-page");
const elementsContainer =  document.getElementById("elements-container");

const getElements = async () => {
  try {
    const response = await apiUrlInstance.get("objects");
    
    return response.data;

  } catch (error) {
    console.log(error.response || error);
    return error.response || error;
  };
}


const startPagination = (currentPage, itemsPerPage) => {
  return (currentPage - 1) * itemsPerPage;
}


const endPagination = (startPagination, itemsPerPage) => {
  return startPagination + itemsPerPage;
}


const calculateTotalPages = (data, itemsPerPage) => {
  return Math.ceil(data.length / itemsPerPage);
}



const renderElements = (element) => {
  const listItem = document.createElement("li");
  listItem.className = "list-element";
  listItem.innerHTML = `Name: ${element.name}`;
  elementsContainer.append(listItem);
}


const renderCurrentPage = (data, currentPage, itemsPerPage) => {
  const startPage = startPagination(currentPage, itemsPerPage);
  const endPage = endPagination(startPage, itemsPerPage);
  elementsContainer.replaceChildren();
  data.slice(startPage, endPage).forEach(item => renderElements(item));
}


const pagination = async () => {
  const data = await getElements();
  const itemsPerPage = 5;
  let currentPage  = 1;
  const totalPages = calculateTotalPages(data, itemsPerPage);
  renderCurrentPage(data, currentPage, itemsPerPage);

  nextPage.addEventListener("click", () => {
    if(currentPage < totalPages){
      currentPage += 1;
      console.log(`page ${currentPage}`)
      renderCurrentPage(data, currentPage, itemsPerPage)
    }
  });

  previousPage.addEventListener("click", () => {
    if(currentPage > 1){
      currentPage -= 1;
      console.log(`page ${currentPage}`);
      renderCurrentPage(data, currentPage, itemsPerPage);
    }
  });
}

pagination();