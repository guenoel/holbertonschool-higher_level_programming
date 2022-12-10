#!/usr/bin/node
/*
add
*/

function facto (a) {
  res = 1
  for (i = 0; i < a; i++) {
    res *= (i + 1);
  }
  return res;
  }
  
  console.log(facto(parseInt(process.argv[2])));
  