from django.db import models


class RapportFinancier(models.Model):
    # 'date' : Date du rapport, par exemple le premier jour du mois
    date = models.DateField(unique=True)

    # 'total_cotisations'
    total_cotisations = models.DecimalField(max_digits=15, decimal_places=2)

    # 'total_retraites' : Total des paiements de retraite sur la période
    total_retraites = models.DecimalField(max_digits=15, decimal_places=2)

    # 'total_epargnes' : Total des dépôts d'épargne sur la période
    total_epargnes = models.DecimalField(max_digits=15, decimal_places=2)

    # Champ pour stocker le fichier PDF/CSV généré
    fichier_rapport = models.FileField(upload_to='rapports/%Y/%m/', null=True, blank=True)

    date_generation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rapport Financier du {self.date.strftime('%Y-%m')}"

    class Meta:
        ordering = ['-date']