function longest(s1, s2) {
  let charCollection = {};
  s1.split("").concat(s2.split("")).forEach(c => charCollection[c] = c);
  return Object.keys(charCollection).sort().join("");
}

const a = "xyaabbbccccdefww";
const b = "xxxxyyyyabklmopq";

console.log(longest(a, b))