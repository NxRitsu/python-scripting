import requests
import smtplib
import re
from email.mime.text import MIMEText
from http import HTTPStatus
from dotenv import load_dotenv
import os

#Exercice 1
with open("websites.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end = '')
        if re.match(r'^https', line):
            r = requests.get(line)
            print("\n")
            print(line)
            print("\n")
            print(r.status_code)
#Exercice 2
            if (r.status_code == HTTPStatus.OK):
                load_dotenv()
                EMAIL_SMTP = os.getenv("EMAIL_SMTP")
                EMAIL_PASS = os.getenv("EMAIL_PASS")
                EMAIL_USER = os.getenv("EMAIL_USER")
                EMAIL_PORT = os.getenv("EMAIL_PORT")
                DESTINATION_EMAIL = os.getenv("DESTINATION_EMAIL")

                # Création de l'email
                msg = MIMEText("Hello, this is a test email.")
                msg['Subject'] = "Test Email"
                msg['From'] = EMAIL_USER
                msg['To'] = DESTINATION_EMAIL

                # Envoi de l'email
                server = smtplib.SMTP(EMAIL_SMTP)
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(EMAIL_USER, DESTINATION_EMAIL, msg.as_string())
                server.quit()
