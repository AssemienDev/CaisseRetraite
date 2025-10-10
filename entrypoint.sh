#!/bin/sh

# Appliquer les migrations de la base de données
echo "Applying database migrations..."
python manage.py migrate

# Créer le superutilisateur si il n'existe pas
echo "Creating superuser if not exists..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="crrae").exists():
    User.objects.create_superuser("crrae", "crrae@gmail.com", "mdp12354@A")
    print("Superuser created")
else:
    print("Superuser already exists")
END

# Collecter les fichiers statiques
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Démarrer le serveur Gunicorn
echo "Starting Gunicorn server..."
gunicorn CaisseRetraite.wsgi:application --bind 0.0.0.0:8004 --workers 3
