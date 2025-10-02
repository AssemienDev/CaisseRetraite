from django.shortcuts import render, get_object_or_404, redirect
from .models import Adherent
from .forms import AdherentForm

# Vue pour lister tous les adhérents
def adherent_list(request):
    adherents = Adherent.objects.all()
    return render(request, 'gestion/liste_adherents.html', {'adherents': adherents})

# Vue pour afficher le détail d'un adhérent
def adherent_detail(request, pk):
    adherent = get_object_or_404(Adherent, pk=pk)
    return render(request, 'gestion/detail_adherent.html', {'adherent': adherent})

# Vue pour créer un nouvel adhérent
def adherent_create(request):
    if request.method == 'POST':
        form = AdherentForm(request.POST)
        if form.is_valid():
            adherent = form.save()
            return redirect('gestion:adherent_detail', pk=adherent.pk)
    else:
        form = AdherentForm()
    return render(request, 'gestion/adherent_form.html', {'form': form})

# Vue pour modifier un adhérent existant
def adherent_update(request, pk):
    adherent = get_object_or_404(Adherent, pk=pk)
    if request.method == 'POST':
        form = AdherentForm(request.POST, instance=adherent)
        if form.is_valid():
            form.save()
            return redirect('gestion:adherent_detail', pk=adherent.pk)
    else:
        form = AdherentForm(instance=adherent)
    return render(request, 'gestion/adherent_form.html', {'form': form})