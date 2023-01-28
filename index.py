'''Flask errors'''
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, render_template as rt, send_from_directory, session, jsonify
from db import Database

app = Flask(__name__)

app.secret_key = '[\xc6\x11\x0b8\x1am\xc5\xdf\xb8Snd(\r\x9b'

app.config['STRIPE_SECRET'] = '''sk_test_51MMNE4Gc3J3VBJP2v4I1FAEgZl8A5kHpkpiFezF
PEmfjODE8fuqnyzD4BoNSP6VPdYp84qPM
RlUwFJu1XReTOXr500UAfpxUuf'''

app.config['STRIPE_PUB'] = '''pk_test_51MMNE4Gc3J3VBJP2CerBgZNbOV1DG
kfcQh672TAF4zQSKejz46AHOuRztD
ceTnvvkVYhloAAOMbRBm4b50JlhISs004iChl6sU'''

client = MongoClient("mongodb+srv://codestack:avneh@cluster0.jsufux8.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client['CodeStack']
accs = db["accounts"]
emails = db["emails"]

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

@app.route('/soon', methods=["GET", "POST"])
def soon():
    '''Soon'''
    if request.method == 'POST':
        response = json.dumps(request.get_json())
        response = json.loads(response)
        print(response)
        email = response["email"]
        emails.insert_one({"email":email})
        return rt('soon.html')
    return rt('soon.html')

@app.route('/signup', methods =["GET", "POST"])
def signup():
    '''signup'''
    if request.method == "POST":
        response = json.dumps(request.get_json())
        response = json.loads(response)
        print(response)
        email = response["email"]
        phone = str(response["phone"].lower())
        password = str(response["password"])
        fname = response["fname"]
        session['username'] = fname
        lname = response["lname"]
        if phone != "none":
            accs.insert_one({"contact":phone, "password":password, "firstname":fname, "lastname":lname})
        else:
            accs.insert_one({"contact":email, "password":password, "firstname":fname, "lastname":lname})
        return jsonify(
            success="true"
        )
    return rt("/account/signup.html")

@app.route('/logout', methods =["POST"])
def logout():
    '''logout'''
    if request.method == "POST":
        print(request)
        # logout


@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method =="POST":
        contact = json.dumps(request.get_json())
        contact = json.loads(contact)
        email = contact["email"].lower()
        phone = str(contact["phone"].lower())
        password = str(contact["password"].lower())
        if phone != "none":
            print("e")
            query = accs.find({"contact": email})
            print(query)
            for x in query:
                print(x)
                if x["password"] == password:
                    auth = 'pass'
                    return rt("/account/loginReal.html", auth=auth)
                else:
                    auth = 'fail'
                    return rt("/account/loginReal.html", auth=auth)
        else:
            query = accs.find({"contact": phone})
            for x in query:
                if x["password"] == password:
                    return rt("/account/loginReal.html", auth="pass")
                else:
                    return rt("/account/loginReal.html", auth="fail")
    return rt("/account/loginReal.html", auth ='')
                                 
@app.route('/confirmSignup')
def confirmSignup():
    return rt('thanks.html')

@app.route('/sudo-mode')
def sudoMode():
    return rt("/account/sudo-mode.html")

@app.route("/email-auth")
def emailAuth():
    return rt("/account/email-auth.html")

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


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
