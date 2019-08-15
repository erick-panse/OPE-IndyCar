from django.shortcuts import render
from django.http import request,HttpResponseRedirect
from .forms import ClienteForm
# Create your views here.

def novocliente(request):
    #testando
    if request.method == 'POST':
        print('POST')
        form = ClienteForm(request.POST)
        if form.is_valid():
            print('CPF = ',request.POST['cpf'])
            print('NOME = ',request.POST['nome'])
            print('ENDERECO = ',request.POST['endereco'])
            print('EMAIL = ',request.POST['email'])
            print('CEP = ',request.POST['cep'])
        return HttpResponseRedirect('formulario_indy_car.html')
    else:
        print('GET')
        form = ClienteForm()
        return render(request,'formulario_indy_car.html',context={'form':form})

