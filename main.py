import requests
import smtplib
import re
from email.mime.text import MIMEText
from http import HTTPStatus

with open("websites.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end = '')
        if re.match(r'^https', line):
            r = requests.get(line)
            print("\n")
            print(line)
            print("\n")
            print(r.status_code)
            if (r.status_code == HTTPStatus.OK):
                # Création de l'email
                msg = MIMEText("Hello, this is a test email.")
                msg['Subject'] = "Test Email"
                msg['From'] = "melvinlh76@example.com"
                msg['To'] = "receiver@example.com"

                # Envoi de l'email
                server = smtplib.SMTP('smtp.example.com')
                server.login("sender@example.com", "password")
                server.sendmail("sender@example.com", "receiver@example.com", msg.as_string())
                server.quit()
