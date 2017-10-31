'use strict';

function factorialTillLimitWithCallback(limit, callback) {
  var factorial = 1;
  for (var i = 1; i <= limit; ++i) {
    factorial *= i;
    callback(factorial);
  }
}

let factorial = function(num) {
    console.log(num)
}

let izé = factorialTillLimitWithCallback(6, factorial)

// Create a function and pass it as a parameter to the factorialTillLimitWithCallback
// function, and print all the factorial numbers till 20

