#!/usr/bin/node
const n = parseInt(process.argv[2]);
const imprime = (times) => {
    if (times == 0) {
        console.log('Missing number of occurrences');
    }
    let i = 0;
    while (i < times) {
        console.log('C is fun');
        i = i + 1;
    }
}
isNaN(n) ? imprime(0) : imprime(n);
