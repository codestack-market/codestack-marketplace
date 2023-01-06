from flask import Blueprint, jsonify, request, url_for
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from os import environ as env

blueprint = Blueprint('internal', __name__.split('.')[0], url_prefix='/internals/')

@blueprint.route('/user_info') # type: ignore
def uinfo():
    token = request.args.get('token', 'totally signed')
    try:
        data = URLSafeTimedSerializer(env['SECRET_KEY']).loads(token, max_age=2952000)

    except (BadSignature, SignatureExpired, KeyError):
        return jsonify({
            'error': 'AUTH_INVALID',
            'redirect': url_for('account.login')
        })