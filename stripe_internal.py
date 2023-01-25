import stripe

stripe.api_key = "sk_test_51MMNE4Gc3J3VBJP2v4I1FAEgZl8A5kHpkpiFezFPEmfjODE8fuqnyzD4BoNSP6VPdYp84qPMRlUwFJu1XReTOXr500UAfpxUuf"

def balance():
    return stripe.Balance.retrieve()

def charge(card_number, exp_month, exp_year, cvc, amount, currency, description):
    token = stripe.Token.create(
    card={
        "number": str(card_number),
        "exp_month": str(exp_month),
        "exp_year": str(exp_year),
        "cvc": str(cvc)
    })
    payment = stripe.Charge.create(
        amount = str(amount),
        currency = currency,
        source = token.id,
        description = description
    )
    return payment["receipt_url"]


