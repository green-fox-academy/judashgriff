// function getChars(word) {
//   let chars = [];
//   for (let i = 0; i < word.length; i++) {
//     chars.push(word[i].toLowerCase())
//   }
//   return chars
// }

// function anagramChecker(word, toCheck) {
//   let wordChars = getChars(word);
//   let toCheckChars = getChars(toCheck);
//   let final = new Boolean;
//   if (wordChars.length !== toCheckChars.length) { return false; }
//   wordChars.forEach(c => {
//     if (toCheckChars.includes(c)) {
//       toCheckChars.splice(toCheckChars.indexOf(c), 1);
//       if (toCheckChars.length === 0) {
//         final = true;
//       }
//     } else { final = false }
//   });
//   return final;
// }

// function anagrams(word, words) {
//   let arrayOfAnagrams = [];
//   words.forEach(el => {
//     let isTrue = anagramChecker(word, el);
//     if (isTrue) { arrayOfAnagrams.push(el); }
//   });
//   return arrayOfAnagrams;
// }

String.prototype.sort = function() {
  return this.toLowerCase().split("").sort().join("");
};

function anagrams(word, words) {
  return words.filter(function(x) {
      return x.sort() === word.sort();
  });
}

console.log(anagrams('dog', ['hag', 'god', 'faggot', 'Odg', 'Bob', 'joe', 'dom', 'fog', 'dmg']));

