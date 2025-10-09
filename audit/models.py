from django.db import models
from django.conf import settings  # Pour référencer le modèle User


class Audit(models.Model):
    # 'action' : Description de l'action
    action = models.CharField(max_length=255)

    # 'date_action' : Date et heure de l'action
    date_action = models.DateTimeField(auto_now_add=True)

    # 'utilisateur' : Référence à l'utilisateur
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        user = self.utilisateur.username if self.utilisateur else "Système"
        return f"[{self.date_action.strftime('%Y-%m-%d %H:%M')}] {user}: {self.action}"

    class Meta:
        ordering = ['-date_action']