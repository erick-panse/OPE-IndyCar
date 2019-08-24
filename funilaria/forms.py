from django import forms
from funilaria.models import Cliente,Empresa


def SomenteLetras(campo):
    return '0123456789!@#$%¨&*()_+`{}^:><|\,.;~]´[=-"' not in campo

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
    email = forms.EmailField(max_length=60,label='email:',widget = forms.EmailInput(attrs={
        'placeholder':'informe o email',
        'name':'email',
        'id':'email'}))
    telefone = forms.CharField(max_length=15,label='telefone:',widget = forms.TextInput(attrs={
        'placeholder':'informe o tel',
        'name':'tel',
        'id':'tel'}))
    marca_veiculo = forms.CharField(max_length=10,label='marca:',widget = forms.TextInput(attrs={
        'placeholder':'informe a marca',
        'name':'marca',
        'id':'marca'}))
    modelo_veiculo = forms.CharField(max_length=20,label='modelo:',widget = forms.TextInput(attrs={
        'placeholder':'informe o modelo',
        'name':'modelo',
        'id':'modelo'}))
    cor_veiculo = forms.CharField(max_length=10,label='cor:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cor',
        'name':'cor',
        'id':'cor'}))
    placa_veiculo = forms.CharField(max_length=7,label='placa:',widget = forms.TextInput(attrs={
        'placeholder':'informe a placa',
        'name':'placa',
        'id':'placa'}))
    ano_veiculo = forms.CharField(max_length=4,label='ano:',widget = forms.TextInput(attrs={
        'placeholder':'informe o ano',
        'name':'ano',
        'id':'ano'}))
    cidade_veiculo = forms.CharField(max_length=10,label='cidade:',widget = forms.TextInput(attrs={
        'placeholder':'informe a cidade',
        'name':'cidade',
        'id':'cidade'}))
    estado_veiculo = forms.CharField(max_length=2,label='estado:',widget = forms.TextInput(attrs={
        'placeholder':'informe o estado',
        'name':'estado',
        'id':'estado'}))
    
    """ def validarNome(self):
        nome = self.cleaned_data_get('nome')
        if not SomenteLetras(campo):
            raise forms.ValidationError('Nome inválido !')
        
        return nome """

    class Meta:
        abstract=True



class ClienteForm(CustomerForm):
    rg = forms.CharField(max_length=9,label='rg:',widget = forms.TextInput(attrs={
        'placeholder':'informe o rg',
        'name':'rg',
        'id':'rg'}))

    class Meta:
        model = Cliente
        fields=['rg','nome','endereco','bairro','email','telefone','marca_veiculo','modelo_veiculo','cor_veiculo','placa_veiculo','ano_veiculo','cidade_veiculo','estado_veiculo']

class EmpresaForm(CustomerForm):
    cnpj = forms.CharField(max_length=9,label='cnpj:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cnpj',
        'name':'cnpj',
        'id':'cnpj'}))

    class Meta:
        model = Empresa
        fields=['cnpj','nome','endereco','bairro','email','telefone','marca_veiculo','modelo_veiculo','cor_veiculo','placa_veiculo','ano_veiculo','cidade_veiculo','estado_veiculo']