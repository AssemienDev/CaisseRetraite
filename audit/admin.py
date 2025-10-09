from django.contrib import admin
from .models import Audit

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('date_action', 'utilisateur', 'action')
    list_filter = ('utilisateur',)
    search_fields = ('action', 'utilisateur__username')
    readonly_fields = ('date_action', 'utilisateur', 'action') # L'historique ne doit pas être modifié

    def has_add_permission(self, request):
        return False # Empêche l'ajout manuel depuis l'admin