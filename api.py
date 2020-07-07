import flask
from flask import request,jsonify
import subprocess,sys, os 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/pour', methods=['GET','POST'])
def pour():
	if "drink" in request.args:
		topour = request.args["drink"]
		
		if any(topour in fname for fname in os.listdir('./recipes')):
			os.system("python3 recipeHandler.py "+topour+"&")
			return jsonify({'status':"pouring",'args':request.args})
		else:
			return "invalid recipe name" 
			
@app.route('/api/mystery', methods=['GET','POST'])
def mystery():
	os.system("python3 recipeHandler.py random&")
	return jsonify({'status':"pouring",'args':request.args})
		
			
	
	
app.run(host='10.0.0.131')
