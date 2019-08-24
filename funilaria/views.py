from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Cliente,Customer,Empresa
from django.contrib.auth.decorators import login_required
# Create your views here.
#comentado pra n ficar obrigatorio
@login_required(login_url='/login/' )

def index (request):
    return render(request, 'index.html')


def cliente(request):
    clientes = Cliente.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'Clientes.html',context={'clientes':clientes,'msg':msg})

def novocliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST or None)
        if form_cliente.is_valid():
            try:
                form_cliente.save()
                messages.success(request,'salvo')
            except Exception as e:
                messages.error(request,e)
        return redirect(cliente)
    else:
        form_cliente = ClienteForm()
        return render(request,'formulario_indy_car.html',context={'form_cliente':form_cliente,})

def editar_cliente(request,id=None):
    instance_cliente = get_object_or_404(Cliente,id=id)
    form_cliente = ClienteForm(request.POST or None, instance= instance_cliente)
    if form_cliente.is_valid():
        try:
            instance_cliente=form_cliente.save(commit=False)
            instance_cliente.save()
            messages.success(request,'editou')
            return redirect(cliente)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_indy_car.html',context={'form_cliente':form_cliente,'instance_cliente':instance_cliente})

def deletar_cliente(request,id=None):
    instance = get_object_or_404(Cliente,id=id)
    try:
        instance.delete()
        messages.success(request,'cliente deletado')
    except Exception as e:
        messages.error(request,'cliente nao foi deletado')
    return redirect(cliente)

def empresa(request):
    empresas = Empresa.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'index.html',context={'empresas':empresas,'msg':msg})

def novoempresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'salvo')
            except Exception as e:
                messages.error(request,e)
        return redirect(empresa)
    else:
        form = EmpresaForm()
        return render(request,'formulario_indy_car.html',context={'form':form})

def editar_empresa(request,id=None):
    instance = get_object_or_404(empresa,id=id)
    form = EmpresaForm(request.POST or None, instance= instance)
    if form.is_valid():
        try:
            instance=form.save()
            instance.save()
            messages.success(request,'editou')
            return redirect(empresa)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_indy_car.html',context={'form':form,'instance':instance})

def deletar_empresa(request,id=None):
    instance = get_object_or_404(empresa,id=id)
    try:
        instance.delete()
        messages.success(request,'empresa deletado')
    except Exception as e:
        messages.error(request,'empresa nao foi deletado')
    return redirect(empresa)

