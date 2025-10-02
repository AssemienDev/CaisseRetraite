from django.urls import path
from . import views

app_name = 'gestion'  # Namespace pour éviter les conflits de noms d'URL

urlpatterns = [
    # Page d'accueil de l'application : liste des adhérents
    path('', views.adherent_list, name='adherent_list'),

    # Page de détail d'un adhérent
    path('adherent/<int:pk>/', views.adherent_detail, name='adherent_detail'),

    # Page pour ajouter un nouvel adhérent
    path('adherent/ajouter/', views.adherent_create, name='adherent_create'),

    # Page pour modifier un adhérent
    path('adherent/<int:pk>/modifier/', views.adherent_update, name='adherent_update'),
]