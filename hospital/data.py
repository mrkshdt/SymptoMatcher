import re
import string
import nltk
from nltk.corpus import stopwords

german_stop_words = stopwords.words('german')

def normalize(user_string):
    
    user_string = user_string.lower()
    clean_rf = re.sub(r"""[-,.;@#?!&$]+\ *"""," ",user_string, flags=re.VERBOSE)
    tokens = nltk.word_tokenize(clean_rf)
    sol = ' '.join([w for w in tokens if not w in german_stop_words])
    
    ### Extract specific german words? (Verbs, Adjectives,...)
    #new = nlp(sol)
    #print("Verbs:", [token.lemma_ for token in new if token.pos_ == "VERB"])
    
    return sol

