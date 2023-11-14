import requests
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from http import HTTPStatus
from dotenv import load_dotenv
import os
import socket

#Exercice 1
print("EXERCICE 1 :\n")
with open("websites.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        try:
            r = requests.get(line)
            print("Website : ", line)
            print("Réponse ---> ", r.status_code, "\n")
        except requests.exceptions.MissingSchema:
            print(f"Erroneous Schema for url {line}")
        except requests.exceptions.SSLError:
            print(f"SSL missing for {line}")
#Exercice 2
"""with open("websites.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if re.match(r'^https', line):
            if (r.status_code == HTTPStatus.OK):
                sender_email = "votre_email@gmail.com"
                receiver_email = "destination@example.com"
                subject = "Site down"
                body = "Corps de l'e-mail"
                #attachment_path = "/chemin/vers/votre/fichier/attaché.txt"

                # Paramètres du serveur SMTP de Gmail
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = "votre_email@gmail.com"
                smtp_password = "your_password"

                # Création du message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = subject

                # Ajout du corps de l'e-mail
                message.attach(MIMEText(body, 'plain'))

                # Ajout d'une pièce jointe
                with open(attachment_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                    message.attach(part)

                # Connexion au serveur SMTP
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    # Démarrer le chiffrement TLS
                    server.starttls()

                    # Authentification auprès du serveur SMTP
                    server.login(smtp_username, smtp_password)

                    # Envoi de l'e-mail
                    server.send_message(message)

                print("L'e-mail a été envoyé avec succès.")"""
#Exercice 3
print("EXERCICE 3 : \n")
with open('websites_and_ports.txt', 'r') as fichier:
    # Lire chaque ligne du fichier
    for ligne in fichier:

        # Diviser la ligne en mots en utilisant l'espace comme séparateur afin de prendre uniquement les ports

        elements = ligne.split()
        port_str = elements[1]

        #On transforme la chaine de caractère en int

        port = int(port_str)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('duclos.xyz', port))
        if result == 0:
            print("Port :", port, " is open")
        else:
            print("Port :", port, " is not open")
        sock.close()

