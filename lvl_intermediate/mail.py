import smtplib
import ssl 
from email.message import EmailMessage
import sys
sys.path.insert(1, 'C:\\Users\\nike9\\OneDrive\\Python practice\\projects\\config')

from projects.config.globals import SENDER_EMAIL, SENDER_TOKEN, RECEIVER_EMAIL


def build_the_message(subject, message):
    email_message = EmailMessage()
    email_message['From'] = SENDER_EMAIL
    email_message['To']  = RECEIVER_EMAIL
    email_message['Subject'] = subject
    email_message.set_content(message)

    return email_message

def send(msg):
    context = ssl.create_default_context()

     # Create an instance of an SMTP connection to Gmail
    print("connecting...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
       # Authenticate
       server.login(
          SENDER_EMAIL,
          SENDER_TOKEN
       )
       # Send the email
       server.sendmail(
           SENDER_EMAIL,
           RECEIVER_EMAIL,
           msg.as_string()
       )
    
    print("Email sent!!")