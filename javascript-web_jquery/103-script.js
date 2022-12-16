#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
    $('INPUT#btn_translate').click(function () {
      code = $.param({ lang: $('INPUT#language_code').val() }) //change lang: en -> lang=en
      $.get('https://stefanbohacek.com/hellosalut/?' + code, function (data) {
        $('#hello').text(data.hello);
      });
    });
    $(document).keypress(function (e) {
        if (e.which === 13) {
          code = $.param({ lang: $('INPUT#language_code').val() })
          $.get('https://stefanbohacek.com/hellosalut/?' + code, function (data) {
        $('#hello').text(data.hello);
      });
    }});
  });
