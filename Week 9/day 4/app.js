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
  console.log(req.query.category)
  let selector = '';
  if (Object.keys(req.query).length > 0) {
    selector += "WHERE"
    selector += req.query.category ? ` cate_descrip = \'${req.query.category}\' AND` : ''
    selector += req.query.publisher ? ` pub_name = \'${req.query.publisher}\' AND` : ''
    selector += req.query.plt ? ` book_price < \'${req.query.plt}\' AND` : ''
    selector += req.query.plt ? ` book_price > \'${req.query.pgt}\' AND` : ''
  } 
  if (selector.endsWith('AND')) {
    selector = selector.substr(0, selector.length - 4);
  }; 
  
  let qu = `
  SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast
  JOIN author ON book_mast.aut_id = author.aut_id
  JOIN category ON book_mast.cate_id = category.cate_id
  JOIN publisher ON book_mast.pub_id = publisher.pub_id
  ${selector};`;

  console.log(qu);

  connection.query(qu, function( err, result ) {
      if ( err ) {
        console.log( err.toString());
        return;
      }
     
    res.json( result );
  });
});

app.listen(3000, function() {
  console.log("The server is up and runing on port 3000")
})