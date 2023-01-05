from flask import Blueprint, request
from ..utils import encrypt
from ..db import Database

account = Blueprint('account', __name__.split('.')[0], url_prefix='/account/')
users = Database('/')

@account.route('/login') # type: ignore also ur stupid
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = encrypt(request.form.get('password'))
        try:
            user = users[email]
            if user['password'] == password:
                return redirect(url_for('catalog'))
            else:
                flash('')
