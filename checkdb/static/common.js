/* global $ */
/* global bootstrap */

$(document).ready(function () {
  // ################## Activate tooltips
  // Grab array of all elements with 'data-bs-toggle="tooltip"' set
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  // Activate tooltips on all elements in the array
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })
  // ################## Activate DataTables
  $('div[data-activate-datatables="card"]').each(function () {
    const table = $(this).find('table')
    let aaSorting = []
    const sort = $(this).attr('data-datatables-ordering')
    if (sort === 'false') {
      aaSorting = []
    } else if (sort) {
      aaSorting = [[parseInt(sort), 'asc']]
    } else {
      aaSorting = [[0, 'asc']]
    }
    const dt = table.DataTable({
      paging: false,
      dom: 'ti',
      aaSorting
    })
    const search = $(this).find('input[data-activate-datatables="search"]')
    const clearButton = search.next('button')
    search.on('keyup', function () {
      dt.search($(this).val()).draw()
    })
    clearButton.on('click', function () {
      search[0].value = ''
      dt.search('').draw()
      search.focus()
    })
  })
  // ################## Detect if on mobile
  const width = (window.innerWidth > 0) ? window.innerWidth : screen.width
  window.isMobile = false
  if (width < 1000) {
    window.isMobile = true
  }
})
