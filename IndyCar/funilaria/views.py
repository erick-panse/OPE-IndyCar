from django.shortcuts import render
from django.http import request
from .forms import ClienteForm
# Create your views here.

def novocliente(request):
    #testando
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            return render(request,'formulario indy car.html',context={'form':form})
    else:
        form = ClienteForm()
        return render(request,'formulario indy car.html',context={'form':form})

