from django.urls import path
from .views import cadastroCliente
 
urlpatterns = [
    path('', cadastroCliente, name='formcli'),
]