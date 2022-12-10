#!/usr/bin/node
/*
value argument
*/

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  const argc = process.argv.slice(2).length;
  for (let i = 0; i < argc; i++) {
    console.log(process.argv[i + 2]);
  }
}
