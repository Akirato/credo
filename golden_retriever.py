from google import google
from constants import IBM_WATSON_API_KEY
from keywords.rake import *
def retrieve_keywords(article):
    imp_keywords = extract_keywords(article)
    return imp_keywords
    
    
def search(query)
    return google.search(' '.join(query))

