#!/usr/bin/python3

'''
    quickdoc
'''

from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
import sqlite3
import json
import csv

# Instanciates the flask app
app = Flask(__name__)

# Get's environment??? also sets template folder as templates
env = Environment(loader=FileSystemLoader('templates'))

# Gets and renders all templates
home_render = env.get_template('index.html').render()
about_render = env.get_template('about.html').render()
contact_render = env.get_template('contact.html').render()

items_template = env.get_template('items.html')
product_display_template = env.get_template('product_display.html')


# Magic for sql returning dict instead of tuple
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def home():
    return home_render, 200


@app.route('/about')
def about():
    return about_render, 200


@app.route('/contact')
def contact():
    return contact_render, 200


@app.route('/items')
def items():
    with open("items.json", 'r') as f:
        data = json.load(f)
    items = data.get("items")
    items_render = items_template.render(items=items)
    return items_render, 200


@app.route('/products')
def products():
    # if data is string, is an error message
    data: list[dict] | str | None = None
    error = False
    try:
        # Check whether source is json or csv, error message if not.
        source = request.args.get("source")
        if source == "json":
            with open("products.json", 'r') as f:
                data = json.load(f)
        elif source == "csv":
            data = []
            with open("products.csv", 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        elif source == "sql":
            sql_conn = sqlite3.connect("products.db")
            # Magic for sql returning dict instead of tuple
            sql_conn.row_factory = dict_factory
            cur = sql_conn.cursor()
            cur.execute("SELECT * FROM Products;")
            data = cur.fetchall()
            cur.close()
            sql_conn.close()
            
        else:
            raise Exception("Wrong source")
        # Check id
        if query_id := request.args.get("id"):
            for item in data:
                if str(item.get("id")) == query_id:
                    data = [item]
                    break
            else:
                raise Exception("Product not found")
        # Check if data is empty
        if not data:
            raise Exception("No items found")
    except Exception as e:
        data = str(e)
        error = True
    products_display_render = product_display_template.render(data=data, error=error)
    return products_display_render, 200


if __name__ == '__main__':
    app.run(port=5000)
