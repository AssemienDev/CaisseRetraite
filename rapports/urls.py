from django.urls import path
from . import views

app_name = 'rapports'

urlpatterns = [
    path('', views.liste_rapports, name='liste_rapports'),
]