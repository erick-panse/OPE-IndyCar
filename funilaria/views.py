from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm,EmpresaForm
from django.contrib import messages
from funilaria.models import Cliente,Customer,Empresa
from django.contrib.auth.decorators import login_required
# Create your views here.
#comentado pra n ficar obrigatorio
def index (request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def cliente(request):
    clientes = Cliente.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'clientes.html',context={'clientes':clientes,'msg':msg})

@login_required(login_url='/login/')
def novocliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST or None)
        print(form_cliente.is_valid())
        if form_cliente.is_valid():
            try:
                form_cliente.save()
                messages.success(request,'salvo')
            except Exception as e:
                messages.error(request,e)
            return redirect(cliente)
        else:
            return render(request,'formulario_indy_car.html',context={'form_cliente':form_cliente})
    else:
        form_cliente = ClienteForm()
        return render(request,'formulario_indy_car.html',context={'form_cliente':form_cliente})

@login_required(login_url='/login/')
def editar_cliente(request,id=None):
    instance_cliente = get_object_or_404(Cliente,id=id)
    print(instance_cliente.modelo_veiculo)
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

@login_required(login_url='/login/')
def deletar_cliente(request,id=None):
    instance = get_object_or_404(Cliente,id=id)
    try:
        instance.delete()
        messages.success(request,'cliente deletado')
    except Exception as e:
        messages.error(request,'cliente nao foi deletado')
    return redirect(cliente)

@login_required(login_url='/login/')
def empresa(request):
    empresas = Empresa.objects.all().order_by('id')
    msg=messages.get_messages(request)
    return render(request,'empresas.html',context={'empresas':empresas,'msg':msg})

@login_required(login_url='/login/')
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
        return render(request,'formulario_empresa.html',context={'form':form})

@login_required(login_url='/login/')
def editar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    form = EmpresaForm(request.POST or None, instance= instance)
    if form.is_valid():
        try:
            instance=form.save()
            instance.save()
            messages.success(request,'editou')
            return redirect(empresa)
        except Exception as e:
            messages.error(request,e)
    return render(request,'formulario_empresa.html',context={'form':form,'instance':instance})

@login_required(login_url='/login/')
def deletar_empresa(request,id=None):
    instance = get_object_or_404(Empresa,id=id)
    try:
        instance.delete()
        messages.success(request,'empresa deletada')
    except Exception as e:
        messages.error(request,'empresa nao foi deletada')
    return redirect(empresa)

