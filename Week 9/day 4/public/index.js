'use strict';

const url = "http://localhost:3000";

let button = document.querySelector("#button");
let main = document.querySelector('#main');
let table = document.createElement("table");
main.appendChild(table);

const ajax = function( method, data, res, callback ) {
    const xhr = new XMLHttpRequest();
    data = data ? data : null;
    xhr.open( method, url + res);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send( JSON.stringify( data ));
    xhr.onreadystatechange = function() {
        if ( xhr.readyState === XMLHttpRequest.DONE ) {
            callback( JSON.parse(xhr.response) );
        };
    };
};


                    // T H E   C R E A T E   E L E M E N T   W A Y


function capitalize(header) {
    return header[0].toUpperCase() + header.slice(1);
};

function headerMaker(className, header) {
    let myTableHeader = document.createElement("th");
    myTableHeader.textContent = capitalize(className);
    header.appendChild(myTableHeader);
};

function header (){
    let headers = ["name", "author", "category", "publication", "price"]
    let header = document.createElement("tr");
    headers.forEach(function(element) {
        headerMaker(element, header);
    });
    table.appendChild(header);
};

function printer( element ) {
    let tableRow = document.createElement( "tr" );
    element.forEach( function( each ) {
        let tableCell = document.createElement( "td" );
        tableCell.textContent = each;
        tableRow.appendChild( tableCell );
    });
    table.appendChild(tableRow);
};

function printOrganiser(item) {
    console.log(item);
    header();
    item.forEach(function(element, i) {
        let toPrint = [element.book_name, element.aut_name, element.cate_descrip, element.pub_name, element.book_price];
        printer(toPrint);
    });
};


                    // T H E   S T R I N G   W A Y 


// function header(str) {
//     str += `<th>Name</th><th>Author</th><th>Category</th><th>Publication</th><th>Price</th></tr>`
//     return str
// }

// function body(str, item) {
//     item.forEach(function(element) {
//         str += "<tr><td>" + element.book_name + "</td>\
//                     <td>" + element.aut_name + "</td>\
//                     <td>" + element.cate_descrip + "</td>\
//                     <td>" + element.pub_name + "</td>\
//                     <td>" + element.book_price + "</td></tr>";
//                 });
//     return str;
// }

// function printOrganiser(item) {
//     let htmlString = "<tr>";
//     htmlString = header(htmlString);
//     htmlString = body(htmlString, item)
//     table.innerHTML = htmlString;
// }

let buttonCounter = 0

button.addEventListener('click', function() {
    ajax("GET", '', "/books", printOrganiser);
    buttonCounter++;
});