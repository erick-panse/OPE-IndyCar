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
    bairro = forms.CharField(max_length=8,label='bairro:',widget = forms.TextInput(attrs={
        'placeholder':'informe o bairro',
        'name':'bairro',
        'id':'bairro'}))
    email = forms.EmailField(max_length=60,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe o seu email',
        'name':'email',
        'id':'email'}))
    rg = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu rg',
        'name':'rg',
        'id':'rg'}))
    tel = forms.CharField(max_length=15,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu tel',
        'name':'tel',
        'id':'tel'}))

    class Meta:
        model = Cliente
        fields={'cpf','nome','endereco','bairro','email','rg','tel'}