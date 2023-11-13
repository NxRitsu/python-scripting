# Python scripting 🐍
L'objectif de ce dépôt est de s'entraîner à réaliser des scripts python. 

## Exercice 1 🖥️
À partir du fichier `websites.txt`, implémentez un script permettant de vérifier que tous les sites sont bien up. 
Pour ce faire, vous aurez besoin d'utiliser une bibliothèque extérieure, `requests` par exemple.

## Exercice 2 📧
À partir du script précédent, informez l'administrateur que le site est down. 
Pour ce faire, le script devra envoyer un email à une adresse mail spécifiée dans le fichier `.env`.
Vous aurez probablement besoin d'une bibliothèque tierce, `smtplib` par exemple.

## Exercice 3 🔗
Hormis le fait de tester des sites, il est parfois nécessaire de vérifier si des ports sont disponibles.
Updatez le script précédent afin de vérifier les ports, vous avez pour cela le fichier `websites_and_ports.txt`.
Pourquoi ne pas tester `socket` cette fois-ci ?

## Exercice 4 📂
Réalisez un script python permettant de parcourir un dossier. Vous aurez probablement recours à la bibliothèque `os`.
et lister l'ensemble des fichiers doublons présents dans ce dossier (d'une manière récursive).

Le test sur le fait d'être un doublon doit couvrir l'un des critères suivants : 
- un même nommage de fichier
- un fichier ayant le même contenu

L'ensemble des fichiers doublons doit être retourné, par exemple avec le dossier `data` ci-joint votre script doit retourner : 
```
Fichier ayant le même nom

    data/premier_doublon.txt
    data/logs/premier_doublon.txt
    Fichier ayant le même contenu
    data/second_d.ini
    data/subfolder/subfolder/second_doublon.ini
```

## Exercice 5 📏
Réalisez un script python permettant de lister la taille des fichiers par ordre décroissant. 
Votre script ne doit afficher que les fichiers ayant une taille supérieure à 40 octets.
Par ordre décroissant au niveau de la taille de fichier. 

