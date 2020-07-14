// Day 8: Buttons Container
// https://www.hackerrank.com/challenges/js10-buttons-container?hr_b=1

// HTML portion
// <!DOCTYPE html>
// <html>
//     <head>
//         <meta charset="utf-8">
//         <title>Buttons Grid</title>
//         <link rel="stylesheet" href="css/buttonsGrid.css" type="text/css">
//     </head>
//     <body>
//         <script src="js/buttonsGrid.js" type="text/javascript"></script>
//     </body>
// </html>

// JS portion --> study diligently...
var container = document.createElement('div');
container.className = 'buttonContainer';
container.id = 'btns';

var buttons = [9];
for (var i = 0; i < 9; i++) {
    buttons[i] = document.createElement('button');
    buttons[i].id = 'btn' + (i + 1);
    buttons[i].innerHTML = (i + 1);
    buttons[i].className = 'button';
    container.appendChild(buttons[i]);
}

document.body.appendChild(container);


function getNextLabel(currentLabel) {
    var labels = [1, 4, 7, 8, 9, 6, 3, 2];
    var index = (labels.indexOf(+(currentLabel)) + 1) % labels.length;

    return labels[index];
}

function updateLabel() {
    for (var i = 0; i < 4; i++) {
        buttons[i].innerHTML = getNextLabel(buttons[i].innerHTML);
    }
    for (var i = 5; i < 9; i++) {
        buttons[i].innerHTML = getNextLabel(buttons[i].innerHTML);
    }
}

btn5.addEventListener("click", function() {
    updateLabel();
});



// CSS portion
// .buttonContainer {
//     width: 75%;
// }

// .buttonContainer > .button {
//     width: 30%;
//     height: 48px;
//     font-size: 24px;
// }