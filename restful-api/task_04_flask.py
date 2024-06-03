#!/usr/bin/python3

'''
    quickdoc
'''

from flask import Flask
from flask import request
from flask import jsonify
import json


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    '''
        quickdoc
    '''

    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    '''
        quickdoc
    '''

    return jsonify(users)

@app.route("/status")
def status():
    '''
        quickdoc
    '''

    return "OK"

@app.route("/status/<usr>")
def status(usr):
    '''
        quickdoc
    '''

    if usr in users:
        return jsonify(users[usr])

@app.post('/add__user')
def login():
    if request.method == 'POST':
        json.dumps(request.form['username'])

if __name__ == "__main__":
    app.run()
