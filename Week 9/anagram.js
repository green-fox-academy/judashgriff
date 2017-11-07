function isAnangram(word1, word2) {
    let str1 = word1.toLowerCase().split('').sort().join('').trim();
    let str2 = word2.toLowerCase().split('').sort().join('').trim();
    let anagram = new Boolean;
    if (str1 === str2) {
        anagram = true;
    } else {
        anagram = false;
    }
    return anagram
}

console.log(isAnangram("Kutya", "Akuty"))

module.exports = isAnangram;