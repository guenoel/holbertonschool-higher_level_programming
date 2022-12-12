#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }

  const thetext = response.body; // Print the response status code if a response was received

  fs.writeFile(
    process.argv[3],
    thetext,
    function (err) {
      if (err) {
        return console.error(err);
      }
    });
});
