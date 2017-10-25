'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];

var order = [];
for (let i = 0; i < boys.length; i++) {
    if (boys[i] !== undefined && girls[i] !== undefined) {
        order.push(boys[i], girls[i]); 
    } else if (girls[i] == undefined) {
        order.push(boys[i]);
    }
}

console.log(order);