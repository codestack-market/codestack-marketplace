import stripe

stripe.api_key = "sk_test_51MMNE4Gc3J3VBJP2v4I1FAEgZl8A5kHpkpiFezFPEmfjODE8fuqnyzD4BoNSP6VPdYp84qPMRlUwFJu1XReTOXr500UAfpxUuf"

def balance():
    return stripe.Balance.retrieve()

def charge(amount, currency, source, description):
    charge = stripe.Charge.create(
        amount = amount,
        currency = currency,
        source = source,
        description = description
    )
    return charge["receipt_url"]

