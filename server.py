import os
import logging
import json
import hashlib

from flask import Flask
from flask import request
from utils import setupLogging
from stardict import DictCsv

app = Flask(__name__)
DICT = DictCsv('./ecdict.csv')

def query(word):
  res = DICT.query(word)
  res = {} if res is None else res
  res['query'] = word
  return res
  
@app.route('/api/ecdict/status')
def status():
    return json.dumps({'status': True }), 200, {'content-type':'application/json'} 

@app.route('/api/ecdict/query', methods=['GET', 'POST'])
def tts():
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
  logging.warn(f'use env {env}')
  app.run(host='0.0.0.0', debug = env != 'production')
  logging.warn(f'start the server done!')