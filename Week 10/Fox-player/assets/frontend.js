'use strict'

const url = "";

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

let addListElement = function(element, cls) {
    let li = document.createElement("li");
    li.classList.add(cls);
    li.textContent = element.title
    return li
}

let addPlaylists = function(data) {
    let playlists = document.querySelector(".playlists");
    data.forEach(function(element) {
        let li = addListElement(element, "list")    
        if (element.system === 0) {
            li.innerHTML += `<i class="fa fa-times icon" aria-hidden="true"></i>`
        }
        playlists.appendChild(li);
    })
}

let getTimeFormat = function(sec) {
    let time = "";
    let add = function() {
        if (Math.floor(sec % 60) < 10) {
            return "0" + Math.floor(sec % 60);
        } else {
            return Math.floor(sec % 60);
        }
    } 
    time = Math.floor(sec / 60) + ":" + add();
    return time
}

let addTracks = function(data) {
    let tracklist = document.querySelector(".tracklist");
    data.forEach(function(element) {
        let li = addListElement(element, "song");
        li.innerHTML = `<span class="index">1</span>${element.title}`;
        let time = getTimeFormat(element.duration);
        li.innerHTML += `<span class="song_length">${time}</span>`;
        tracklist.appendChild(li);
    });
    indexTrackList();
}

ajax("GET", '', "/playlists", addPlaylists)
ajax("GET", '', "/playlist-tracks", addTracks)
ajax("POST", '', "/playlists", addPlaylists)


            // additional functions


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

let indexTrackList = function(){
    let numbering = document.querySelectorAll(".index");
    numbering.forEach(function(each, i) {
        each.textContent = i + 1;
    }); 
}

let addBtn = document.querySelector(".fa-plus");
let addNew = document.querySelector(".add_new_playlist");

addBtn.addEventListener('click', function() {
    addNew.classList.toggle("hidden")
});

let newListBtn = addNew.querySelector("button");
let newListInput = addNew.querySelector("input");

newListBtn.addEventListener('click', function() {
    ajax("POST", newListInput.value, "/playlists", 'somethingforlatertimes');
});

function select(itemList) {
    itemList.forEach(function(element) {
        console.log(element)
        this.addEventListener('click', function() {
            this.style.backgroundColor = "teal";
        });
    });
};

let listsAll = document.querySelectorAll(".list");
let songsAll = document.querySelectorAll(".song");

let addClickFunc = function() {
    select(listsAll);
    select(songsAll);
};

addClickFunc();

console.log(listsAll, songsAll)