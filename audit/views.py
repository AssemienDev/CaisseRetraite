from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Audit


# Ce décorateur s'assure que seul un membre du staff peut voir cette page
@user_passes_test(lambda u: u.is_staff)
def log_list(request):
    audit_logs = Audit.objects.select_related('utilisateur').all()
    return render(request, 'audit/audit_log_list.html', {'audit_logs': audit_logs})