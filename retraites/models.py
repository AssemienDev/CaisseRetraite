from django.db import models
from gestion.models import Adherent  # On se base sur le modèle Adherent existant


class DemandeRetraite(models.Model):
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('APPROUVEE', 'Approuvée'),
        ('REJETEE', 'Rejetée'),
    ]

    # 'profil' : Référence à l'utilisateur (adhérent)
    profil = models.ForeignKey(Adherent, on_delete=models.CASCADE, related_name='demandes_retraite',
                               verbose_name="Adhérent")

    # 'montant_retraite' : Montant demandé
    montant_retraite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Montant demandé")

    # 'date_demande' : Date de la demande
    date_demande = models.DateField(auto_now_add=True)

    # 'statut' : Statut de la demande
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='EN_ATTENTE')

    def __str__(self):
        return f"Demande de {self.profil} - {self.get_statut_display()}"

    class Meta:
        verbose_name = "Demande de Retraite"
        verbose_name_plural = "Demandes de Retraite"
        ordering = ['-date_demande']