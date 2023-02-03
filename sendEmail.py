import smtplib
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
    res = email.encode('utf-8')
    res = base64.urlsafe_b64encode(res)
    res = res.decode("utf-8")
    key_dict = {"bin": res}
    json_object = json.dumps(key_dict, indent = 4) 
    return json_object

def decodeEmail(enc):
    res = enc.encode('utf-8')
    print(res)
    res = base64.urlsafe_b64decode(res)
    print(res)
    res = res.decode('utf-8')
    return res
