from django.apps import AppConfig
from django.urls import path
from app_cad_usuarios import views
urlpatterns = [
    path('')
    
    
]
class AppCadUsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_cad_usuarios'
    
