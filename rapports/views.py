from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RapportFinancier


@login_required
def liste_rapports(request):
    rapports = RapportFinancier.objects.all()
    return render(request, 'rapports/liste_rapports.html', {'rapports': rapports})