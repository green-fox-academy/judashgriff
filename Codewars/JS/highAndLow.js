function highAndLow(numbers){
    let nums = numbers.split(" ").map(e => Number(e));
    return `${Math.max(...nums)} ${Math.min(...nums)}`;
  }


console.log(highAndLow("1 2 3 4 5")); // return "5 1"
console.log(highAndLow("1 2 -3 4 5")); // return "5 -3"
console.log(highAndLow("1 9 3 4 -5")); // return "9 -5"