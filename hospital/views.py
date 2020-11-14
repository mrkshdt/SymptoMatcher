from hospital import app
from flask import render_template, request
from. import data_processing

import time
import json

@app.route("/")
def base():
	dict_words = {}
	return dict_words

@app.route("/api/routing")
def get_route():
    """
    :query_parameter user_string: The user's description of his condition
    """
    start_total = time.time()
    user_string = request.args.get('user_string')

    # Get a ranking of appropriate fachbereiche
    ranking, fb_matching_details, mentioned_bereiche = data_processing.string_to_fb(user_string)

    end_total = time.time()
    print("Total time until response: ", end_total - start_total)
    print(type(ranking[0][1]))
    print(type(fb_matching_details['Kardiologie'][0]['score']))
    
    
    
    
    tmp_dict = {
        'ranking': ranking,
        'matching_details': fb_matching_details,
        'mentioned_bereiche': mentioned_bereiche
    }

    #print(fb_matching_details['Kardiologie'][0])

    return json.dumps(tmp_dict) 