from django import forms
from .models import Adherent

class AdherentForm(forms.ModelForm):
    class Meta:
        model = Adherent
        # On choisit les champs à afficher dans le formulaire
        fields = ['nom', 'prenom', 'date_naissance', 'numero_securite_sociale']
        # On peut personnaliser les widgets pour avoir un calendrier par exemple
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        }