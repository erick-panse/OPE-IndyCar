from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def novo_usuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário cadastrado com sucesso !')
        else:
             messages.error(request,'Form inválido!')
        return redirect('/cliente/')
    else:
        form = UserRegisterForm()
    return render(request,'novo-usuario.html',context={'form':form})

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
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