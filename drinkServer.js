let {PythonShell} = require('python-shell')

const express = require('express')
const app = express()
var request = require('request')

app.use(express.urlencoded())


app.get('/pour', function(req, res) {
	console.log("pourpage");
	res.sendFile(__dirname + "/" + "select.html");
});

app.get('/shot', function(req, res) {
	console.log("shotpage");
	res.sendFile(__dirname + "/" + "shots.html");
});

app.get('/', function(req, res) {
	res.redirect('/pour')
});

app.get('/drunk-splash', function(req, res) {
	console.log("pouring")

	res.sendFile(__dirname + "/" + "enjoy.html");
});

app.post('/get-drunk', (req, res) => {
	res.redirect('/drunk-splash');

  const name = req.body.drinks
  console.log(name)

	let options = {
    args: [name]
  };

  PythonShell.run('recipeHandler.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
  });

  res.end()
})

app.get('/mystery-splash', function(req, res) {
	console.log("mysteryshot");
	res.sendFile(__dirname + "/" + "mysteryshot.html");
});

app.post('/mystery-shot', (req, res) => {
		res.redirect('/mystery-splash');
		console.log("mystery oooh")

		let options = {
	    args: ["random"]
	  };

 		PythonShell.run('recipeHandler.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
  });

res.end()
});

app.listen(3000);

console.log("server on");
