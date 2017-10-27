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

let printLine = function(length) {
    let section1 = "+";
    section1 += addLines(length);
    section1 += addLines(15);
    section1 += addLines(10);
    return section1;
}
   
let theLength = function() {
    let length = 0;
    ingredients.forEach(function(element) {
        if (length < element["name"].length) {
            length = element["name"].length;
        };
    });
    length += 2;
    return length;
}

let addLines = function(num) {
    let section = "";
    for (let i = 0; i < num; i++) {
        section += "-";
    }
    section += "+";
    return section;
}

let printHead = function(length) {
    let head = "|"
    head += addContent("Ingridient", length);
    head += addContent("Needs cooling", 15);
    head += addContent("In stock", 10);
    return head;
}

let addContent = function(text, length) {
    let content = " ";
    content += text;
    for (let i = content.length; i < length; i++) {
        content += " ";
    };
    content += "|"
    return content;
}

let addBody = function(element, length) {
    let body = "|";
    body += addContent(element["name"], length);
    if (element["needs_cooling"] === true) {
        body += addContent("Yes", 15);
    } else {
        body += addContent("No", 15);
    };
    if (element["in_stock"] > 0) {
        body += addContent(element["in_stock"], 10);
    } else {
        body += addContent("-", 10);
    }
    return body;
} 

let printBoss = function() {
    let length = theLength();
    let line = printLine(length);
    let head = printHead(length);
    console.log(line);
    console.log(head);
    console.log(line);
    ingredients.forEach(function(element){
        let body = addBody(element, length);
        console.log(body);
    });
    console.log(line);
}

printBoss();