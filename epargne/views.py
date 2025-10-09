from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CompteEpargne
from gestion.models import Adherent


@login_required
def mon_epargne(request):
    try:
        # Récupère le compte épargne via la relation inverse depuis l'adhérent
        compte = request.user.adherent.compte_epargne
    except (Adherent.DoesNotExist, CompteEpargne.DoesNotExist):
        compte = None

    return render(request, 'epargne/mon_epargne.html', {'compte': compte})