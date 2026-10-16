\# School Manager



\## 1. Description



School Manager est un projet développé avec Django et Python. Il permet de découvrir la création d'un site web et l'organisation d'un projet Django.



\## 2. Prérequis



Avant de commencer, il faut installer :



\* Python

\* Git

\* Django

\* Un terminal comme PowerShell ou CMD



\## 3. Installation du projet



Cloner le dépôt Git :



```bash

git clone ADRESSE\_DU\_DEPOT

```



Accéder au dossier du projet :



```bash

cd school\_manager

```



\## 4. Création et activation de l'environnement virtuel



Créer l'environnement virtuel :



```bash

python -m venv venv

```



Activer l'environnement sous Windows avec PowerShell :



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Ou avec CMD :



```cmd

venv\\Scripts\\activate.bat

```



\## 5. Installation des dépendances



Installer les dépendances :



```bash

python -m pip install -r requirements.txt

```



\## 6. Lancement du serveur



Appliquer les migrations :



```bash

python manage.py migrate

```



Démarrer le serveur Django :



```bash

python manage.py runserver

```



Ouvrir le site dans le navigateur :



http://127.0.0.1:8000/



\## 7. URLs disponibles



\* `/` : page d'accueil.

\* `/students/` : page de gestion ou d'affichage des étudiants.



Les pages disponibles dépendent des URL réellement configurées dans le projet.



