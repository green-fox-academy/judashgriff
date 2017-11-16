'use strict' 

const express = require( 'express' );
const app = express();
const mysql = require( 'mysql' );

const connection = mysql.createConnection( {
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'fox_player'
});
  
connection.connect( ( err ) => {
    if ( err ) throw err;
    console.log( 'Connected!' );
});

app.use( express.static( __dirname + "/assets" )  );
app.use( express.json());

app.get( '/playlists', function(  req, res  ) {
    connection.query( "SELECT name, system FROM playlists;", function(  err, result  ) {
        if (  err  ) {
            console.log(  err.toString());
            return;
        }
    res.json(  result  );
    });
});

app.get( '/playlist-tracks', function(  req, res  ) {
    connection.query( `SELECT title, author, duration, path FROM tracks;`, function(  err, result  ) {
        if (  err  ) {
            console.log(  err.toString());
            return;
        };
    res.json(  result  );
    });
});

app.post( '/playlists', function(  req, res  ) {
    connection.query( `INSERT INTO playlists ( name, system )
                      VALUES ( '${req.body.value}', '0' );`, function(  err, result  ) {
        if (  err  ) {
            console.log(  err.toString());
            return;
        };
    res.json(  result  );
    });
});

app.delete( '/playlists', function(  req, res  ) {
    connection.query( `DELETE FROM playlists
                      WHERE name ='${req.body.value}';`, function(  err, result  ) {
        if (  err  ) {
            console.log(  err.toString());
            return;
        };
    res.json(  result  );
    });
})


app.listen( 3000, function() {
    console.log( "The server is up and runing on port 3000" )
})