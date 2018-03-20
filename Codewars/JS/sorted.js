function sortAscending(arr) {
  return arr.sort(function(a, b) {
    return a - b;
  });
}

function sortDescending(arr) {
  return arr.sort(function(a, b) {
    return b - a;
  });
}

function isSortedAndHow(array) {
  let how = "no";
  if (array.length < 2) {
    return how;
  }
  let asc = sortAscending([...array]);
  let desc = sortDescending(array.slice());
  console.log(array, asc, desc);
  if (asc == array) {
    how = "yes, ascending";
  }
  if (desc == array) {
    how = "yes, descending";
  }
  
  return how;
}

let myArr = [1, 515, 1000, 1200];
console.log(isSortedAndHow(myArr));


// const animals = ['Dog', 'Cat', 'Elephant', 'Dolphin'];

// let copy = animals.slice();
// console.log(animals, copy);
// console.log(animals === copy, animals == copy);