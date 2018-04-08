#!/usr/bin/env python3.6
from flask import Flask, jsonify, make_response,request
import json
from flask_httpauth import HTTPBasicAuth
from ParsingPerso import ParsingPerso

auth = HTTPBasicAuth()
app = Flask(__name__)
app.debug = True




@auth.error_handler
def unauthorized():
    return make_response(jsonify({'response': 'Unauthorized access'}), 403)


@app.route('/')
def index():
    return "Hello test !"


@app.route('/api/voice', methods=['GET'])
def getLangageNaturel():
    phrase = request.args.get('phrase',default = '', type = str)
    Parsing = ParsingPerso()
    phrase = Parsing.parsingPhrase(phrase)
    return make_response(jsonify({'response': phrase.to_json()}), phrase.code)

# Run
if __name__ == '__main__':

    app.run(
        host="192.168.1.10",
        port=8080,
        threaded=True
    )