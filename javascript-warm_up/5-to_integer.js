#!/usr/bin/node
/*
integer
*/

const n = process.argv[2];

if (!isNaN(n)) {
  console.log('My number: %s', process.argv[2]);
} else {
  console.log('Not a number');
}
