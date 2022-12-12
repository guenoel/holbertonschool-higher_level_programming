#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  const parsing = JSON.parse(body);
  let count = 0;
  for (const elem of parsing.results) {
    for (const people of elem.characters) {
      if (people === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
}
);
