# backend/Dockerfile
FROM python:3.9

# Créez un répertoire pour l'application
WORKDIR /app

# Copiez les fichiers nécessaires
COPY requirements.txt . 
RUN pip install -r requirements.txt

# Copiez le reste du code
COPY . .

# Commande pour démarrer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


