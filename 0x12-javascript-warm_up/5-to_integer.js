#!/usr/bin/node

const inNumber = process.argv[2];

if ((!isNaN(parseInt(inNumber)))) {
  console.log(`My number: ${parseInt(inNumber)}`);
} else {
  console.log('Not a number');
}
