"use strict"

let elevator = document.querySelector(".right");

for (let i = 0; i < 10; i++) {
    let level = document.createElement("nav");
    level.classList.add("floor");
    level.classList.add("floor_" + i);
    elevator.appendChild(level);
}

let floors = document.querySelectorAll(".floor");

floors[0].classList.add("current");

let current = document.querySelector(".current");

let people = 0;
current.textContent = people;

let refresh = function() {
    current.textContent = people;    
}


let add = document.querySelector(".add");
let remove = document.querySelector(".remove");

add.addEventListener("click", function() {
    if (people < 10) {
        people++;
        refresh()
    };
});

remove.addEventListener("click", function() {
    if (people > 0) {
        people--;
        refresh()
    };
});