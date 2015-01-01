import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')
arr=[]
for smt in g:
    arr.append(str(smt[1]))
arr1=set(arr)
print arr1
    #print len(arr1)      

