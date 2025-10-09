from django.contrib import admin
from .models import DemandeRetraite

@admin.register(DemandeRetraite)
class DemandeRetraiteAdmin(admin.ModelAdmin):
    list_display = ('profil', 'montant_retraite', 'date_demande', 'statut')
    list_filter = ('statut',)
    search_fields = ('profil__nom', 'profil__prenom')
    # Permet de modifier le statut directement depuis la liste
    list_editable = ('statut',)