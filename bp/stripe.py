from flask import Blueprint, jsonify, url_for
import stripe

stripe.api_key = 'sk_test_'

blueprint = Blueprint(__name__.split('.')[0], 'stripe', url_prefix='/payment/')

@blueprint.route('/create_session') # type: ignore
def create_session():
    sess = stripe.checkout.Session.create(
        success_url=url_for('stripe.success')
    )
    return jsonify({

    })