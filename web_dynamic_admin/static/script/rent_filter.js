$(function () {
  const rentCheckbox = $('.rent-checkbox');
  let checkedType;

  rentCheckbox.on('change', function () {
    // Makes sure only 1 checkbox is checked at a time
    $('.rent-checkbox').not(this).prop('checked', false);
    
    if ($(this).is(':checked')) {
      checkedType = $(this).data('name');
    } else {
      checkedType = '';
    }
    // update the h4 element with the checked type
    $('.rent-type h4').text(checkedType);
  });

  $('.filters button').on('click', function() {
    $('.rent-list').each(function () {
      let rentType = $(this).data('type');
      if (!checkedType) {
        $(this).removeAttr('style');
      } else {
        if (rentType !== checkedType) {
          $(this).css('display', 'none');
        } else {
          $(this).removeAttr('style');
        }
      }
    });
  });
});
