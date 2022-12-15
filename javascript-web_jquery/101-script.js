#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
$('#add_item').click(function () {
  $('.my_list').append('<li>Item</li>');
});

$('#remove_item').click(function () {
  $('.my_list>li').first().remove();
});

$('#clear_list').click(function () {
  $('.my_list').empty();
});
})
