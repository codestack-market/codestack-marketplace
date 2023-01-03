from flask import Flask, request, render_template as rt, send_from_directory
import stripe

app = Flask(__name__)

@app.route('/')
def index():
    return rt('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./', 'favicon.ico')