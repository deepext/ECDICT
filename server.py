import os
import logging
import json
import hashlib

from flask import Flask
from flask import request
from utils import setupLogging
from stardict import DictCsv, LemmaDB

app = Flask(__name__)
DICT = DictCsv('./ecdict.csv')
logging.info('dict loaded done')
LEMMA = LemmaDB()
LEMMA.load('./lemma.en.txt')
logging.info('lemma dict loaded done')

def query(word):
  lemmas = LEMMA.get(word, reverse = True)
  lemma = word if (lemmas is None or len(lemmas) == 0) else lemmas[0]

  res = DICT.query(lemma)
  res = {} if res is None else res
  res['lemma'] = lemma
  res['query'] = word
  return res
  
@app.route('/api/ecdict/status')
def status():
    return json.dumps({'status': True }), 200, {'content-type':'application/json'} 

@app.route('/api/ecdict/query', methods=['GET', 'POST'])
def query():
  if request.method == 'POST':
    words = request.json['words']
  else:
    words = request.args['words'].split(',')

  results = [query(word) for word in words]
  res = {}
  res['results'] = results
  res['ok'] = True
  return json.dumps(res), 200, {'content-type':'application/json'}

if __name__ == "__main__":
  env = os.environ.get("ENV", default="dev")
  setupLogging(logging.INFO)
  logging.info(f'use env {env}')
  app.run(host='0.0.0.0', debug = env != 'prod')
  logging.info(f'start the server done!')