function summary(myList) {
    return myList.reduce(function (a, b) {
        return a + b;
    }, 0);
}

let nums = [1,4,3, 4,7];
// let thing = summary(nums);
module.exports = summary;