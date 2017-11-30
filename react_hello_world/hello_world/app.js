'use strict';

const mysql = require('mysql');
const express = require('express');
const app = express();

app.use(express.json());
app.use('/', express.static("./public"));

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'react_practice'
});

connection.connect((err) => {
    if (err) throw err;
    console.log('Connected!');
});

app.get( '/data', function( req, res ) {
    console.log( req.query );

    connection.query( "SELECT * FROM animals;", function( err, result ) {
        if ( err ) {
            console.log( err );
            res.send( { "result": "error", "message": "invalid input" } );
        return;
    };
    res.json( result );
    });
});

app.listen( 3000, function() {
    console.log( "The server is up and runing on port 3000" )
});