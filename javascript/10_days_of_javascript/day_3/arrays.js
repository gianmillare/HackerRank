// Day 3: Arrays
// https://www.hackerrank.com/challenges/js10-arrays/problem

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
function getSecondLargest(nums) {
    var set_nums = [];

    for (var i = 0; i < nums.length; i++)
    {
        if (set_nums.includes(nums[i])) {
            continue;
        } else {
            set_nums.push(nums[i]);
        }
    }
    var ans = set_nums.sort(function(a, b){return a - b});
    return ans[ans.length - 2];
}


function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}