'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){
  let newStr = str1 + str2;
  if (str1 instanceof String && str2 instanceof String) {
    printStr(newStr);
  } else {
      throw ("DiS Iz AN TYp ErROr!!");
  }
} 

let printStr = function(str) {
  console.log(str);
}

try {
  addString(1234, 56789, 'printStr');
} catch (error) {
    console.log(error);
}