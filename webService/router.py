#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response, request, config
import json
from flask_httpauth import HTTPBasicAuth
from ParsingPerso import ParsingPerso
import ip

# config.host = "192.168.1.10"
config.host = ip.get_ip()

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True

app.config['JSON_AS_ASCII'] = False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'response': 'Unauthorized access'}), 403)


@app.route('/')
def index():
    return "Hello test !"


@app.route('/api/voice', methods = ['GET', 'POST'])
def getLangageNaturel():
    if request.method == 'GET':
        phrase = request.args.get('phrase',default = '', type = str)
    if request.method == 'POST':
        phrase = request.form.get('phrase', default='', type=str)
    Parsing = ParsingPerso()
    phrase = Parsing.parsingPhrase(phrase)
    return make_response(jsonify({'response': phrase.to_json()}), phrase.code)

# Run
if __name__ == '__main__':

    app.run(
        host=config.host,
        port=8080,
        threaded=True
    )