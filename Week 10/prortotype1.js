'use strict'

const GreatHouse = function( speak ) {
    this.words = speak;
};

GreatHouse.prototype.speak = function() {
    console.log( this.words );
};

let lannysters = new GreatHouse( "Hear my roar!" );
let baratheon = new GreatHouse( "Ours is the Fury!" );
let targaryen = new GreatHouse( "Fire and Blood" );
let starks = new GreatHouse( "Winter is coming!" );

starks.speak();