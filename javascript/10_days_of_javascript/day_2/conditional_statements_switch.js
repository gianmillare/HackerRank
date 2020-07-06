// Day 2: Conditional Statements: Switch
// https://www.hackerrank.com/challenges/js10-switch/problem

function getLetter(s) {
    let letter;

    switch (true) { 
        case 'aeiou'.includes(s[0]):
            letter = 'A';
            return letter;
        case 'bcdfg'.includes(s[0]):
            letter = 'B';
            return letter;
        case 'hjklm'.includes(s[0]):
            letter = 'C';
            return letter;
        default:
            letter = 'D';
            return letter;
    }
}