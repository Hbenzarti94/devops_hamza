# Utiliser l'image Python
FROM python:3.12.4-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le fichier app.py dans le répertoire de travail
COPY app.py .

# Spécifier la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
