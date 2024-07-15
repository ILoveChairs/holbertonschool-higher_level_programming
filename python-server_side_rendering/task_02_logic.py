#!/usr/bin/python3

'''
    quickdoc
'''

from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader
import json

# Instanciates the flask app
app = Flask(__name__)

# Get's environment??? also sets template folder as templates
env = Environment(loader=FileSystemLoader('templates'))

# Gets and renders all templates
home_template = env.get_template('index.html').render()
about_template = env.get_template('about.html').render()
contact_template = env.get_template('contact.html').render()
items_template = env.get_template('items.html').render()


@app.route('/')
def home():
    return home_template, 200


@app.route('/about')
def about():
    return about_template, 200


@app.route('/contact')
def contact():
    return contact_template, 200


@app.route('/items')
def items():
    return items_template, 200


if __name__ == '__main__':
    app.run(port=5000)
