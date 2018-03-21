// function sortAscending(arr) {
//   return arr.sort(function(a, b) {
//     return a - b;
//   });
// }

// function sortDescending(arr) {
//   return arr.sort(function(a, b) {
//     return b - a;
//   });
// }

// function isSortedAndHow(array) {
//   let how = "no";
//   if (array.length < 2) { return how; }
//   let asc = sortAscending([...array]);  // using the spread operator in an array
//   let desc = sortDescending(array.slice());  // using slice - does the same it this case
//   let checkerAsc = [];
//   let checkerDesc = [];
//   array.forEach((e, i) => {
//     if (e === asc[i]) {
//       checkerAsc.push(i);
//     }
//     if (e === desc[i]) {
//       checkerDesc.push(i);
//     }
//   });
//   if (array.length === checkerAsc.length) {
//     how = "yes, ascending";
//   }
//   if (array.length === checkerDesc.length) {
//     how = "yes, descending";
//   }
  
//   return how;
// }

function isSortedAndHow(arr) {
return arr.every((e, i) => i === 0 || arr[i] <= arr[i - 1])? 'yes, descending' :
       arr.every((e, i) => i === 0 || arr[i] >= arr[i - 1])? 'yes, ascending' : 'no';
}

let myArr = [100, 80, 76, -13];
console.log(isSortedAndHow(myArr));
