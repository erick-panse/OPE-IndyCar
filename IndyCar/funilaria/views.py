from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Cliente
from funilaria.models import Customer
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='/login/' )
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

def login_user(request):
    return render(request, 'login.html')

'''
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')'''
