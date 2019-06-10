# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:45:27 2018

@author: acer
"""

import sys
import spacy
from spacy import displacy

def perform_ner(doc):
    
    '''
    options = {'ents': ['DATE']}
    
    '''
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    html = displacy.render(doc, style='ent')
    return html


#nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_md")
nlp = spacy.load("en_core_web_lg")


text = sys.argv[1]
text = text.replace('\n',' ')
text = text.replace('|','')
out_path = "ner_results.txt"
fd = open(out_path,"w")
fd.write("%s" %perform_ner(nlp(text)))
fd.close()
    
