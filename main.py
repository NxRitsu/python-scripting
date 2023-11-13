import requests
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
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
                sender_email = "poalacassenito101@gmail.com"
                receiver_email = "melvin.prevost@ecoles-espi.net"
                subject = "Site down"
                body = "Corps de l'e-mail"
                #attachment_path = "/chemin/vers/votre/fichier/attaché.txt"

                # Paramètres du serveur SMTP de Gmail
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "poalacassenito101@gmail.com"
                smtp_password = "6124asgg"

                # Création du message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = subject

                # Ajout du corps de l'e-mail
                message.attach(MIMEText(body, 'plain'))

                # Ajout d'une pièce jointe
                """with open(attachment_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                    message.attach(part)"""

                # Connexion au serveur SMTP
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    # Démarrer le chiffrement TLS
                    server.starttls()

                    # Authentification auprès du serveur SMTP
                    server.login(smtp_username, smtp_password)

                    # Envoi de l'e-mail
                    server.send_message(message)

                print("L'e-mail a été envoyé avec succès.")
