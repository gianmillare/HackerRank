// Day 5: Template Literals
// https://www.hackerrank.com/challenges/js10-template-literals/problem

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
function sides(literals, ...expressions) {
    var area = expressions[0];
    var perimeter = expressions[1];
    var d = Math.sqrt((perimeter*perimeter) - (16*area));
    var s1 = (perimeter + d) / 4;
    var s2 = area / s1;

    var ans = [s1, s2].sort();

    return ans;
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}