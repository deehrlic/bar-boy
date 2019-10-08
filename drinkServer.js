let {PythonShell} = require('python-shell')

const express = require('express')
const app = express()

app.use(express.urlencoded())


app.get('/pour', function(req, res) {
	console.log("pourpage");
	res.sendFile(__dirname + "/" + "select.html");
});

app.post('/get-drunk', (req, res) => {
  const name = req.body.drinks
  console.log(name)

	let options = {
    args: [name]
  };

  PythonShell.run('recipeHandler.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results);
  });



  res.end()
})

app.listen(3000);

console.log("server on");
