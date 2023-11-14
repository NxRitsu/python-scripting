import requests
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http import HTTPStatus
from dotenv import load_dotenv
import os
import socket

def send_mail(line):
    load_dotenv()

    try:
        server = smtplib.SMTP_SSL(os.getenv('EMAIL_SMTP'), os.getenv('EMAIL_PORT'))
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))

        message = "Subject: Erreur\n\nImpossible de joindre le site : "+line

        server.sendmail(
            os.getenv('EMAIL_USER'),
            os.getenv('DESTINATION_EMAIL'),
            message
        )

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        server.quit()

#Exercice 1 & 2
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
            send_mail(line)
        except requests.exceptions.SSLError:
            print(f"SSL missing for {line}")
            send_mail(line)

#Exercice 3
print("EXERCICE 3 : \n")
with open('websites_and_ports.txt', 'r') as fichier:
    # Lire chaque ligne du fichier
    for ligne in fichier:

        # Diviser la ligne en mots en utilisant l'espace comme séparateur afin de prendre uniquement les ports

        website, port_str = ligne.split()

        #On transforme la chaine de caractère en int

        port = int(port_str)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((website, port))
        if result == 0:
            print("Port :", port, " is open")
        else:
            print("Port :", port, " is not open")
        sock.close()

