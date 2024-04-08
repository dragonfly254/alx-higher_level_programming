#!/usr/bin/node

const size = process.argv[2];

if (!isNaN(parseInt(size))) {
  const sizeInt = parseInt(size);
  let square = '';

  for (let i = 0; i < sizeInt; i++) {
    let line = '';
    for (let j = 0; j < sizeInt; j++) {
      line += 'X ';
    }
    square += line + '\n';
  }

  console.log(square);
} else {
  console.log('Missing size');
}
