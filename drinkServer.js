let {PythonShell} = require('python-shell')



const express = require('express')
const app = express()

app.use(express.urlencoded())


app.get('/', function(req, res) {
	console.log("mainpage");
	res.sendFile(__dirname + "/" + "form.html");
});

app.post('/get-drunk', (req, res) => {
  const name = req.body.subject
  console.log(name)
  let options = {
    args: [name]
  };

  PythonShell.run('drinkParser.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results);
  });



  res.end()
})

app.listen(3000);

console.log("server on");
