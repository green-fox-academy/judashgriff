'use strict'

const url = "songs.json";

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

let play = document.querySelector(".play");

let rest = function() {
    return play.src.substring(0, play.src.lastIndexOf("/") + 1)
};

let last = "play.svg";

play.addEventListener('click', () => {
    let restStr = rest()
    if (last == "play.svg") {
        play.src = (restStr += "pause.svg");
        last = "pause.svg";
    } else {
        play.src = (restStr += "play.svg");
        last = "play.svg";
    }
});

let numbering = document.querySelectorAll(".index");

numbering.forEach(function(each, i) {
    each.textContent = i + 1;
}); 