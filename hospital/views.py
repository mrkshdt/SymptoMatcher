from hospital import app
from flask import render_template

@app.route("/")
def base():
	dict_words = {}
	return dict_words