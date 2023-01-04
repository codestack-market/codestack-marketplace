from flask import Flask, request, render_template as rt, send_from_directory
import stripe
from db import Database

import bp

app = Flask(__name__)
app.config['STRIPE_SECRET'] = 'sk_test_51MMNE4Gc3J3VBJP2YlMeztqt8XTuKuzGKBvPqm0jTOEsyi2aIae87dBjhqHUi9w9T2XOtCVBHH0mspkNrPYXIAIH00YCQ10hME'
app.config['STRIPE_PUB'] = 'pk_test_51MMNE4Gc3J3VBJP2vuqxUNYGksRHmjgzS1YftjeqfvF8h2BkiqZey57cLN4NpqXl8WExdx2hWszGQO2xlV4jDJiR00zUFkGM2I'

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

app.register_blueprint(bp.stripe.blueprint)

if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True)