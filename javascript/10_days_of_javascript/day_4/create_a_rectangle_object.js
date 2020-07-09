// Day 4: Create a Rectangle Object
// https://www.hackerrank.com/challenges/js10-objects/problem



/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    this.length = a;
    this.width = b;
    this.perimeter = (a + b) * 2;
    this.area = a * b;
}

