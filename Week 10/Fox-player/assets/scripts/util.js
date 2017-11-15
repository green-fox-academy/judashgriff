'use strict'

const utilFunctions = function() {
    let getTimeFormat = function(sec) {
        let minutes = Math.floor(sec / 60);
        let seconds = Math.floor(sec % 60);
        seconds = seconds < 10 ? "0" + seconds : seconds
        return minutes + ":" + seconds
    };

    let listSelecting = function() {
        let select = function(itemList) {
            itemList.forEach(function(element) {
                element.addEventListener('click', function() {
                    this.style.backgroundColor = "lightskyblue";
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
    };

    return {
        getTimeFormat,
        listSelecting
    };
};