from django import forms
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

        if not somenteEmail(username):
            raise forms.ValidationError('nome de usuário inválido !')

        if not somenteLetras(first_name):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(last_name):
            raise forms.ValidationError('Sobrenome inválido !')

        if not somenteEmail(email):
            raise forms.ValidationError('Email inválido !')

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
