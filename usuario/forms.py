from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class EditarUsuarioForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
