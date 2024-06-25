#!/usr/bin/python3

'''
    quickdoc
'''

from flask import Flask, request, jsonify


app = Flask(__name__)

users = {}


@app.route("/")
def home_getter():
    '''
        quickdoc
    '''

    return "Welcome to the Flask API!"


@app.route("/data")
def data_getter():
    '''
        quickdoc
    '''

    return [x for x in users]


@app.route("/status")
def status_getter():
    '''
        quickdoc
    '''

    return "OK"


@app.route("/users")
def users_getter():
    '''
        quickdoc
    '''

    return [x for x in users]


@app.route("/users/<usr>")
def user_getter(usr):
    '''
        quickdoc
    '''

    if usr in users:
        return users[usr]
    else:
        return {"error": "User not found"}, 404


@app.post('/add_user')
def user_adder():
    dic = request.get_json(force=True, silent=True)
    if dic is None:
        return {"error": "Not valid"}, 400
    if "username" not in dic or not isinstance(dic["username"], str) \
        or not dic["username"].isalpha():
        return {"error": "Not valid"}, 400
    users[dic["username"]] = dic
    return dic


if __name__ == "__main__":
    app.run()
