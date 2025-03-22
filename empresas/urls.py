from django.urls import path
from .views import homeEmpresas

urlpatterns = [
    path('', homeEmpresas, name='home_empresas'),
]