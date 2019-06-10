# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:28:08 2018

@author: Abhijeet Kumar
"""

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import sys
from whoosh import scoring

ix = open_dir("indexdir")

query_str = sys.argv[1]
topN = int(sys.argv[2])

with ix.searcher(weighting=scoring.BM25F) as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query,limit=topN)
        for i in range(topN):
            print(results[i]['title'] + ";" + str(results[i].score) + ";" + results[i]['textdata'])
            sys.stdout.flush()


            
        
        
        
        
        
        
        
        
        