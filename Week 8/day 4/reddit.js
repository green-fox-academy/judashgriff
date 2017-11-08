"use strict"

let request = new XMLHttpRequest;

request.open("GET", "http://secure-reddit.herokuapp.com/simple/posts");
request.setRequestHeader("Content-Type", "application/json");

request.onreadystatechange = function() {
    if(request.readyState == 4) {
        let news = JSON.parse(request.responseText).posts
        postNews(news);
    }
}
request.send();

let left = document.querySelector("#left");

function postNews(news) {
    console.log(news);
    news.forEach(function(post) {
        let newPost = document.createElement("article");
        let nav = document.createElement("nav");

        createArrow("up", nav);
        let navSpan = document.createElement("span");
        navSpan.textContent = post.score;
        nav.appendChild(navSpan);
        createArrow("down", nav, post);

        let contDiv = document.createElement("div");
        let p = document.createElement("p");
        p.textContent = post.title; 
        contDiv.appendChild(p);
        newPost.classList.add("post");
        newPost.appendChild(contDiv);
        newPost.appendChild(nav);
        left.appendChild(newPost);
    });
};

function createArrow(dir, nav, post) {
    let arrow = document.createElement("img");
    arrow.src = "Assets/" + dir + "vote.png";
    arrow.classList.add("arrow");
    arrow.addEventListener("click", function(post) {
        arrow.src = "Assets/" + dir + "voted.png";
        let span = document.querySelector("span");
        request.open("PUT", "http://secure-reddit.herokuapp.com/simple/posts/" + post.id + "/" + dir + "vote");

        request.onreadystatechange = function() {
            if(request.readyState == 4) {
                console.log(JSON.parse(request.responseText))
                let news = JSON.parse(request.responseText).posts
                postNews(news);
            }
        }

        request.send();
    })
    nav.appendChild(arrow);
};