'use strict'

const Rectangle = function( x, y ) {
    this.a = x;
    this.b = y;
};

Rectangle.prototype.getArea = function() {
    console.log( this.a * this.b );
};

Rectangle.prototype.getCircumference = function() {
    console.log( this.a * 2 + this.b * 2 );
}

let rectOne = new Rectangle( 2, 4 );
let rectTwo = new Rectangle( 3, 5 );
let rectThree = new Rectangle( 4, 4 );
let rectFour = new Rectangle( 3, 2 );

rectOne.getArea();
rectFour.getCircumference();