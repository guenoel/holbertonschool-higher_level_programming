#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  }
  const parsed = JSON.parse(body);
  const result = {};
  for (const task of parsed) {
    if (task.completed === true) {
      if (result[task.userId] === undefined) {
        result[task.userId] = 1;
      } else {
        result[task.userId] += 1;
      }
    }
  }
  console.log(result);
}
);
