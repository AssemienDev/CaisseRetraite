from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion import views as gestion_views # Importer les vues de l'app gestion
from django.conf import settings
from django.conf.urls.static import static

from gestion.views import logoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL du tableau de bord
    path('', gestion_views.dashboard, name='dashboard'),

    # Inclure les URLs de chaque application
    path('retraites/', include('retraites.urls')),
    path('epargne/', include('epargne.urls')),
    path('rapports/', include('rapports.urls')),
    path('audit/', include('audit.urls')),

    # URLs d'authentification
    path('connexion/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('deconnexion/', logoutView, name='logout'),
]

# Uniquement en mode DEBUG, pour servir les fichiers uploadés (comme les rapports)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)