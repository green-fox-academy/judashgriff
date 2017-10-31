'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

let countE = fruits.map(function(fruit, i) {
    let splitted = fruit.split("");
    let count = 0;
    splitted.forEach(function(char) {
        if (char === "e") {
            count++;
        }
    })
    return count;
})

console.log(countE)
// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.