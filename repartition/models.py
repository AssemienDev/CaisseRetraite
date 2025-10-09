from django.db import models
from retraites.models import DemandeRetraite  # On se lie à la demande de retraite approuvée


class FondsRetraite(models.Model):
    """ Modèle simple pour suivre le montant total. Il n'y aura qu'une seule ligne dans cette table. """
    # 'montant_total' : Montant total des fonds
    montant_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    derniere_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fonds de Retraite Global : {self.montant_total} €"

    class Meta:
        verbose_name_plural = "Fonds de Retraite"


class PaiementRetraite(models.Model):
    """ Modèle qui représente l'historique des paiements. """
    # Lien vers la demande de retraite qui a été approuvée
    demande = models.ForeignKey(DemandeRetraite, on_delete=models.PROTECT, limit_choices_to={'statut': 'APPROUVEE'})

    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()

    def __str__(self):
        return f"Paiement de {self.montant}€ à {self.demande.profil} le {self.date_paiement}"

    class Meta:
        ordering = ['-date_paiement']