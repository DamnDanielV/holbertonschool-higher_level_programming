#!/usr/bin/node
const factorial = (num) => {
  if (num > 0) {
    return (num * factorial(num - 1));
  } else {
    return 1;
  }
}
const result = parseInt(process.argv[2]);
console.log(factorial(result));
