import smtplib
import json
import random
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(receiver,url):
    sender_address = 'help.codestack@gmail.com'
    sender_pass = 'vyiaemvzojgmdzkz'
    receiver_address = receiver
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver
    message['Subject'] = 'CodeStack MarketPlace Authentication Email'   #The subject line
    #The body and the attachments for the mail
    sign = 'Sincerely,\nCodeStack MarketPlace'
    mail_content = f'''This email was sent in regards to your recent signup with CodeStack MarketPlace.
    \nIf this was you, please go to {url}\n\n\n\n\n\n\n\n\n\n\n\n\n\n{sign.center(50)}.
    If this wasn't you, you can ignore this email.'''
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def encodeEmail(email):
    res = int(''.join(format(ord(i), '08b') for i in email))
    res_int = random.randint(0,10)
    res = res_int*res
    res = res_int.to_bytes(100,"big")
    res = base64.urlsafe_b64encode(res)
    res = res.decode("utf-8") 
    key_dict = {"id": res, "key": res_int}
    json_object = json.dumps(key_dict, indent = 4) 
    return json_object

def decodeEmail(json_object):
    res = json_object["id"]
    res = bytes(res ,'utf-8')
    res = base64.urlsafe_b64decode(res)
    res = int.from_bytes(100, "big")
    res = res/int(json_object['key'])
    binary_values = str(res)
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string 

x = encodeEmail("ab7552@pleasantonusd.net")
print(x)
y = decodeEmail(x)
print(y)
