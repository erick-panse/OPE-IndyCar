from django.shortcuts import render,redirect
from django.http import request,HttpResponseRedirect
from funilaria.forms import ClienteForm
from django.contrib import messages
from funilaria.models import Customer
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/' )
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

def login_user(request):
    return render(request, 'login.html')


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
    return redirect('/login/')