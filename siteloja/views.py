from django.shortcuts import render
from .utils import criptografia 
from .models import Clientes

def cadastroCliente(request):
    
    if request.method == 'POST':    
        codigoCliente = request.POST.get('codigoCliente')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        criptosenhas = criptografia(senha)
    
        cliente = Clientes(
            codigoCliente = codigoCliente,
            nome = nome,
            cpf = cpf,
            email = email,
            senha = criptosenhas
        )
 
        cliente.save()
        
        return render(request, 'formcli.html')
    
    return render(request, 'formcli.html')