// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

let size = 8

if (size % 2 == 1) {
    size = size-1;
}

for (let i = 1; i <= size; i++) {
    if (i % 2 == 1) {
        console.log("% ".repeat(size/2));
    } else {
        console.log(" %".repeat(size/2));
    }
}