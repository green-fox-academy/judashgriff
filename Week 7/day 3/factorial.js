'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

let fac = function factorio(inp) {
    let out = 1;
    for (let n = 1; n <= inp; n++) {
        out = out * n;
    }
    return out;
}

console.log(fac(3))