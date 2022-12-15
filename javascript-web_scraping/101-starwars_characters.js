#!/usr/bin/node
const request = require('request');

const theURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(theURL, async function (error, response) {
  if (error) { console.error('error:', error); }
  const listURL = JSON.parse(response.body).characters;
  for (const URLchar of listURL) {
    await new Promise((resolve, reject) => {
      request(URLchar, function (error, response) {
        if (error) { reject(error); }
        console.log(JSON.parse(response.body).name);
        resolve();
      });
    });
  }
});
