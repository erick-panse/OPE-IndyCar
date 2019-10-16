from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from .validacao import*

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        dados=self.cleaned_data
        username=dados.get('username')
        first_name=dados.get('first_name')
        last_name=dados.get('last_name')
        email=dados.get('email')
        password1=dados.get('password1')
        password2=dados.get('password2')

        if not somenteEmail(username):
            raise forms.ValidationError('nome de usuário inválido !')

        if not somenteLetras(first_name):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(last_name):
            raise forms.ValidationError('Sobrenome inválido !')

        if not somenteEmail(email):
            raise forms.ValidationError('Email inválido !')
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class EditarUsuarioForm(UserChangeForm):
    password=None

    def clean(self):
        dados=self.cleaned_data
        first_name=dados.get('first_name')
        last_name=dados.get('last_name')
        email=dados.get('email')

        if not somenteLetras(first_name):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(last_name):
            raise forms.ValidationError('Sobrenome inválido !')

        if not somenteEmail(email):
            raise forms.ValidationError('Email inválido !')

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class AlterarSenhaForm(forms.Form):
    email = forms.EmailField(label=("Email"), max_length=254,required=True)

class AtribuirNovaSenhaForm(forms.Form):
    error_messages = {
        'password_mismatch': ("Senhas não coincidem"),
        }
    new_password1 = forms.CharField(label=("Nova senha"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("Confirmação da nova senha"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        password_validation.validate_password(password2)
        return password2
