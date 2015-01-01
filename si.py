# -*- coding: utf-8 -*-

from pprint import pprint
import rdflib
g=rdflib.Graph()
g.load('http://dbpedia.org/resource/Semantic_Web')
data_subject = {}
data_object = {}
for entry in g:
    data_subject.setdefault(entry[1], []).append(unicode(entry[0]))
    data_object.setdefault(entry[1], []).append(unicode(entry[2]))

pprint(data_object)
pprint(data_subject)

