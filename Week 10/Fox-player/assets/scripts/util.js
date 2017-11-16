'use strict'

const utilFunctions = function() {
    let getTimeFormat = function( sec ) {
        let minutes = Math.floor( sec / 60 );
        let seconds = Math.floor( sec % 60 );
        seconds = seconds < 10 ? "0" + seconds : seconds
        return minutes + ":" + seconds
    };

    return {
        getTimeFormat
    };
};