from django import forms
from funilaria.models import Cliente

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(max_length=9,label='CPF:',widget = forms.TextInput(attrs={
        'placeholder':'informe o cpf',
        'name':'cpf',
        'id':'cpf'}))
    nome = forms.CharField(max_length=60,label='Nome completo:')
    endereco = forms.CharField(max_length=100,label='Endereço:')
    cep = forms.CharField(max_length=8,label='CEP:')
    email = forms.EmailField(max_length=60,label='Email:')

    class Meta:
        model = Cliente
        fields={'cpf'}