#!/usr/bin/node
const n = parseInt(process.argv[2])
const imprime = (times)=> {
    if (times == 0) {
        console.log('Missing size')
    }
    for (let i = 0; i < times; i++) {
        console.log('X'.repeat(times))       
    }
}
isNaN(n) ? imprime(0) : imprime(n);
