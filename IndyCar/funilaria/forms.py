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

from django import forms
from funilaria.models import Cliente,Empresa,Veiculo

class ClienteForm(forms.ModelForm):
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
        fields={'nome','endereco','bairro','email','rg','tel'}

class EmpresaForm(forms.ModelForm):
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
    cnpj = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu rg',
        'name':'rg',
        'id':'rg'}))
    tel = forms.CharField(max_length=15,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu tel',
        'name':'tel',
        'id':'tel'}))

    class Meta:
        model = Empresa
        fields={'cnpj','nome','endereco','bairro','email','tel'}

class VeiculoForm(forms.ModelForm):
    marca = forms.CharField(max_length=10,label='Nome completo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o nome',
        'name':'nome',
        'id':'nome'}))
    modelo = forms.CharField(max_length=20,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'informe o endereço',
        'name':'endereco',
        'id':'endereco'}))
    cor = forms.CharField(max_length=10,label='bairro:',widget = forms.TextInput(attrs={
        'placeholder':'informe o bairro',
        'name':'bairro',
        'id':'bairro'}))
    placa = forms.EmailField(max_length=7,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe o seu email',
        'name':'email',
        'id':'email'}))
    ano = forms.CharField(max_length=4,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu rg',
        'name':'rg',
        'id':'rg'}))
    cidade = forms.CharField(max_length=10,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu tel',
        'name':'tel',
        'id':'tel'}))
    estado = forms.CharField(max_length=2,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o seu tel',
        'name':'tel',
        'id':'tel'}))

    entrada = forms.DateTimeField(label='tel:',widget = forms.widgets.DateTimeInput(format="%d %b %Y %H:%M:%S %Z"))
    
    finalizado = forms.DateTimeField(label='tel:',widget = forms.widgets.DateTimeInput(format="%d %b %Y %H:%M:%S %Z"))
    
    class Meta:
        model = Veiculo
        fields={'marca','modelo','cor','placa','ano','cidade','estado','entrada','finalizado'} 