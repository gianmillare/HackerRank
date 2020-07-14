// Day 8: Create a Button
// https://www.hackerrank.com/challenges/js10-create-a-button?hr_b=1

// HTML portion
// <!DOCTYPE html>
// <html>
//     <head>
//         <meta charset="UTF-8">
//         <title>Button</title>
//             <link rel="stylesheet" href="css/button.css" type="text/css">
//     </head>
//         <body>
//             <button id="btn">0</button>
//             <script src="js/button.js" type="text/javascript"></script>
//         </body>
// </html>



// JS portion
var btnCounter = document.getElementById('btn');
btnCounter.addEventListener('click',function() {
    btnCounter.innerHTML=+(btnCounter.innerHTML) + 1;
});




// CSS portion
// #btn {
//     width: 96px;
//     height: 48px;
//     font-size: 24px;
// }