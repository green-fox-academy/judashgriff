'use strict'

const requestModule = function() {
    const url = "";
    
    const send = function( method, res, callback, data ) {
        const xhr = new XMLHttpRequest();
        data = data ? data : null;
        xhr.open( method, url + res);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send( JSON.stringify( data ));
        xhr.onreadystatechange = function() {
            if ( xhr.readyState === XMLHttpRequest.DONE ) {
                callback( JSON.parse(xhr.response) );
            };
        };
    };

    const getPlaylists = function(callback){
        send("GET", "/playlists", callback, '')
    }

    const getTracks = function(callback){
        send("GET", "/playlist-tracks", callback, '')
    }

    return {
        send,
        getPlaylists,
        getTracks
    }
}