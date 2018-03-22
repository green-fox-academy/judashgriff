function tribonacci(signature,n){
  let array = signature.slice(0, 3);
  while (array.length < n) {
    array.push(array.slice(-3).reduce((nums, current) => nums + current))
  }
  return array.slice(0, n);
}

console.log(tribonacci([1,1,1],10));
