"use strict"

let request = new XMLHttpRequest();

request.open("GET", "https://api.nytimes.com/svc/search/v2/articlesearch.json?=moon+landing+apollo+11&api_key=c80c264c847e4f6f8560dd888ec4557a&limit=10");
request.onreadystatechange = function() {
    if(request.readyState == 4) {
        let apollo = JSON.parse(request.responseText).response.docs
        createArticle(apollo);
    }
}
request.send();

function createArticle(apollo) {
    console.log(apollo);
    apollo.forEach(function(article, i) {
        let art = document.createElement("article");
        let head = document.createElement("h3");
        head.textContent = article.headline.main;
        let snippet = document.createElement("p");
        snippet.textContent = article.snippet;
        let date = document.createElement("span");
        date.textContent = article.pub_date;
        let link = document.createElement("a");
        link.href = article.web_url;
        link.textContent = "  Read more"
        art.appendChild(head);
        art.appendChild(snippet);
        art.appendChild(date);
        art.appendChild(link);
        document.body.appendChild(art);
    }, this);

};