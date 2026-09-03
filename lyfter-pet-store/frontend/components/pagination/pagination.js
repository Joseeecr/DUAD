export function createPagination(totalPages, currentPage) {

  let buttons = ""
  for (let page = 1; page <= totalPages; page += 1) {
    const active =
    page === currentPage
      ? 'active'
      : ''

    buttons += `<button data-page=${page} class="page ${active}">${page}</button>`;
  }

  return `
    <nav class="pagination">
      ${buttons}
    </nav>
  `
}