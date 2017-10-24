'use strict';

var lineCount = 8;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

if (lineCount % 2 == 1) {
    for (let i = 1; i <= (lineCount + 1) / 2; i++) {
        console.log(" ".repeat((lineCount + 1) / 2 - i), "*".repeat(i + (i - 1)))
    }
    for (let i = (lineCount - 1) /2; i > 0; i--) {
        console.log(" ".repeat((lineCount + 1) / 2 - i), "*".repeat(i + (i - 1)))
    }
}   else if (lineCount % 2 == 0) {
    for (let i = 1; i <= lineCount / 2; i++) {
        console.log(" ".repeat(lineCount / 2 - i), "*".repeat(i + (i - 1)))
    }
    for (let i = lineCount / 2; i > 0; i--) {
        console.log(" ".repeat(lineCount / 2 - i), "*".repeat(i + (i - 1)))
    }
}