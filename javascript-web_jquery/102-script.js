#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click(function () {
    code = $.param({ lang: $('INPUT#language_code').val() }) //change lang: en -> lang=en
    console.log(code)
    $.get('https://stefanbohacek.com/hellosalut/?' + code, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
