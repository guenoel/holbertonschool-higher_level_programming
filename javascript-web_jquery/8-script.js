#!/usr/bin/node

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const res = data.results;
  for (const film of res) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  }
});
