// Time Conversion
// https://www.hackerrank.com/challenges/time-conversion/problem

function timeConversion(s) {
    // filter and list all characters, removing ":"
    s = s.split("");
    var time_array = s.filter(function (el) {
        return !(el == ":");
    }) 

    // Create a new list in pairs of two
    var conversion_pairing = [];
    for (var i = 0; i < time_array.length; i+=2) {
        conversion_pairing.push(time_array[i].concat(time_array[i + 1]));
    }

    // If the end is AM, leave as is unless first hour is 12, then subtract 12 from first hour and append a "0"
    if (conversion_pairing[conversion_pairing.length - 1] === "AM") {
        if (conversion_pairing[0] === "12") {
            var converted_hour = parseInt(conversion_pairing[0]) - 12;
            conversion_pairing[0] = converted_hour.toString().concat("0");
            return conversion_pairing.slice(0, 3).join(":");
        } else {
            return conversion_pairing.slice(0, 3).join(":")
        }
    } else {
        // if the end is PM, add 12 to the first hour unless it is 12, then leaves as is
        if (conversion_pairing[0] === "12") {
            return conversion_pairing.slice(0,3).join(":");
        } else {
            var converted_hour = parseInt(conversion_pairing[0]) + 12;
            conversion_pairing[0] = converted_hour.toString();
            return conversion_pairing.slice(0,3).join(":");
        }
    }
}

console.log(timeConversion("07:05:45AM"));
console.log(timeConversion("07:05:45PM"));
console.log(timeConversion("12:40:22AM"));
console.log(timeConversion("12:40:22PM"));