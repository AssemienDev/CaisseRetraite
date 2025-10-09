from django.urls import path
from . import views

app_name = 'epargne'

urlpatterns = [
    path('mon-epargne/', views.mon_epargne, name='mon_epargne'),
]