from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
	return render_template("welcome.html", nadpis = "Barborkina stranka")



@app.route("/about/")
def about():
	return render_template("about.html", nadpis = "about page")
