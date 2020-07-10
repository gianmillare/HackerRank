// Day 5: Inheritance
// https://www.hackerrank.com/challenges/js10-inheritance/problem

Rectangle.prototype.area = function() {return this.w * this.h;}

class Square extends Rectangle {
    constructor(x) {
        super(x, x);
    }
}