from django.shortcuts import render,redirect
from django.contrib import messages
#UserCreationForm e EditProfileForm customizados 
from .forms import UsuarioForm,EditarUsuarioForm,AlterarSenhaForm,AtribuirNovaSenhaForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
#email
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from django.template import loader
from django.contrib.auth import get_user_model
#email


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
            try:
                form.save()
                messages.success(request,'Usuário cadastrado com sucesso')
            except IntegrityError as e: 
                print('UNIQUE constraint' in str(e.args))
                if 'UNIQUE constraint' in str(e.args): 
                    messages.error(request,'Usuário já cadastrado')
                    return render(request,'novo-usuario.html',context={'form':form})
            except Exception as e:
                messages.error(request,e)
            return redirect(perfil_usuario)
        else:
            if form.non_field_errors():
                for i in form.non_field_errors():
                    messages.error(request,i)
                return render(request,'novo-usuario.html',context={'form':form})
            messages.error(request,'Senha inválida')
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
            for i in form.non_field_errors():
                messages.error(request,i)
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
    return redirect('/')

def senha(request):
    if request.POST:
        form = AlterarSenhaForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data["email"]
            usuarios = User.objects.filter(email=data)
            for user in usuarios:
                c = {
                    'email': user.email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'indycar.pythonanywhere.com',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                subject_template_name='registration/password_reset_subject.txt'
                # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                email_template_name='registration/password_reset_email.html'
                # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                subject = loader.render_to_string(subject_template_name, c)
                # Email subject *must not* contain newlines
                subject = ''.join(subject.splitlines())
                email = loader.render_to_string(email_template_name, c)
                send_mail(subject, email, 'tstmail92@gmail.com' , [user.email], fail_silently=False)
            messages.success(request, 'Um email foi enviado para ' + data +". Por favor acesse seu inbox para continuar o processo de redefinição de senha.")
            return redirect('/login/')
    else:
        form = AlterarSenhaForm()
    return render(request,'alterarsenha.html',context={'form':form})

def atribuir_nova_senha(request,uidb64=None, token=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    if request.POST:
        UserModel = get_user_model()
        form = AtribuirNovaSenhaForm(request.POST)
        assert uidb64 is not None and token is not None  # verificação feita pelo URLconf pra ver se o link e token são válidos
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password= form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Senha alterada com sucesso')
                return render(request,'nova-senha.html',context={'form':form}) 
            else:
                messages.error(request, 'Não foi possível alterar a senha.')
                return render(request,'nova-senha.html',context={'form':form}) 
        else:
            messages.error(request,'Este link não é mais válido')
            return redirect('/login/')
    else:
        form = AtribuirNovaSenhaForm()
        return render(request,'nova-senha.html',context={'form':form}) 