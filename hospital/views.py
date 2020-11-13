from hospital import app
from flask import render_template

@app.route("/")
def base():
	return None