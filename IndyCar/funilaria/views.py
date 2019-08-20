from django.shortcuts import render,redirect
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Customer
# Create your views here.


def cliente(request):
    clientes = Customer.objects.all().order_by('id')
    return render(request,'index.html',context={'clientes':clientes})

def novocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'foi')
        else:
            messages.error(request,'n foi')
        return redirect(cliente)
    else:
        form = ClienteForm()
        return render(request,'formulario_indy_car.html',context={'form':form})

