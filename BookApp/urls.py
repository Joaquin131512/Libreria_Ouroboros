from django.urls import path
from BookApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),#homes de la tienda
    path('store/', views.store, name='store'),#Tienda principal del sitio
    path('profile/', views.profile, name='profile'),#Perfil de usuario
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)