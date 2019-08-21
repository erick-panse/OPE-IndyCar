from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Cliente
# Create your views here.


def cliente(request):
    clientes = Cliente.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'index.html',context={'clientes':clientes,'msg':msg})

def novocliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'salvo')
            except Exception as e:
                messages.error(request,e)
        return redirect(cliente)
    else:
        form = ClienteForm()
        return render(request,'formulario_indy_car.html',context={'form':form})

def editar_cliente(request,id=None):
    instance = get_object_or_404(Cliente,id=id)
    form = ClienteForm(request.POST or None, instance= instance)
    if form.is_valid():
        try:
            instance=form.save()
            instance.save()
            messages.success(request,'editou')
            return redirect(cliente)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_indy_car.html',context={'form':form,'instance':instance})

