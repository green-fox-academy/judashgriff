let test = require('tape');
let appleLoadear = require('./apple');


test('getApple prints apple', function (t) {
    t.equal(appleLoadear(), "apple");
    t.end();
});