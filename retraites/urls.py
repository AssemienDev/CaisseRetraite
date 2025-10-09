from django.urls import path
from . import views

app_name = 'retraites'

urlpatterns = [
    path('mes-demandes/', views.mes_demandes, name='mes_demandes'),
    path('creer-demande/', views.creer_demande, name='creer_demande'),
]