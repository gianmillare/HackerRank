// Day 2: Loops
// https://www.hackerrank.com/challenges/js10-loops/problem

function vowelsAndConsonants(s) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];

    var list_s = s.split('');
    var consonants = []
    
    for (var i = 0; i < list_s.length; i++) {
        if (vowels.includes(list_s[i])) {
            console.log(list_s[i]);
        } else {
            consonants.push(list_s[i]);
        }
    }

    for (var i = 0; i < consonants.length; i++) {
        console.log(consonants[i]);
    }
}

vowelsAndConsonants('javascript');