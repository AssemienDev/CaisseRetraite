# Utiliser une seule étape car l'environnement de build et d'exécution est le même
FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copier et installer les dépendances en premier pour profiter du cache Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code
COPY . .

# Donner les permissions d'exécution au script
RUN chmod +x /app/entrypoint.sh

# Créer et passer à l'utilisateur non-root
RUN adduser --system --group nonroot
USER nonroot

# Exposer le port de l’application
EXPOSE 8004

# Lancer le script d'entrée
ENTRYPOINT ["/app/entrypoint.sh"]