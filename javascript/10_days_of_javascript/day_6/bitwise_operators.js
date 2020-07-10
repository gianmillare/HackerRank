// Day 6: Bitwise Operators
// https://www.hackerrank.com/challenges/js10-bitwise/problem

function getMaxLessThanK(n,k) {
  // create a max variable
  var max = 0;

  // loop through range 1 -> n
  for (var i = 0; i < n; i++) {
    // start from index 1 of range n
    for (var j = i + 1; j <= n; j++) {
      var bitWiseAnd = i & j;

      // change max if AND operator returns higher, but less than k
      if (bitWiseAnd < k && bitWiseAnd > max) {
        max = bitWiseAnd;
      }
    }
  }
  return max;
}
