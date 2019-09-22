from django.shortcuts import render,redirect
from django.contrib import messages
#UserCreationForm e EditProfileForm customizados 
from .forms import UsuarioForm,EditarUsuarioForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def pagina_inicial(request):
    return render(request, 'pagina-inicial.html')

@login_required(login_url='/login/')
def index (request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def perfil_usuario(request):
    msg=messages.get_messages(request)
    return render(request,'perfil.html',context={'user':request.user,'msg':msg})

@login_required(login_url='/login/')
def novo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect(perfil_usuario)
        else:
            messages.error(request,'Não foi possível cadastrar o usuário')
            return render(request,'novo-usuario.html',context={'form':form})
    else:
        form = UsuarioForm()
    return render(request,'novo-usuario.html',context={'form':form})

@login_required(login_url='/login/')
def editar_usuario(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST or None,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário editado com sucesso')
            return redirect(perfil_usuario)
        else:
             messages.error(request,'Não foi possível atualizar os dados do usuário')
             return render(request,'formusuario.html',context={'form':form})
    else:
        form = EditarUsuarioForm(instance=request.user)
    return render(request,'formusuario.html',context={'form':form})

@login_required(login_url='/login/')
def alterar_senha(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Senha alterada com sucesso')
            return redirect(perfil_usuario)
        else:
            messages.error(request,'Não foi possível alterar a senha')
            return render(request,'alterarsenha.html',context={'form':form}) 
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'alterarsenha.html',context={'form':form}) 


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
            return redirect('/index/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/login/')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')