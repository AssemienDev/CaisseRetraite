from django.db import models
from django.db.models import Sum
from gestion.models import Adherent


class CompteEpargne(models.Model):
    """ Représente le compte global d'un adhérent. """
    profil = models.OneToOneField(Adherent, on_delete=models.CASCADE, related_name='compte_epargne',
                                  verbose_name="Adhérent")
    date_ouverture = models.DateField(auto_now_add=True)

    @property
    def solde_total(self):
        """ Calcule le solde en temps réel en additionnant toutes les opérations. """
        total = self.operations.aggregate(Sum('montant'))['montant__sum']
        return total or 0.00

    @property
    def interets_accumules(self):
        """ Calcule le total des intérêts accumulés. """
        total = self.operations.filter(type_operation='INTERET').aggregate(Sum('montant'))['montant__sum']
        return total or 0.00

    def __str__(self):
        return f"Compte épargne de {self.profil}"


class OperationEpargne(models.Model):
    """ Représente une transaction : un dépôt, un retrait, ou un versement d'intérêts. """
    TYPE_CHOICES = [
        ('DEPOT', 'Dépôt'),
        ('INTERET', 'Intérêt'),
    ]

    compte = models.ForeignKey(CompteEpargne, on_delete=models.CASCADE, related_name='operations')
    type_operation = models.CharField(max_length=10, choices=TYPE_CHOICES, default='DEPOT')

    # 'montant' : Montant épargné
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    # 'date' : Date de l'épargne
    date = models.DateField()

    def __str__(self):
        return f"{self.get_type_operation_display()} de {self.montant}€ le {self.date}"

    class Meta:
        ordering = ['-date']