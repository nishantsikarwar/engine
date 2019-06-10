from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
 
ix = open_dir("indexdir")
 
# query_str is query string
query_str = sys.argv[1]
# Top 'n' documents as result
topN = int(sys.argv[2])
 
with ix.searcher(weighting=scoring.Frequency) as searcher:
    query = QueryParser("content", ix.schema).parse(query_str)
results = searcher.search(query,limit=topN)
for i in range(topN):
    print(results[i]['title'], str(results[i].score), results[i]['textdata'])