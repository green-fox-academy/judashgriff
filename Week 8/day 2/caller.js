'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


let print = function printNumber(num) {
  console.log(num);
}

let arr = [2, 5, 7, 8, 9, 11];

let select = function selectLastEvenNumber(arr, callback) {
    let lastEven = 0;
    arr.forEach(function(num) {
        if (num % 2 === 0) {
            lastEven = num;
        };
    });
    callback(lastEven);
}

select(arr, print);