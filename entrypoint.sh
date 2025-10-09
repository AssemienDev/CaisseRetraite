#!/bin/sh

# Appliquer les migrations de la base de données
echo "Applying database migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Démarrer le serveur Gunicorn
echo "Starting Gunicorn server..."
gunicorn CaisseRetraite.wsgi:application --bind 0.0.0.0:8004 --workers 3