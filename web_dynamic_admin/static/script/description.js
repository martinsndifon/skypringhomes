$(document).ready(function() {
  // Attach event listener to listing cards
  $('.listing-card').click(function() {
    // Get data attributes from the clicked listing card
    const id = $(this).data('id');
    const name = $(this).data('name');

    // Determine the route based on the data-name value
    let route = '';
    if (name === 'Rent') {
      route = 'rent';
    } else if (name === 'Sale') {
      route = 'sale';
    } else {
      route = 'service_apartments';
    }

    // Construct the URL with the route and id
    const url = 'http://127.0.0.1:3000/skyspringhomes/admin/' + route + '/' + id;

    // Open a new page with the constructed URL
    window.open(url, '_self');
  });
});
