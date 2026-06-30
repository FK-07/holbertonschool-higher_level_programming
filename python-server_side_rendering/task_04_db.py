#!/usr/bin/python3
"""
Flask application displaying product data from JSON, CSV, or SQLite database.
"""
import csv
import json
import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Reads products from products.json file."""
    if not os.path.exists('products.json'):
        return []
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv_products():
    """Reads products from products.csv file."""
    products = []
    if not os.path.exists('products.csv'):
        return products
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products


def read_sql_products():
    """Reads products from products.db SQLite database."""
    products = []
    if not os.path.exists('products.db'):
        return None
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
        return products
    except sqlite3.Error:
        return None


@app.route('/')
def home():
    """Renders Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders About Us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders Contact Us page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Renders Items page from items.json."""
    items_list = []
    if os.path.exists('items.json'):
        try:
            with open('items.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except Exception:
            items_list = []
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Renders product list filtered by source (json, csv, sql) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        product_list = read_json_products()
    elif source == 'csv':
        product_list = read_csv_products()
    elif source == 'sql':
        product_list = read_sql_products()
        if product_list is None:
            return render_template(
                'product_display.html',
                error="Database error"
            )

    if product_id is not None:
        try:
            p_id = int(product_id)
            product_list = [p for p in product_list if p.get('id') == p_id]
            if not product_list:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(port=5000)
