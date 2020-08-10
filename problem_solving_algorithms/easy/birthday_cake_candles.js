// Birthday Cake Candles
// https://www.hackerrank.com/challenges/birthday-cake-candles/problem

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the birthdayCakeCandles function below.
function birthdayCakeCandles(ar) {
    var max_height = ar.reduce(function(a, b) {return Math.max(a, b)});
    var count = 0;

    for (var i = 0; i < ar.length; i++) {
        if (ar[i] == max_height) {
            count++;
        }
    }

    return count;
}

function main() {
    const arCount = parseInt(readLine(), 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = birthdayCakeCandles(ar);

    console.log(result);
}
