import re
import string
import nltk
import json
import fasttext
import difflib
import spacy
import random
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
MODEL_PATH = "../wiki.de.bin"

# Keep the fasttext model as a global, cached variable 
fastText_model = None
german_stop_words = stopwords.words('german')

def normalize(user_string):
    """
    lower input string and normalize it by deleting stop words and punctuation; 
    Delete all adjectives, verbs and adverbs to increase data quality
    """
    nlp = spacy.load('de_core_news_sm')

    sol=[]
    user_string = user_string.lower()
    clean_rf = re.sub(r"""[-,.;@#?!&$]+\ *"""," ",user_string, flags=re.VERBOSE)
    tokens = nltk.word_tokenize(clean_rf)
    tmp_sol = ' '.join([w for w in tokens if not w in german_stop_words])
    new = nlp(tmp_sol)
    
    for i in new:
        #print(i.lemma_,i.pos_)
        if i.pos_ == "ADJ" or i.pos_ == "ADV":
            pass
        else:
            sol.append(i)

    return sol

def difflib_similarity(word1,word2):
    """
    Compare input words with symptom array and give back a value between 0 and 100; 100 being the highest similarity;
    """
        
    seq = difflib.SequenceMatcher(None,str(word1),str(word2))
    d = seq.ratio()
        
    return d     


#Problems with loading word.bin.de


def fasttext_similarity(word1, word2):
    """
    Computes the similarity between two words by their semantic meaning or their lexical similarity if one of the words is unknown.
    """
    # Load the fastText model if this is the first time the function is called
    global fastText_model
    fastText_model = fasttext.load_model(MODEL_PATH) if not fastText_model else fastText_model
    embedding1 = fastText_model.get_word_vector(word1).reshape(1,-1)    # reshape needed to satisfy cosine function below
    embedding2 = fastText_model.get_word_vector(word2).reshape(1,-1)
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity[0,0]

def get_fb_ranking(fb_matched_terms):
    """
    Returns a fachbereich ranking according to how many tokens have been matched for each fachbereich.
    """
    # Count for each fachbereich how many tokens were detected as relevant and sort the fachbereiche by their count
    ranking = sorted([(fb, len(fb_matched_terms[fb])) for fb in fb_matched_terms.keys()], key=lambda x: x[1], reverse=True)
    return ranking

def string_to_fb(user_string):
    """
    Checks for relevant terms of each fachbereich in the user_string
    """
    with open ('./hospital/resources/terms.json', 'r') as f:
        gazetteers = json.load(f, encoding='utf-8')

    user_tokens = normalize(user_string)

    # fb_matched_terms is a dictionary which maps every fachbereich to a score that represents how much the users description fits the fachbereich
    fb_matched_terms = {}
    # fb_matching_details maps for every fachbereich which user token has been detected as relevant by which fb_term 
    fb_matching_details = {}
    mentioned_bereiche = set()
    thresh = 0.59
    # Get the matches between tokens and relevant terms of each fachbereich
    for bereich in gazetteers['Fachbereiche']:
        fb_matched_terms[bereich['name']] = set()
        fb_matching_details[bereich['name']] = []
 
        for token in user_tokens:
            token = str(token)

            # Check whether the name of the fachbereich has been mentioned in which case it should definitely be displayed as an option to the user
            if similarity(token, bereich['name']) > thresh:
                mentioned_bereiche.add(bereich['name'])

            for alt_name in bereich['alt_names']:
                if similarity(token, alt_name) > thresh:
                    mentioned_bereiche.add(bereich['name'])

            # Check whether the similarity of one of the tokens matches one of the words associated with the fachbereich
            for fb_term in bereich['associated_terms']:
                #print("%s == %s ---> similarity of %1.3f"%(token, fb_term, similarity(token, fb_term)))
                if similarity(token, fb_term) > thresh:
                    fb_matched_terms[bereich['name']].add(token)
                    fb_matching_details[bereich['name']].append({'user_token':token, 'fb_term':fb_term, 'score':float(similarity(token, fb_term))})
        # In order to serialize the data later on we have to convert from set to list again
        fb_matched_terms[bereich['name']] = list(fb_matched_terms[bereich['name']])

    mentioned_bereiche = list(mentioned_bereiche)


    ranking = get_fb_ranking(fb_matched_terms)

    #for i in fb_matching_details:
    #    print(fb_matching_details[i])
    

    return ranking, fb_matching_details, mentioned_bereiche

useFastText = False
similarity = fasttext_similarity if useFastText else difflib_similarity

#string_to_fb("Ich habe übertrieben harte Bauchschmerzen")

def generate_fun_fact(fb_matching_details):
    """
    Generates funfacts / tooltips based on the matching results of the string_to_fb method
    """
    # List all the facts and the term that triggers them to be displayed to the user
    facts = [
        ('Atembeschwerden', 'Sie sind nicht alleine, im Durchschnitt kommen 156 Personen im Jahr mit Atembeschwerden in die Notaufnahme'),
        ('Hautausschlag', 'Sie sind heute bereits die vierte Person mit Hautausschlag')
    ]

    matching_facts = []
    for keyword, fact in facts:
        for bereich_name in fb_matching_details.keys():
            for match in fb_matching_details[bereich_name]:
                #print("check %s == %s"%(keyword, match['fb_term']))
                if keyword == match['fb_term']:
                    matching_facts.append(fact)

    # Just for testing determinism
    random.seed(42)
    if len(matching_facts) > 0:
        random.shuffle(matching_facts)
        return matching_facts[0]
    else:
        return '' 