// Day 3: Throw
// https://www.hackerrank.com/challenges/js10-throw/problem

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
function isPositive(a) {
    if (a == 0) {
        throw new Error("Zero Error");
    } else if (a < 0) {
        throw new Error("Negative Error");
    } else {
        return "YES";
    }
}


function main() {
    const n = +(readLine());
    
    for (let i = 0; i < n; i++) {
        const a = +(readLine());
      
        try {
            console.log(isPositive(a));
        } catch (e) {
            console.log(e.message);
        }
    }
}