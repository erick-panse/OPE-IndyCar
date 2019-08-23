from django import forms
from funilaria.models import Cliente,Empresa

class DateInput(forms.DateInput):
    input_type='date'

class CustomerForm(forms.ModelForm):
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
    tel = forms.CharField(max_length=15,label='tel:',widget = forms.TextInput(attrs={
        'placeholder':'informe o tel',
        'name':'tel',
        'id':'tel'}))
    marca = forms.CharField(max_length=10,label='marca:',widget = forms.TextInput(attrs={
        'placeholder':'informe a marca',
        'name':'marca',
        'id':'marca'}))
    modelo = forms.CharField(max_length=20,label='modelo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o modelo',
        'name':'modelo',
        'id':'modelo'}))
    cor = forms.CharField(max_length=10,label='cor:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cor',
        'name':'cor',
        'id':'cor'}))
    placa = forms.CharField(max_length=7,label='placa:',widget = forms.TextInput(attrs={
        'placeholder':'informe a placa',
        'name':'placa',
        'id':'placa'}))
    ano = forms.CharField(max_length=4,label='ano:',widget = forms.TextInput(attrs={
        'placeholder':'informe o ano',
        'name':'ano',
        'id':'ano'}))
    cidade = forms.CharField(max_length=10,label='cidade:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cidade',
        'name':'cidade',
        'id':'cidade'}))
    estado = forms.CharField(max_length=2,label='estado:',widget = forms.TextInput(attrs={
        'placeholder':'informe o estado',
        'name':'estado',
        'id':'estado'}))

    entrada = forms.DateField(widget=DateInput)
    saida = forms.DateField(widget=DateInput)
    
    class Meta:
        abstract=True



class ClienteForm(CustomerForm):
    rg = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o rg',
        'name':'rg',
        'id':'rg'}))
    

    class Meta:
        model = Cliente
        fields=['rg','nome','endereco','bairro','email','tel','marca','modelo','cor','placa','ano','cidade','estado','entrada','saida']

class EmpresaForm(CustomerForm):
    cnpj = forms.CharField(max_length=9,label='cnpj:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cnpj',
        'name':'cnpj',
        'id':'cnpj'}))

    class Meta:
        model = Empresa
        fields=['cnpj','nome','endereco','bairro','email','tel']