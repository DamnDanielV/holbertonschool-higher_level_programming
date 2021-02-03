#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  isNaN(parseInt(process.argv[2])) ? console.log('Not a number') : console.log(`My number: ${process.argv[2]}`);
}
