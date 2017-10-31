"use strict"

let multiplier = function(amt) {
    let amount = amt
    return function (n) {
        let num = n;
        num = num * amount;
        return num;
    }
}

const duplicator = multiplier(2)

console.log(duplicator(5)); // should log 10
console.log(duplicator(10)); // should log 20

const threeTimes = multiplier(3);

console.log(threeTimes(5)); // should log 15
console.log(threeTimes(100));

const FortysixTimes = multiplier(46);

console.log(FortysixTimes(1)); // should log 15
console.log(FortysixTimes(5)); // should log 15
console.log(FortysixTimes(100));

