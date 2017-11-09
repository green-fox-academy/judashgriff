let express = require("express");
let app = express();

app.use('/assets', express.static('assets'));
app.use(express.json())

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html')
});

express.json.type = "application/json";

app.get('/doubling/', function(req, res){
    if (req.query.input) {
        res.json({
            "received": req.query.input,
            "result": req.query.input * 2
        });
    } else {
        res.json({
            "error": "Please provide an input!"
        });
    }
});

app.get('/greeter/', function(req, res){
    if (req.query.name && req.query.title) {
        res.json({
            "welcome_message": "Oh, hi there " + req.query.name + ", my dear " + req.query.title + "!"
        });
    } else if (!req.query.name) {
        res.json({
            "error": "Please provide a name!"
        });
    } else if (!req.query.title) {
        res.json({
            "error": "Please provide a title!"
        });
    }
});

app.get('/appenda/:appendable', function(req, res) {
    res.json({
        "appended": req.params.appendable + "a"
    });
});

function rSum (num) {
    if (num <= 0) {
        return 0; 
    }
    else { 
        return num + rSum( num - 1 ); 
}}

function rFact(num) {
    if (num <= 0) {
        return 1; 
    } else { 
        return num * rFact( num - 1 ); 
}}

app.post('/dountil/:item', function(req, res) {
    console.log('receiving data...');
    console.log('body is ',req.body);

    if ( req.params.item == "sum" ) {
        let until = rSum(req.body.until);
        res.json({
            "result": until
        }); 
    } else if ( req.params.item == "factor" ) {
        let until = rFact(req.body.until);

        res.json({
            "result": until
        });    
     } else {
        res.json({
            "error": "Please provide a number!"
        });    
    }    
});    


app.listen(8080);