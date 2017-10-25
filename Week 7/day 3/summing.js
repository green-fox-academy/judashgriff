'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

let sum = function sumarizer(limit) {
    let out = 0;
    for (let num = 1; num < limit; num++) {
        out += num;
    }
    return out;
}

console.log(sum(4))