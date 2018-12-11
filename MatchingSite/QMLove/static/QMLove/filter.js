$(document).ready(function () {
  console.log('filter.js updated and loaded')

  $('#submitFiltering').on('click', function(event) {
    var frm = $('#formFiltering');
      $.ajax({
        type: 'GET',
        url: '/search/',
        data: frm.serialize(),
        success: function(data) {
          $('body').html(data)
        },
        error: function(jqXHR, textStatus, error) {
          console.log(error);
        },
      });
      event.preventDefault();
  });


  $('.homelink').on('click', function(event) {
      $.ajax({
        type: 'GET',
        url: '/',
        success: function(data) {
          $('body').html(data)
        },
        error: function(jqXHR, textStatus, error) {
          console.log(error);
        },
      });
      event.preventDefault();
  });

  $('#search').on('click', function(event) {
      $.ajax({
        type: 'GET',
        url: '/search/',
        success: function(data) {
          $('body').html(data)
        },
        error: function(jqXHR, textStatus, error) {
          console.log(error);
        },
      });
      event.preventDefault();
  });

  $('#logout').on('click', function(event) {
      $.ajax({
        type: 'GET',
        url: '/logout/',
        success: function(data) {
          $('body').html(data)
        },
        error: function(jqXHR, textStatus, error) {
          console.log(error);
        },
      });
      event.preventDefault();
  });
});
