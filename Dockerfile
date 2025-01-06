# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le modèle et le reste du code de l'application
COPY model.pkl .
COPY app.py .
COPY wsgi.py .

# Copier le répertoire templates dans l'image Docker
COPY templates/ /app/templates/

# Définir une variable d'environnement pour Flask en mode production
ENV FLASK_ENV=production

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Spécifier la commande pour exécuter l'application avec Waitress
CMD ["python", "wsgi.py"]
