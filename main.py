from flask import Flask, request, render_template as rt, send_from_directory
import stripe
from db import Database

app = Flask(__name__)
products = Database('/products/')

@app.route('/')
def index():
    return rt('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./', 'favicon.ico')

@app.route('/catalog')
def catalog():
    return rt('catalog.html', top_products=products.values()[0:100])

if __name__ == '__main__':
    app.run('0.0.0.0', 80)