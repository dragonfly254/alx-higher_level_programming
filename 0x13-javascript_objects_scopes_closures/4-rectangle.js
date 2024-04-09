#!usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (Object.keys(this).length === 0) {
      return;
    }

    const tmpWidth = this.width;
    this.width = this.height;
    this.height = tmpWidth;
  }

  double () {
    if (Object.keys(this).length === 0) {
      return;
    }
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
