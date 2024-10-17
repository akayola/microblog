from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
	user = {"username": "AnKa"}
	posts = [
		{
			"author": {"username": "John"},
			"body": "Beutiful day in Marlboro!"
		},
		{
			"author": {"username": "Mike"},
			"body": "The Avengers movie was so cool!"
		}
	]
	return render_template("index.html", title="Home", username=user["username"], posts=posts)