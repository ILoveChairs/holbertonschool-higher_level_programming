#!/usr/bin/python3

'''
    quick doc
'''

from flask import Flask, request, jsonify
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {}


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]
    else:
        return None


@app.get('/basic-protected')
@auth.login_required
def index():
    return "Basic Auth: Access Granted"


@app.post('/login')
def login():
    dic = request.get_json()
    return {"access_token": 1}


@app.get('/jwt-protected')
def jwt():
    pass


@app.get('/admin-only')
def admin():
    pass


if __name__ == '__main__':
    app.run()
