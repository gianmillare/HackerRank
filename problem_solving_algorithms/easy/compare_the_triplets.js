// Compare the Triplets
// https://www.hackerrank.com/challenges/compare-the-triplets/problem

// function compareTriplets(x, y) {
//     var a = x.split(' ');
//     var b = y.split(' ');

//     var a_arr = [];
//     var b_arr = [];

//     for (var i = 0; i < a.length; i++) {
//         a_arr.push(parseInt(a[i]));
//         b_arr.push(parseInt(b[i]));
//     }

//     var aScore = 0;
//     var bScore = 0;

//     for (var n = 0; n < a_arr.length; n++) {
//         if (a_arr[n] > b_arr[n]) {
//             aScore++;
//         } else if (a_arr[n] < b_arr[n]) {
//             bScore++;
//         }
//     }

//     return aScore.toString() + " " + bScore.toString();
// }


// Accepted Solution
function compareTriplets(a, b) {
    var result = [];
    var aScore = 0, bScore = 0;

    for (var i = 0; i < a.length; i++) {
        if (a[i] > b[i]) aScore++;
        if (a[i] < b[i]) bScore++;
    }
    result[0] = aScore;
    result[1] = bScore;
    return result;
}

console.log(compareTriplets('5 6 7', '3 6 10'));