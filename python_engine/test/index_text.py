# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 08:34:53 2018

@author: Abhijeet Kumar
"""

import os
import sys
from whoosh.index import create_in 
from whoosh.fields import Schema, TEXT, ID

def createSearchableData(root):   
    schema = Schema(title=TEXT(stored=True),path=ID(stored=True), content=TEXT,\
                    textdata=TEXT(stored=True))
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
        
    ix = create_in("indexdir",schema)
    writer = ix.writer()
    
    filepaths = [os.path.join(root,i) for i in os.listdir(root)]
    for path in filepaths:
        fp = open(path,'r')
        #print(path)
        text = fp.read()
        writer.add_document(title=path.split("\\")[1], path=path,content=text,\
                            textdata=text)
        fp.close()        
    writer.commit()

root = sys.argv[1]
createSearchableData(root)