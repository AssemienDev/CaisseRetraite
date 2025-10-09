from django.contrib import admin
from .models import FondsRetraite, PaiementRetraite

@admin.register(FondsRetraite)
class FondsRetraiteAdmin(admin.ModelAdmin):
    list_display = ('montant_total', 'derniere_mise_a_jour')

@admin.register(PaiementRetraite)
class PaiementRetraiteAdmin(admin.ModelAdmin):
    list_display = ('demande', 'montant', 'date_paiement')
    list_filter = ('date_paiement',)
    search_fields = ('demande__profil__nom',)