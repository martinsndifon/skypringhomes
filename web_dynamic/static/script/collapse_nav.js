$(document).ready(function() {
  $(".bars").on('click', function(e) {
    e.stopPropagation(); // Prevent the event from bubbling up

    $(".hidden").toggleClass("hidden-active");
  });
  
  // Hides the menu when any other part of the screen is clicked
  $(document).click(function(e) {
    if (!$(e.target).closest(".hidden").length) {
      $(".hidden").removeClass("hidden-active");
    }
  });
});
