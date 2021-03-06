#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(`${c}`.repeat(this.height));
    }
  }
};
