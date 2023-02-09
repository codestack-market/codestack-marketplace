import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(receiver,url):
    sender_address = 'help.codestack@gmail.com'
    sender_pass = 'vyiaemvzojgmdzkz'
    receiver_address = receiver
    #Setup the MIME
    message = MIMEMultipart('alternative')
    message['From'] = sender_address
    message['To'] = receiver
    message['Subject'] = 'CodeStack MarketPlace Authentication Email'   #The subject line
    #The body and the attachments for the mail
    sign = 'Codestack Marketplace'
    #mail_content = f'''This email was sent in regards to your recent signup with CodeStack MarketPlace.
    #\nIf this was you, please go to {url}.
    #If this wasn't you, you can ignore this email.
    #\n\n\n\n\n\n\n\n\n\n\n\n\n\n{sign.center(50)}'''
    html = f'''
    <span><a href="www.codestack.ga" target="_blank" style="color: black; font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;">Codestack Marketplace</a></span>
    <table width="100%" height="100%" border="0" cellspacing="0" cellpadding="0">
    <tr>
        <td align="center">
            <img src="https://www.codestack.ga/static/assets/favicon2.png" height="75px" width="75px">
            <h1 style="font-family:'Helvetica Neue',Helvetica,sans-serif; color: black; ">Codestack Marketplace</h1>
            <p style="font-size:14px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#121212;line-height:1.5; color: black;">This email was sent to verify a created account under the email of {receiver}.</p>
            <p style="font-size:14px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#121212;line-height:1.5; color: black;">If this wasn't you, you may discard this email.</p>
            <div align="center">
            <a href="{url}" target="_blank" style="text-decoration:none;display:block;color:#ffffff;background-color:#eb0028;border-radius:4px;width:200px;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:04px;padding-bottom:04px;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;font-size:16px;text-align:center;word-break:keep-all; height: 35px;" align="left">
            <span style="padding-left:04px;padding-right:04px;font-size:16px;display:inline-block;letter-spacing:normal"><span dir="ltr" style="word-break:break-word;line-height:32px"><strong>Verify Email</strong></span></span>
            </a>
            </div>
            <br><br>
            <hr width="85%">
            <div style="background-color: darkgray; font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; margin-top: 25px; color: white; height: 150px; width: 500px; padding-top: 50px;">
            You recieved this email because an account was created on Codestack Marketplace from this email.
            <br><br>
            If this wasn't you, but you still want an account, visit <a href="https://www.codestack.ga/signup" target="_blank" style=" color: white; text-decoration: underline;">https://www.codestack.ga/signup</a>
            </div>
        </td>
    </tr>
    </table>
    '''
    message.attach(MIMEText(html, 'html'))
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
    return res

def decodeEmail(enc):
    res = enc.encode('utf-8')
    print(res)
    res = base64.urlsafe_b64decode(res)
    print(res)
    res = res.decode('utf-8')
    return res
