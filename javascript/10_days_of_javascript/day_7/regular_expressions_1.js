// Day 7: Regular Expressions I
// https://www.hackerrank.com/challenges/js10-regexp-1/problem

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
function regexVar() {
    const regex = /^([aeiou]).+\1$/;
    return regex;
}


function main() {
    const re = regexVar();
    const s = readLine();
    
    console.log(re.test(s));
}