from app import app
from flask import render_template, request

from app.utils import punctuation_restoration

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	inp = request.form.get("txt")
	res = punctuation_restoration(inp)
	
	return render_template("results.html", res=res)
