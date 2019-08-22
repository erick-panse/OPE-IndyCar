from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Cliente
from funilaria.models import Customer
from django.contrib.auth.decorators import login_required
# Create your views here.
#comentado pra n ficar obrigatorio
@login_required(login_url='/login/' )
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

def veiculo(request):
    veiculos = Veiculo.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'index.html',context={'veiculos':veiculos,'msg':msg})

def novoveiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'salvo')
            except Exception as e:
                messages.error(request,e)
        return redirect(veiculo)
    else:
        form = VeiculoForm()
        return render(request,'formulario_indy_car.html',context={'form':form})

def editar_veiculo(request,id=None):
    instance = get_object_or_404(veiculo,id=id)
    form = VeiculoForm(request.POST or None, instance= instance)
    if form.is_valid():
        try:
            instance=form.save()
            instance.save()
            messages.success(request,'editou')
            return redirect(veiculo)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_indy_car.html',context={'form':form,'instance':instance})

def deletar_veiculo(request,id=None):
    instance = get_object_or_404(veiculo,id=id)
    try:
        instance.delete()
        messages.success(request,'veiculo deletado')
    except Exception as e:
        messages.error(request,'veiculo nao foi deletado')
    return redirect(veiculo)
