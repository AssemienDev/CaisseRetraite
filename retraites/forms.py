from django import forms
from .models import DemandeRetraite


class DemandeRetraiteForm(forms.ModelForm):
    class Meta:
        model = DemandeRetraite
        # L'utilisateur ne doit saisir que le montant. Le reste sera géré par la vue.
        fields = ['montant_retraite']
        labels = {
            'montant_retraite': 'Montant de la retraite mensuelle souhaité'
        }