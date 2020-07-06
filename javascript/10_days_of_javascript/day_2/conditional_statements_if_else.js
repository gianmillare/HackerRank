// Day 2: Conditional Statements: If-Else
// https://www.hackerrank.com/challenges/js10-if-else/problem

function getGrade(score) {
    if (score > 25 && score <= 30) {
        return "A";
    } else if (score > 20 && score <= 25) {
        return "B";
    } else if (score > 15 && score <= 20) {
        return "C";
    } else if (score > 10 && score <= 15) {
        return "D";
    } else if (score > 5 && score <= 10) {
        return "E";
    } else {
        return "F";
    }
}