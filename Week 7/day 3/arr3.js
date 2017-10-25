'use strict';
// Add "a" to every string in far

var far = ["kuty", "macsk", "kacs", "rók", "halacsk"];

far.map(function(x, i) {
    far[i] += "a";
})

console.log(far);