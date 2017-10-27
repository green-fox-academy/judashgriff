"use strict"

let img1 = document.querySelector(".left img");
let img2 = document.querySelector(".right img");
img1.addEventListener("mouseover", function(){
    img1.src = "assets/left-dark.svg";
});

img2.addEventListener("mouseover", function(){
    img2.src = "assets/right-dark.svg";
});