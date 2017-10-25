'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

let printer = function() {
    for (let i = 0; i < arguments.length; i++) {
        console.log(arguments[i])
    }
}

printer("kutya", "cica", "mérési hiba")