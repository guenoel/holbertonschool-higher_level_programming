#!/usr/bin/node
const request = require('request');

const theURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(theURL, function (error, response) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }

  console.log(JSON.parse(response.body).title); // Print the response status code if a response was received
});
