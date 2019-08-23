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
        'placeholder':'informe email',
        'name':'email',
        'id':'email'}))
    rg = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe rg',
        'name':'rg',
        'id':'rg'}))
    tel = forms.CharField(max_length=15,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe tel',
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
        'placeholder':'informe o email',
        'name':'email',
        'id':'email'}))
    cnpj = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cnpj',
        'name':'cnpj',
        'id':'cnpj'}))
    tel = forms.CharField(max_length=15,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o tel',
        'name':'tel',
        'id':'tel'}))

    class Meta:
        model = Empresa
        fields={'cnpj','nome','endereco','bairro','email','tel'}

class VeiculoForm(forms.ModelForm):
    marca = forms.CharField(max_length=10,label='Nome completo:',widget = forms.TextInput(attrs={
        'placeholder':'informe a marca',
        'name':'marca',
        'id':'marca'}))
    modelo = forms.CharField(max_length=20,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'informe o modelo',
        'name':'modelo',
        'id':'modelo'}))
    cor = forms.CharField(max_length=10,label='bairro:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cor',
        'name':'cor',
        'id':'cor'}))
    placa = forms.EmailField(max_length=7,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe a placa',
        'name':'placa',
        'id':'placa'}))
    ano = forms.CharField(max_length=4,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o ano',
        'name':'ano',
        'id':'ano'}))
    cidade = forms.CharField(max_length=10,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cidade',
        'name':'cidade',
        'id':'cidade'}))
    estado = forms.CharField(max_length=2,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o estado',
        'name':'estado',
        'id':'estado'}))

    entrada = forms.DateTimeField(label='tel:',widget = forms.widgets.DateTimeInput(format="%d %b %Y %H:%M:%S %Z"))
    
    finalizado = forms.DateTimeField(label='tel:',widget = forms.widgets.DateTimeInput(format="%d %b %Y %H:%M:%S %Z"))
    
    class Meta:
        model = Veiculo
        fields={'marca','modelo','cor','placa','ano','cidade','estado','entrada','finalizado'} 