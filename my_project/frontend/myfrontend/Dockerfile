# frontend/myfrontend/Dockerfile
FROM node:14

# Créez un répertoire pour l'application
WORKDIR /app

# Copiez les fichiers nécessaires
COPY package*.json ./
RUN npm install
COPY . .

# Commande pour démarrer l'application
CMD ["npm", "start"]

