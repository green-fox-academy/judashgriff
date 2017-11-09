'use strict' 

const mysql = require('mysql');
const express = require('express');
const app = express();

app.use(express.json());
app.use('/', express.static("./public"));

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '1234',
  database: 'bookstore'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});

app.get('/books', function( req, res ) {
  console.log(req)
  let selector = '';
  let qu = `
  SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
  JOIN author ON book_mast.aut_id = author.aut_id
  JOIN category ON book_mast.cate_id = category.cate_id
  JOIN publisher ON book_mast.pub_id = publisher.pub_id` + selector + `;`
  if (req.category) {
    selector += "WHERE category = " + req.books.category;
  } else if (req.publisher) {
    selector += "WHERE publisher = " + req.books.publisher;
  } else if (req.plt) {
    selector += "WHERE price < " + req.books.plt;
  } else if (req.pgt) {
    selector += "WHERE price > " + req.books.pgt;
  }

  connection.query(qu, function( err, result ) {
      if ( err ) {
        console.log( err.toString());
        return;
      }
      console.log( result );
     
    res.json( result );
  });
});

app.listen(3000, function() {
    console.log("The server is up and runing on port 3000")
})