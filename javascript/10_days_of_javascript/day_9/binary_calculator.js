// https://www.hackerrank.com/challenges/js10-binary-calculator?hr_b=1
// Day 9: Binary Calculator



// <!DOCTYPE html>
// <html>
// <head>
//   <meta charset="utf-8">
//   <link rel="stylesheet" href="css/binaryCalculator.css" type="text/css">
// </head>

// <body>
//   <div class="container-fluid">
//       <div id="res" maxlength="8"></div>

//       <div id="btns" class="btn">
//         <div class="upper">
//           <button class="lgreen" id="btn0" onclick="key('0')">0</button>
//           <button class="lgreen" id="btn1" onclick="key('1')">1</button>
//           <button class="dgreen" id="btnClr" onclick="cl()">C</button>
//           <button class="dgreen" id="btnEql" onclick="operatorFunx()">=</button>
//         </div>
//         <div class="lower">
//           <button id="btnSum" class="operator" onclick="key('+')">
//                   +</button>
//           <button id="btnSub" class="operator" onclick="key('-')">
//                   -</button>
//           <button id="btnMul" class="operator" onclick="key('*')">
//                   *</button>
//           <button id="btnDiv" class="operator" onclick="key('/')">
//                   /</button>
//         </div>
//       </div>
//     </div>
//   </div>
    
// <script src="js/binaryCalculator.js" type="text/javascript"></script>

// </body>

// </html>






// body{
//     width: 33%;
// }
// #res{
//     background-color:lightgray;
//     border:solid;
//     border-color:black;
//     height:48px;
//     font-size:20px;
// }

//  .lgreen{
//     background-color:lightgreen;
//     width:25%;
//     font-size:18px;
//     margin:0px;
//     float:left;
//     color:brown;
//     height:36px;
// }
// .upper > .dgreen{
//     background-color:darkgreen;
//     width:25%;
//     font-size:18px;
//     margin:0px;
//     float:left;
//     color:white;
//     height:36px;
// }

// .lower > .operator{
//     background-color:black;
//     width:25%;
//     height:36px;
//     font-size:18px;
//     margin:0px;
//     color:red;
//     float:left;
// }







var screen = "";

function operatorFunx() {
  if (screen.indexOf("+") != -1) {
    var numbers = screen.split("+");
    var x = parseInt(numbers[0], 2);
    var y = parseInt(numbers[1], 2);
    var sum = x + y;
    var ans = sum.toString(2);
  } else if (screen.indexOf("-") != -1) {
    var numbers = screen.split("-");
    var x = parseInt(numbers[0], 2);
    var y = parseInt(numbers[1], 2);
    var sub = x - y;
    var ans = sub.toString(2);
  } else if (screen.indexOf("*") != -1) {
    var numbers = screen.split("*");
    var x = parseInt(numbers[0], 2);
    var y = parseInt(numbers[1], 2);
    var mul = x * y;
    var ans = mul.toString(2);
  } else if (screen.indexOf("/") != -1) {
    var numbers = screen.split("/");
    var x = parseInt(numbers[0], 2);
    var y = parseInt(numbers[1], 2);
    var div = x / y;
    var ans = div.toString(2);
  }
  screen = ans;
  document.getElementById("res").innerHTML = screen;
}

function key(c) {
  
  screen += c;
  document.getElementById("res").innerHTML = screen;
}

function cl() {
  screen = "";
  document.getElementById("res").innerHTML = screen;
};