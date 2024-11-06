# Utiliser une image de base avec Python
FROM python:3.11

# Créer le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers nécessaires dans l'image
COPY app.py /app
COPY model1.pkl /app
COPY model2.pkl /app
COPY scaler1.pkl /app
COPY scaler2.pkl /app


# Copier les fichiers statiques dans le dossier static
RUN mkdir -p /app/static
COPY script.js /app/static/
COPY styles.css /app/static/
COPY arfab.jpeg /app/static/
# Copier les fichiers HTML dans le dossier templates
RUN mkdir -p /app/templates 
COPY hoom.html /app/templates
COPY apropos.html /app/templates
COPY predir.html /app/templates
COPY tester.html /app/templates
  


# Commande pour démarrer l'application Flask
CMD ["python", "app.py"]


