from django import forms
from funilaria.models import Cliente

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(max_length=9,label='CPF:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cpf',
        'name':'cpf',
        'id':'cpf'}))
    nome = forms.CharField(max_length=60,label='Nome completo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o nome',
        'name':'nome',
        'id':'nome'}))
    endereco = forms.CharField(max_length=100,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'informe o endereço',
        'name':'endereco',
        'id':'endereco'}))
    cep = forms.CharField(max_length=8,label='CEP:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cep',
        'name':'cep',
        'id':'cep'}))
    email = forms.EmailField(max_length=60,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe o seu email',
        'name':'email',
        'id':'email'}))

    class Meta:
        model = Cliente
        fields={'cpf','nome','endereco','cep','email',}