#!/usr/bin/node

const argsc = process.argv.length - 2;

if (argsc === 0) {
  console.log('No argument');
} else if (argsc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
