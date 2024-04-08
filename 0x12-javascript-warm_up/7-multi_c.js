#!/usr/bin/node

const numOfOccurence = process.argv[2];

if ((isNaN(parseInt(numOfOccurence)))) {
  console.log('Missing number of occurrences');
}

if ((numOfOccurence > 0)) {
  for (let i = 0; i < numOfOccurence; i++) {
    console.log('C is fun');
  }
}
