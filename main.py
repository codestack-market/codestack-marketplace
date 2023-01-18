'''Flask errors'''
from flask import Flask, request, render_template as rt, send_from_directory
from db import Database
import bp

app = Flask(__name__)
app.config['STRIPE_SECRET'] = '''sk_test_51MMNE4Gc3J3VBJP2YlMeztqt8XTuKuzGKBvPqm0j
TOEsyi2aIae87dBjhqHUi9w9T2XOtCVBHH0mspkNrPYXIAIH00YCQ10hME'''

app.config['STRIPE_PUB'] = '''pk_test_51MMNE4Gc3J3VBJP2vuqxUNYGksRHmjgzS1YftjeqfvF
8h2BkiqZey57cLN4NpqXl8WExdx2hWszGQO2xlV4jDJiR00zUFkGM2I'''

products = Database('products/')

@app.route('/')
def index():
    '''Homepage'''
    return rt('index.html')

@app.route('/favicon.ico')
def favicon():
    '''Favicon route'''
    return send_from_directory('./', 'favicon.ico.png')

@app.route('/marketplace/')
def catalog():
    '''Test catalog'''
    return rt('catalog.html', top_products=products.values()[0:100])

@app.route('/thanks')
def thanks():
    '''Thanks'''
    return rt('thanks.html')

@app.route('/soon', methods=["GET"])
def soon():
    '''Soon'''
    if request.method == 'GET':
        email = request.args.get("emailInput")
        if email is None:
            email = 'empty'
        print(email)
        with open("emails.txt", "w+",encoding='utf-8') as data:
            data.write(f'{email}\n')
        return rt('soon.html')
    return rt('soon.html')

@app.route('/signup', methods =["GET", "POST"])
def signup():
    '''signup'''
    print('e')
    if request.method == "POST":
        email = request.form.get('emailInput')
        password = request.form.get('passwordInput')
        with open("accounts.csv", "w+", encoding='utf-8') as data:
            data.write(f"{email}, {password}")
            data.write('\n')
        return rt('/account/signup.html')
    return rt("/account/signup.html")


@app.errorhandler(404)
def err404(e):
    '''error'''
    return rt('404.html')

@app.errorhandler(500)
def err500(e):
    '''error'''
    return rt('500.html')

@app.errorhandler(429)
def err429(e):
    '''error'''
    return rt('429.html')

app.register_blueprint(bp.stripe.blueprint)
app.register_blueprint(bp.account.blueprint)
app.register_blueprint(bp.internals.blueprint)

if __name__ == '__main__':
    app.run('0.0.0.0', 69420, debug=True)
