from flask import Blueprint, request, redirect, url_for, flash, render_template
import sys
sys.path.append('..')
from utils import encrypt
from db import Database

blueprint = Blueprint('account', __name__.split('.')[0], url_prefix='/account/')
users = Database('users/')

@blueprint.route('/login') # type: ignore also ur stupid
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = encrypt(request.form.get('password'))
        try:
            user = users[email]
            if user['password'] == password: # type: ignore
                return redirect(url_for('catalog'))
            else:
                flash('Incorrect password!')
        except KeyError:
            flash('Incorrect email!')
        return redirect(url_for('account.login'))

    return render_template('loginReal.html')