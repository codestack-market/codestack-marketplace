from flask import Blueprint, jsonify, url_for
import stripe

stripe.api_key = 'sk_test_51MMNE4Gc3J3VBJP2YlMeztqt8XTuKuzGKBvPqm0jTOEsyi2aIae87dBjhqHUi9w9T2XOtCVBHH0mspkNrPYXIAIH00YCQ10hME'

blueprint = Blueprint('stripe', __name__.split('.')[0], url_prefix='/payment/')

@blueprint.route('/create_session') # type: ignore
def create_session():
    sess = stripe.checkout.Session.create(
        success_url=url_for('stripe.success', _external=True),
        line_items=[{
            'price': 'price_1MMO4tGc3J3VBJP253GWXL1h',
            'quantity': 69
        }],
        mode='payment'
    )
    return jsonify({
        'session_id': sess.id,
        'pubkey': 'pk_test_51MMNE4Gc3J3VBJP2vuqxUNYGksRHmjgzS1YftjeqfvF8h2BkiqZey57cLN4NpqXl8WExdx2hWszGQO2xlV4jDJiR00zUFkGM2I'
    })

@blueprint.route('/success')
def success():
    return 'Thank you!'