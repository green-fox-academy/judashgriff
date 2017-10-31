'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

let fruits = ["apple", "pear", "melon", "grapes"];
let times = [0, 1000, 3000, 5000];

fruits.forEach(function(fruit, i) {
    setTimeout(print, times[i], fruit);

})

function print(arg) {
    console.log(arg);
};