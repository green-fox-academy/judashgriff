// COMMAND LINE
// more info and git:
// https://www.codeproject.com/Articles/457305/Basic-Git-Command-Line-Reference-for-Windows-Users
// List the contents of the current directory:
  // $ ls
    // - a: Show Everything, including hidden items
    // - 1: List 1 item per line
    // - d: list only directories
    // - r: Reverse the sort order
    // - l: Use a long listing format
  // Create a New Directory:
    // $ mkdir NewFolderName
    // $ mkdir /c/ExistingParentFolder/NewFolderName
  // Create Files:
    // $ touch newFile.txt
    // $ touch /c/SomeFolder/newFile.txt
  // Append text to a file. If the file does not exist, one is created: 
    // $ echo "This text is added to the end of the file" >> newFile.txt
  // Remove Files:
    // $ rm DeleteFileName
  // Remove Directories:
    // $ rm -rf DeleteFolderName (Removes the specified folder and all contents)
  // Moving files:
    // $ mv hello.html /c/TargetFolder
  // Renaming files:
    // $ mv oldFileName.html newFileName.html

// GIT - very basic commands:
  // Configure Git (git config):
    // git config --global user.name "FirstName LastName"
    // git config --global user.email UserEmailAddress
  // Initialize a New Git Repo:
    // git init
  // Add/Stage for Commit (git add):
    // git add
      // -A: Add all changes in the working directory to the next commit, including new files and deletions
      //  .: Add all changes to tracked files and all new files to the next commit, but do not add file deletions
      // -u: adds all changes to tracked files and all file removals to the next commit, but does not add new files
      // -p: Walks through changed files and prompts user for add option. Does not include new files
  // Unstage from Commit (git reset):
    // git reset HEAD FileName
  // Committing Changes (git commit):
    // git commit FileName –m "Message Text"
      // (If you do not provide one using the -m option, you will be prompted to do so before the commit is performed.)
      // -a: Commit all changes to tracked files since last commit
      // -v: Verbose: include the diffs of committed items in the commit message screen
  // Pushing to Remote Repositories (git push):
    // git push
    // git push RemoteName BranchName
  // Pulling from Remote Repositories (git pull) 
    // git pull
    // git pull RemoteName/BranchName


// JavaScript Datatypes
  // JavaScript allows you to work with three primitive data types:
    // Numbers:
      var number = 175.89;
      // JavaScript does not make a distinction between integer values and floating-point values.
      // All numbers in JavaScript are represented as floating-point values!!!!!
    // Strings:
      var string = "This is a string";
    // Boolean:
      var boolean = true;
  //JavaScript also defines two trivial data types, null and undefined:
    var myNull = null;
    var myNothing = undefined;
  // JavaScript supports a composite data type known as object:
    var myObj = Object; // -- later

// JavaScript Variables:
  // Before you use a variable in a JavaScript program,
  // you must declare it!!
    var name; // this is declaration
    var money, car;  // this is multiple variable declaration
    var age = 31; // this is variable initialization, storing a value in a variable
    name = 'JSmaster'; //  you can assign the value later (if it is declared)
  // JavaScript is untyped language!! 
  // You don't have to tell JavaScript during variable declaration
  // what type of value the variable will hold.

  // var, let or const:
    // var: standard variable declaration
    // let (ES6+): block scope local variable:
        let x = 1;
        if (x === 1) {
          let x = 2;
          console.log(x); // expected output: 2
        }
        console.log(x); // expected output: 1
    // const (ES6+): block-scoped declaration, that means
        // The value of a constant cannot change through re-assignment,
        // and it can't be redeclared.

// JavaScript Variable Scope:
  // The scope of a variable is the region of your program in which it is defined.
  // JavaScript variables have only two scopes:
    // GLOBAL Variables:
      // A global variable has global scope which means it can be defined anywhere in your JavaScript code.
    // LOCAL Variables:
      // A local variable will be visible only within a function where it is defined.
      // Function parameters are always local to that function!!
      // If you declare a local variable or function parameter with the same name as a global variable,
      // you effectively hide the global variable. 
      // Take a look into the following example:
      var myVar = "global"; // Declare a global variable
      function checkscope() {
        var myVar = "local";  // Declare a local variable
        console.log(myVar);   // The output is: local 
      }

// Functions:
  // Generally speaking, a function is a "subprogram"
  // that can be called by code external (or internal in the case of recursion) to the function.
  // Every function in JavaScript is a Function object!!!
  // For all other functions, the default return value is undefined!!!
  // The parameters of a function call are the function's arguments.
  
  // The function declaration:
  function myFunc(theObject) {
    return theObject.brand;
  }

  var myCar = {
    brand: "Honda",
    model: "Accord",
    year: 1998
  };

  console.log(myFunc(myCar)); // Honda

  // The function expression:
  
  var myFunction = function(number) {
    return number < 6;
  }

  console.log(myFunction(8)); // false

  // Multiple arguments:

  function multiArg() {
    console.log(arguments[1])
  }
 multiArg('one', 'two', 'three'); // two

// What is strict mode?? "use strict"
  // It is a directive, that the code should be executed in "strict mode".
  // With strict mode, you can not use undeclared variables!!
  // Without strict mode:
    myName = 'Attila'; // this variable will be declared automatically Global
    // or, let see this:
    myFunction();
    // code here can use carName, because it will be global, even if the value is assigned inside a function!
    function myFunction() {
        carName = "Volvo";
    }
  
  // With "use strict":
    myName = 'Attila';  // This will cause an error because myName is not declared!!

  // So Strict mode makes it easier to write "secure" JavaScript. That's it! :)

// LOOPS LOOPS LOOPS LOOPS LOOPS LOOPS

      var myArray = ["BMW", "Audi", "Mercedes", "Porsche", "Trabant"];
      // FOR LOOP:
      for (let i = 0; i < myArray.length; i++) {
        console.log(myArray[i]);
      }
      
      // WHILE LOOP:
      let i = 0;
      while (i < myArray.length) {
        console.log(myArray[i]);
        i++;
      }

      // ForEach LOOP:
      myArray.forEach(function(element, index, array) {
        console.log(element);
      });
      // index is the index of the current element,
      // array represents the whole array

// Arrays:

  // How to declare it:
      let newArray = ["green", 6, "blue", false];
      let newArray_2 = new Array("green", 6, "blue", false);
      let cars = [];

  // Push: adds one or more elements to the end of an array and returns the new length of the array.
      let colors = ["green", "yellow", "red", "white"];
      colors.push("blue");  // it returns with 5
      console.log(colors);

  // Pop: removes the last element from an array and returns that element. 
      colors.pop();   // it returns with "blue"
      console.log(colors);
  
  // Shift: removes the first element from an array and returns that removed element.
    var a = [1, 2, 3];
    var b = a.shift();
    console.log(a); // [2, 3]
    console.log(b); // 1

  // Unshift: adds one or more elements to the beginning of an array and returns the new length of the array.
    var a = [1, 2, 3];
    a.unshift(4, 5);
    console.log(a); // [4, 5, 1, 2, 3]

  // Splice: changes the contents of an array by removing existing elements and/or adding new elements.
    var woman = ["Carol", "Cherry", "Jody", "Lilly", "Shelley"];

    // Remove 0 elements from index 2, and insert "drum":
    var removed = woman.splice(2, 0, 'Adele');
      // woman is ["Carol", "Cherry", "Adele", "Jody", "Lilly", "Shelley"]
      // removed is [], no elements removed
    
    // Remove 1 element from index 3:
    var removed = woman.splice(3, 1);
      // removed is ["Lilly"]
      // woman is ["Carol", "Cherry", "Adele", "Jody", "Shelley"]

  // MAP: creates a new array with the results of calling a provided function on every element in the calling array.
    var array1 = [1, 4, 9, 16];
    
    // pass a function to map (with arrow function)
    const map1 = array1.map(x => x * 2);
    
    // without arrow function:
    const map2 = array1.map(function(x) {
      return x * 2; // you must return always!
    });

    console.log(map1);
    // expected output: Array [2, 8, 18, 32]
  
  // FILTER: creates a new array with all elements that pass the test implemented by the provided function.
    var words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
    const result = words.filter(word => word.length > 6);
    console.log(result); // expected output: Array ["exuberant", "destruction", "present"]
  
  // concat: is used to merge two or more arrays.
    var array1 = ['a', 'b', 'c'];
    var array2 = ['d', 'e', 'f'];
    
    console.log(array1.concat(array2));
    // expected output: Array ["a", "b", "c", "d", "e", "f"]
  
  // indexOf: returns the first index at which a given element can be found in the array, or -1 if it is not present.
    var beasts = ['ant', 'bison', 'camel', 'duck', 'bison'];
    console.log(beasts.indexOf('bison'));
    // expected output: 1

    console.log(beasts.indexOf('giraffe'));
    // expected output: -1

  // includes: determines whether an array includes a certain element, returning true or false as appropriate.
    var array1 = [1, 2, 3];
    
    console.log(array1.includes(2));
    // expected output: true
  
  // slice:  returns a shallow copy of a portion of an array
  // into a new array object selected from begin to end (end not included).
    var animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
    console.log(animals.slice(2));
    // expected output: Array ["camel", "duck", "elephant"]

    console.log(animals.slice(2, 4));
    // expected output: Array ["camel", "duck"]
  
  // MORE MORE MORE: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

// STRINGS:
  
  // Split: splits a String object into an array of strings by separating the string into substrings,
  // using a specified separator string to determine where to make each split.
    var str = "How are you doing today?";
    var res = str.split(" ");
    // res = ["How","are","you","doing","today?"]
  
  // Join: joins all elements of an array (or an array-like object) into a string and returns this string.
    console.log(res.join());
    // expected output: How,are,you,doing,today?
  
  // Replace: returns a new string with some or all matches of a pattern replaced by a replacement.
    var str = 'Twas the night before Xmas...';
    var newstr = str.replace(/xmas/i, 'Christmas');
    console.log(newstr);  // Twas the night before Christmas...   
  
  // substr: returns the characters in a string beginning at the specified location through the specified number of characters. 
    var str = "Hello world!";
    console.log(str.substr(1, 4));
    // expected output: ello

  // trim: method removes whitespace from both ends of a string.
    var str = "       Hello World!        ";
    console.log(str.trim());
    // expected output: Hello World! (without whitespaces)
    
  // MORE MORE MORE: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String

// Object ori...