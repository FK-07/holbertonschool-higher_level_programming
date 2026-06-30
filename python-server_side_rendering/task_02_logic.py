#!/usr/bin/python3
"""
Flask application displaying dynamic content using Jinja loops and conditions.
"""
import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the About Us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the Contact Us page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Reads items from items.json and renders items.html."""
    items_list = []
    filename = 'items.json'

    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except Exception:
            items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(port=5000)
