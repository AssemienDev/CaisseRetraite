from django.contrib import admin
from .models import CompteEpargne, OperationEpargne

class OperationEpargneInline(admin.TabularInline):
    model = OperationEpargne
    extra = 1

@admin.register(CompteEpargne)
class CompteEpargneAdmin(admin.ModelAdmin):
    list_display = ('profil', 'solde_total', 'interets_accumules', 'date_ouverture')
    readonly_fields = ('solde_total', 'interets_accumules') # Les champs calculés ne sont pas éditables
    inlines = [OperationEpargneInline]