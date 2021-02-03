#!/usr/bin/node
m1 = 'No argument';
m2 = 'Argument found';
m3 = 'Arguments found';
const imprime = (text) => console.log(text);

if (process.argv.length === 2) {
  imprime(m1);
} else {
  process.argv.length === 3 ? imprime(m2) : imprime(m3);
}
