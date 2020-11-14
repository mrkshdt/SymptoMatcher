from hospital import app
from flask import render_template
from. import data_processing

@app.route("/")
def base():
	dict_words = {}
	return dict_words