'use strict';

function loadImage(url) {
    return new Promise((resolve, reject) => {
        let image = new Image();

        image.onload = () => {
            resolve(image);
        };

        image.onerror = () => {
            let message = 'Could not load image at ' + url;
            reject(new Error(message));
        };
        image.src = url;
    });
};

let addImg = (src) => {
    let imgElement = document.createElement("img");
    imgElement.src = src;
    document.body.appendChild(imgElement);
};

loadImage('./cat1.jpg').then((image) => {
    addImg(image.src);
});