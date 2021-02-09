#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = null, h = null) {
    if (h < 1 || w < 1) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
