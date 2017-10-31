// Create a prison function, that has your name as a private fugutive variable
// The function should return an object that has two methods:
//  - visit() // logs "[yourname] is visited [x] time(s)" to the console.
//    - the [x] times displayes the numbers the function is called
//    - If the fugitive variable is empty, then display "Nobody is here anymore"
//  - escape() // logs "BREAKING NEWS, [yourname] escaped the prison" to the console.
//    - it should empties the fugitive variable
"use strict"

function jail(prisoner) {
    this.fugitive = prisoner;
    this.counter = 0;
    this.visit = function(){
        if (this.fugitive === "") {
            console.log("Nobody is here anymore");
        } else {
            this.counter++;
            console.log(this.fugitive + " is visited " + this.counter + " time(s).");
        };
    };
    this.escape = function() {
        console.log("BREAKING NEWS, " + this.fugitive + " escaped the prison");
        this.fugitive = "";
    };
};


let prison = function(HeWhoIsBusted) {
    return new jail(HeWhoIsBusted);
}

const alcatraz = prison('Sad Panda');

alcatraz.visit()
alcatraz.visit()
alcatraz.escape()
alcatraz.visit()