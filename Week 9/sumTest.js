let test = require('tape');
let summer = require('./sum');

test('summarizes my list of numbers', function (t) {
    t.equal(summer([1,4,3, 4,7]), 19);
    t.end();
});