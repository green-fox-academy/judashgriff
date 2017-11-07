let test = require('tape');
let summer = require('./sum');

test('summarizes my list of numbers', function (t) {
    t.equal(summer([1,4,3, 4,7]), 19);
    t.end();
});

test('sum if 0', function (t) {
    t.equal(summer([]), 0);
    t.end();
});

test('sum if 1', function (t) {
    t.equal(summer([6]), 6);
    t.end();
});