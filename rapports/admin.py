from django.contrib import admin
from .models import RapportFinancier

@admin.register(RapportFinancier)
class RapportFinancierAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_cotisations', 'total_retraites', 'total_epargnes', 'fichier_rapport')
    # Les rapports une fois générés ne devraient pas être modifiés
    readonly_fields = ('date', 'total_cotisations', 'total_retraites', 'total_epargnes', 'date_generation')