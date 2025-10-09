# Étape 1: Base avec Python et dépendances
FROM python:3.10-slim-buster AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 2: Construction de l'application
FROM base AS build

WORKDIR /app

# Copier tout le code avant le changement d’utilisateur
COPY . .

# Donner les permissions d’exécution au script
RUN chmod +x /app/entrypoint.sh

# Créer un utilisateur non-root pour la sécurité
RUN adduser --system --group nonroot

# Passer à l'utilisateur nonroot
USER nonroot

# Exposer le port de l’application
EXPOSE 8004

# Lancer le script d'entrée
ENTRYPOINT ["/app/entrypoint.sh"]
