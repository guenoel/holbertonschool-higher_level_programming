#!/usr/bin/node

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const key1 = data.name;
  $('#character').text(key1);
});
