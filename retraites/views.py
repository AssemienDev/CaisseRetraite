from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DemandeRetraite
from .forms import DemandeRetraiteForm
from gestion.models import Adherent



@login_required
def mes_demandes(request):
    try:
        adherent = request.user.adherent
        demandes = DemandeRetraite.objects.filter(profil=adherent)
    except Adherent.DoesNotExist:
        demandes = []

    return render(request, 'retraites/mes_demandes.html', {'demandes': demandes})



@login_required
def creer_demande(request):
    adherent = request.user.adherent
    if request.method == 'POST':
        form = DemandeRetraiteForm(request.POST)
        if form.is_valid():
            # Ne pas sauvegarder tout de suite en base de données
            demande = form.save(commit=False)
            # Assigner l'adhérent connecté comme profil de la demande
            demande.profil = adherent
            demande.save()
            return redirect('retraites:mes_demandes')
    else:
        form = DemandeRetraiteForm()

    return render(request, 'retraites/demandes_retraite_form.html', {'form': form})