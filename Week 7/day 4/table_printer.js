'use strict';
// Create a function that prints the ingredient list of dictionaries to the console in the following format:
//
// +--------------------+---------------+----------+
// | Ingredient         | Needs cooling | In stock |
// +--------------------+---------------+----------+
// | vodka              | Yes           | 1        |
// | coffee_liqueur     | Yes           | -        |
// | fresh_cream        | Yes           | 1        |
// | captain_morgan_rum | Yes           | 2        |
// | mint_leaves        | No            | -        |
// +--------------------+---------------+----------+
//
// OPTIONAL
// The frist columns should be automatically as wide as the longest key

const ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": true },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": true },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": true },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": true },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": false },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": false },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": true },
	{ "name": "soda", "in_stock": 0, "needs_cooling": true }
]

let printLine = function() {
    let section1 = "+";
    let length = 0;
    ingredients.forEach(function(element) {
        if (length < element["name"].length) {
            length = element["name"].length;
        };
    });
    section1 += addLines(length);
    section1 += addLines(15);
    section1 += addLines(10);
    return section1;
}
    
let addLines = function(num) {
    let section = "";
    for (let i = 0; i < num; i++) {
        section += "-";
    }
    section += "+";
    return section;
}


let print = function() {
    let line = printLine();
    
    console.log(line);
}

print();