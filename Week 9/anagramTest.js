let test = require('tape');
let anagram = require('./anagram');

test('If anagrams are good', function (t) {
    // t.plan(4);
    t.ok(anagram("", ""));
    t.notOk(anagram("asss", "sas"));
    t.notOk(anagram("I am a sweet puppy", "SweeT MothEr Of mercy"));
    t.ok(anagram("I am a sweet puppy", "SweeT pa       mIA PPyu"));
    t.end();
});
