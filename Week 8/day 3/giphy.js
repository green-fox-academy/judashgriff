"use strict"

let request = new XMLHttpRequest();

let btn = document.querySelector("#btn");
let content = document.querySelector("#content");

request.open("GET", "http://api.giphy.com/v1/gifs/search?q=the+last+airbender&api_key=uy7yUbYfg7jQ1Zbtxem8BwiLKwxurqZi&limit=16");
btn.addEventListener("click", function () {
    request.onreadystatechange = function() {
        if(request.readyState == 4) {
            let giphy = JSON.parse(request.responseText).data
            createGifs(giphy);
        }
    }
    request.send()
});

function createGifs(giphy) {
    giphy.forEach(function(gif, i) {
        let newGif = document.createElement("img");
        newGif.src = gif.images.downsized_still.url;
        newGif.dataset.alt = gif.images.downsized.url;
        newGif.classList.add("img");
        content.appendChild(newGif);
        newGif.addEventListener("click", function() {
        [this.src, this.dataset.alt] = [this.dataset.alt, this.src];
        })
    });
};

function onClick(newGif) {
    // this.classList.toggle("moving")
    this.src = this.images.downsized.url;
}