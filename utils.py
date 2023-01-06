import hashlib

def encrypt(input_str):
    a = hashlib.new('sha256')
    a.update(input_str)
    return a.hexdigest()