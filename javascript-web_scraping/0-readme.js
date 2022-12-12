#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], function (err, toto) {
  if (err) {
    console.log(err);
  }
  console.log(toto.toString());
});
