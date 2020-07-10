// Day 5: Arrow Functions
// https://www.hackerrank.com/challenges/js10-arrows/problem

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

// SOLUTION
// "?" means "if this expression is true, do the method on the left, else do method on the right"
function modifyArray(nums) {
    return nums.map((n) => (n % 2 == 0) ? n * 2: n * 3);
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}