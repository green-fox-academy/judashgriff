'use strict';

let currentHours = 14;
let currentMinutes = 34;
let currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let totalSeconds = 24*60*60;

console.log(totalSeconds - ((currentHours * 60 * 60) + currentMinutes * 60 + currentSeconds));