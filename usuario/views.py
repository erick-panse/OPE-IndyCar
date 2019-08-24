from django.shortcuts import render,redirect
from django.contrib import messages
#UserCreationForm e EditProfileForm customizados 
from .forms import UsuarioForm,EditarUsuarioForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def perfil_usuario(request):
    msg=messages.get_messages(request)
    return render(request,'perfil.html',context={'user':request.user,'msg':msg})


def novo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário cadastrado com sucesso !')
        else:
             messages.error(request,'Form inválido!')
        return redirect('/cliente/')
    else:
        form = UsuarioForm()
    return render(request,'novo-usuario.html',context={'form':form})

@login_required(login_url='/login/')
def editar_usuario(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST or None,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Usuário editado com sucesso !')
        else:
             messages.error(request,'Form inválido!')
        return redirect(perfil_usuario)
    else:
        form = EditarUsuarioForm(instance=request.user)
    return render(request,'formusuario.html',context={'form':form})

@login_required(login_url='/login/')
def alterar_senha(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user,)
            messages.success(request,'Senha alterada com sucesso !')
        else:
            messages.error(request,'Erro ao alterar')
        return redirect(perfil_usuario)
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
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/login/')

def logout_user(request):
    logout(request)
    return redirect('/login/')