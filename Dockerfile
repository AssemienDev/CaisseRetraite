# Étape 1: Base avec Python et dépendances
FROM python:3.10-slim-buster AS base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape 2: Construction de l'application
FROM base AS build

COPY . .

# Création d'un utilisateur non-root pour la sécurité
RUN adduser --system --group nonroot
USER nonroot

# Exposer le port que Gunicorn utilisera (choisissons 8004 comme convenu)
EXPOSE 8004

# Script de démarrage
ENTRYPOINT ["/app/entrypoint.sh"]