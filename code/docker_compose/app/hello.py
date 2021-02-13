#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from elasticsearch import Elasticsearch
from datetime import datetime as dt

es = Elasticsearch(hosts=['elasticsearch'])
app = Flask(__name__) 
 
# !!NB it is bad to use GET here
@app.route("/add")
def add():
    text = request.args.get('text', '')
    
    doc = {
        'title': str(dt.now()),
        'text': text
    }
        
    res = es.index(index="test-index", id=1, body=doc)
    return res
    

@app.route("/search")
def search():
    text = request.args.get('text', '')
     
    res = es.search(index="test-index", body={"query": {"match": {"text": text}}})
    return res   
    

app.run('0.0.0.0', port=8989, debug=True)
