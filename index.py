'''Flask errors'''
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, render_template as rt, send_from_directory,session, jsonify, url_for, redirect
from stripe_internal import charge
from webscraper import scrape_py, scrape_js
from sendEmail import sendMail, encodeEmail, decodeEmail
global enc
enc =""

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
    return rt('index.html')

@app.route('/favicon.ico')
def favicon():
    '''Favicon route'''
    return send_from_directory('./', 'favicon.ico.png')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return rt('/account/logout.html')

@app.route('/marketplace/')
def catalog():
    '''Test catalog'''
    return rt('marketplace/catalog.html')

@app.route('/marketplace/item')
def item():
    return rt("marketplace/item.html")

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

@app.route('/signup')
def signup():
    '''signup'''
    return rt("/account/signup.html")

@app.route('/robot-chat')
def robotChat():
    return rt("/support/robot-chat.html")

@app.route('/csudo', methods =['POST'])
def cSudo():
    '''csudo'''
    if request.method == 'POST':
        response = json.dumps(request.get_json())
        response = json.loads(response)
        password = str(response["password"].lower())
        print(password)
        # find pswrd and stuff idk
        return jsonify(
            success="true"
        )

@app.route('/orders')
def orders():
    return rt("account/orders.html")

@app.route('/forgotPassword', methods =["GET", "POST"])
def forgotPassword():
    '''forgotPassword'''
    return rt("/account/forgotPassword.html")

@app.route('/getauth', methods=["GET", "POST"])
def getAuth():
    if request.method == 'POST':
        print('e')
        response = json.dumps(request.get_json())
        response = json.loads(response)
        print(response)
        email = response["email"]
        global enc
        enc = encodeEmail(email)
        url = f"https://www.codestack.ga/verify?key={enc}"
        sendMail(email, url)
        return jsonify(
            success ="true"
        )
    return rt('/account/email_sent.html')

@app.route('/verify', methods=["GET", "POST"])
def verify_email():
    if request.method == "POST":
        print('e')
        global enc
        url_end = enc
        email_send = decodeEmail(url_end)
        response = json.dumps(request.get_json())
        response = json.loads(response)
        email = response["email"]
        phone = str(response["phone"])
        password = str(response["password"])
        fname = response["fname"]
        session['username'] = fname
        lname = response["lname"]
        print(response)
        if email == email_send:
            accs.insert_one({"contact":email, "password":password, "firstname":fname, "lastname":lname})
        elif phone != "none":
            accs.insert_one({"contact":phone, "password":password, "firstname":fname, "lastname":lname})
        else:
            return jsonify(
            success="true"
        )   
    return rt('thanks.html')
    

@app.route('/support')
def support():
    '''support'''
    return rt('/support/support.html')


@app.route('/license')
def license():
    return rt('legal/license.html')


@app.route('/licenseRaw')
def licenseRaw():
    return rt('legal/LICENSE')

@app.route('/tos')
def tos():
    return rt('legal/TOS.html')

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
                    return jsonify(
                        status="pass"
                    )
                else:
                    return jsonify(
                        status="fail"
                    )
        else:
            query = accs.find({"contact": phone})
            for x in query:
                if x["password"] == password:
                    return jsonify(
                        status="pass"
                    )
                else:
                    return jsonify(
                        status="fail"
                    )
        return jsonify(
            status="fail"
        )
    return rt("/account/loginReal.html")
                                 
@app.route('/sudo-mode', methods =['GET', 'POST'])
def sudoMode():
    '''sudoMode'''
    return rt("/account/sudo-mode.html")

@app.route('/settings')
def settings():
    return rt('/settings/settings.html')

@app.route('/settings/account')
def settingsAccount():
    return rt('/settings/account.html')

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
