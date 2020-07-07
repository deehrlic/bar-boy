import flask
from flask import request,jsonify,render_template
import subprocess,sys, os, requests 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET','POST'])
def home():
	return render_template("select.html")

@app.route('/get-drunk', methods=['GET','POST'])
def req():
	select = request.form.get("drinks")
	print(str(select))
	
	if str(select) is not None and str(select) is not "None":
		urlG = "http://10.0.0.131:5000/api/pour?drink="+str(select)
		r = requests.get(url=urlG,verify=False)
		data = r.json()
		print(data)

	return render_template("enjoy.html")
	
@app.route('/mystery', methods=['GET','POST'])
def mys():
	return render_template("shots.html")
	
@app.route('/mystery-shot', methods=['GET','POST'])
def run():
	urlG = "http://10.0.0.131:5000/api/pour?drink=random"
	r = requests.get(url=urlG,verify=False)
	data = r.json()
	print(data)
	return render_template("mysteryshot.html")
	



app.run(host='10.0.0.131',port=4000)
