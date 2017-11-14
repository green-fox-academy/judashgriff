'use strict' 

const express = require('express');
const app = express();

app.use(express.static(__dirname + "/assets") );
app.use(express.json());

app.get('/playlists', function( req, res ) {
    res.json([
        { "id": 1, "title": "Favorites", "system": 1},
        { "id": 2, "title": "Music for programming", "system": 0},
        { "id": 3, "title": "Driving", "system": 0},
        { "id": 5, "title": "Fox house", "system": 0}
    ]);
});

app.get('/playlist-tracks', function( req, res ) {
    res.json([
        { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
        { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
    ]);
});


app.listen(3000, function() {
    console.log("The server is up and runing on port 3000")
})