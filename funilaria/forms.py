from django import forms
from funilaria.models import Cliente,Empresa,Orcamento,OrdemDeServico,Customer,Material
import localflavor.br.forms
from funilaria.views import *
from .widgets import FengyuanChenDatePickerInput
from .validacao import *

ESTADO_CARRO= [
    ('AC', 'Acre'),    
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ('ET', 'Estrangeiro'),]
    
class CustomerForm(forms.ModelForm):
    nome = forms.CharField(max_length=60,label='Nome completo:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o nome',
        'name':'nome',
        'id':'nome'}))
    endereco = forms.CharField(max_length=100,label='Endereço:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o endereço',
        'name':'endereco',
        'id':'endereco'}))
    bairro = forms.CharField(max_length=30,label='Bairro:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o bairro',
        'name':'bairro',
        'id':'bairro'}))
    email = forms.EmailField(max_length=60,label='Email:',widget = forms.EmailInput(attrs={
        'placeholder':'Informe o email',
        'name':'email',
        'id':'email'}))
    telefone = forms.CharField(max_length=11,label='Telefone:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o telefone',
        'name':'tel',
        'id':'tel'}))

    def validar(self):
        dados=self.cleaned_data
        nome=dados.get('nome')
        endereco=dados.get('endereco')
        bairro=dados.get('bairro')
        email=dados.get('email')
        telefone=dados.get('telefone')
        

        if not somenteLetras(nome):
            raise forms.ValidationError('Nome inválido !')

        if not somenteLetras(bairro):
            raise forms.ValidationError('Bairro inválido !')

        if not validarTelefone(telefone):
            raise forms.ValidationError('Telefone inválido !')

    class Meta:
        abstract=True



class ClienteForm(CustomerForm):
    cpf = localflavor.br.forms.CharField(max_length=11, min_length=11,label='CPF:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o CPF',
        'name':'cpf',
        'id':'cpf'}))


    def clean(self):
        dados = self.cleaned_data
        cpf=dados.get('cpf')
        if not somenteNumeros(cpf) or not validarTamanho(cpf,11):
            raise forms.ValidationError('CPF inválido !')
        self.validar()

    class Meta:
        model = Cliente
        fields=['cpf','nome','endereco','bairro','email','telefone']

class EmpresaForm(CustomerForm):
    cnpj = localflavor.br.forms.CharField(min_length=14, max_length=14,label='CNPJ:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o CNPJ',
        'name':'cnpj',
        'id':'cnpj'}))

    def clean(self):
        dados = self.cleaned_data
        cnpj=dados.get('cnpj')
        if not somenteNumeros(cnpj) or not validarTamanho(cnpj,14):
            raise forms.ValidationError('CNPJ inválido !')
        self.validar()

    class Meta:
        model = Empresa
        fields=['cnpj','nome','endereco','bairro','email','telefone']

""" class OrcamentoForm(forms.ModelForm):
    quantidade_pecas = forms.CharField(label='Quantidade de peças:',widget = forms.NumberInput(attrs={
        'placeholder':'Informe a quantidade de peças',
        'name':'quantidade_pecas',
        'id':'quantidade_pecas'}))
    servicos = forms.CharField(max_length=500,label='Serviços:',widget = forms.Textarea(attrs={
        'placeholder':'Informe os serviços necessários',
        'name':'servicos',
        'id':'servicos'}))
    pecas = forms.ModelChoiceField(queryset=Material.objects.all())
    
    valor_mao_de_obra = forms.FloatField(label='valor da mão de obra:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o valor da mão de obra',
        'name':'valor_mao_de_obra',
        'id':'valor_mao_de_obra'}))

    total_a_pagar = forms.DecimalField(label='Total a pagar:',widget = forms.TextInput(attrs={
        'readonly':'Total a pagar',
        'name':'total_a_pagar',
        'id':'total_a_pagar'}))
    
    previsao_entrega = forms.DateField(label='Previsão entrega:',widget = forms.DateInput(attrs={
        'placeholder':'Informe a previsão entrega',
        'name':'previsao_entrega',
        'id':'previsao_entrega'}))
    data_saida = forms.DateField(label='Data saída:',widget = forms.DateInput(attrs={
        'placeholder':'Informe a data de saida',
        'name':'data_saida',
        'id':'data_saida'}))
    
    def clean(self):
        dados=self.cleaned_data
        quantidade_pecas=dados.get('quantidade_pecas')
        servicos=dados.get('servicos')
        pecas=dados.get('pecas')
        valor_mao_de_obra=dados.get('valor_mao_de_obra')
        total_a_pagar=dados.get('total_a_pagar')
        previsao_entrega=dados.get('previsao_entrega')
        data_saida=dados.get('data_saida')

        if not somenteNumeros(quantidade_pecas):
            raise forms.ValidationError('Quantidade de peças inválida !')

        if not somenteLetras(servicos):
            raise forms.ValidationError('Serviços inválidos !')
        
        if not somenteLetras(pecas):
            raise forms.ValidationError('Peças inválidas !')

        if not somenteNumeros(valor_mao_de_obra):
            raise forms.ValidationError('Valor mão de obra inválido !')

        if not somenteNumeros(total_a_pagar):
            raise forms.ValidationError('Total a pagar inválido !')
        
    
    class Meta:
        model = Orcamento
        fields=['pecas','quantidade_pecas','servicos','valor_mao_de_obra','previsao_entrega','data_saida','total_a_pagar'] """

class OrdemDeServicoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(queryset=Customer.objects.all().select_subclasses().order_by('id'))
    marca_veiculo = forms.CharField(max_length=10,label='Marca:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a marca',
        'name':'marca',
        'id':'marca'}))
    modelo_veiculo = forms.CharField(max_length=20,label='Modelo:',widget = forms.TextInput(attrs={
        'placeholder':'Informe o modelo',
        'name':'modelo',
        'id':'modelo'}))
    cor_veiculo = forms.CharField(max_length=10,label='Cor:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a cor',
        'name':'cor',
        'id':'cor'}))
    placa_veiculo = forms.CharField(max_length=7,label='Placa:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a placa',
        'name':'placa',
        'id':'placa'}))
    ano_veiculo = forms.CharField(max_length=4,label='Ano:',widget = forms.NumberInput(attrs={
        'placeholder':'Informe o ano',
        'name':'ano',
        'id':'ano'}))
    estado_veiculo= forms.CharField(label='Estado', widget=forms.Select(choices=ESTADO_CARRO))
    cidade_veiculo = forms.CharField(max_length=10,label='Cidade:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a cidade',
        'name':'cidade',
        'id':'cidade'}))
    reparos_necessarios = forms.CharField(max_length=500,label='Reparos necessários:',widget = forms.Textarea(attrs={
        'placeholder':'Informe os reparos necessários',
        'name':'reparos_necessarios',
        'id':'reparos_necessarios'}))
    prazo_entrega = forms.DateField(label='Prazo entrega:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Prazo de entrega',
        'name':'prazo_entrega',
        'id':'prazo_entrega'}))
    data_finalizacao = forms.DateField(required=False,label='Data de finalização:',input_formats=['%d/%m/%Y'],widget = FengyuanChenDatePickerInput(attrs={
        'placeholder':'Data de finalização',
        'name':'data_finalizacao',
        'id':'data_finalizacao'}))
    
    def clean(self):
        dados=self.cleaned_data
        reparos_necessarios=dados.get('reparos_necessarios')
        entrada=dados.get('entrada')
        data_finalizacao=dados.get('data_finalizacao')
        prazo_entrega=dados.get('prazo_entrega')
        finalizado=dados.get('finalizado')
        marca_veiculo=dados.get('marca_veiculo')
        modelo_veiculo=dados.get('modelo_veiculo')
        cor_veiculo=dados.get('cor_veiculo')
        placa_veiculo=dados.get('placa_veiculo')
        ano_veiculo=dados.get('ano_veiculo')
        cidade_veiculo=dados.get('cidade_veiculo')
        estado_veiculo=dados.get('estado_veiculo')

        if not somenteLetras(reparos_necessarios):
            raise forms.ValidationError('Reparos necessários inválidos !')

        if not somenteLetras(marca_veiculo):
            raise forms.ValidationError('Marca inválida !')

        if not validarModelo(modelo_veiculo):
            raise forms.ValidationError('Modelo inválido !')

        if not somenteLetras(cor_veiculo):
            raise forms.ValidationError('Cor inválida !')

        if not validarPlaca(placa_veiculo):
            raise forms.ValidationError('Placa inválida !')

        if not validarAno(ano_veiculo):
            raise forms.ValidationError('Ano inválido !')

        if not somenteLetras(cidade_veiculo):
            raise forms.ValidationError('Cidade inválida !')

        if not somenteLetras(estado_veiculo):
            raise forms.ValidationError('Estado inválido !')

        if not validarDataObrigatoria(prazo_entrega):
            raise forms.ValidationError('Prazo inválido !')

        if not validarData(data_finalizacao):
            raise forms.ValidationError('Data de finalização inválida !')

    class Meta:
        model = OrdemDeServico
        fields=['cliente','marca_veiculo','modelo_veiculo','cor_veiculo','placa_veiculo','ano_veiculo','cidade_veiculo','estado_veiculo','reparos_necessarios','prazo_entrega','data_finalizacao']

class MaterialForm(forms.ModelForm):
    quantidade_estoque = forms.CharField(max_length=6,label='Quantidade em estoque:',widget = forms.NumberInput(attrs={
        'placeholder':'Informe a quantidade em estoque',
        'name':'quantidade_estoque',
        'id':'quantidade_estoque'}))
    descricao = forms.CharField(max_length=200,label='Descrição:',widget = forms.TextInput(attrs={
        'placeholder':'Informe a descrição',
        'name':'descricao',
        'id':'descricao'}))
    
    valor = forms.CharField(max_length=10,label='Valor:',widget = forms.NumberInput(attrs={
        'placeholder':'Valor da peça',
        'name':'valor',
        'id':'valor'}))
    
    def clean(self):
        dados=self.cleaned_data
        quantidade_estoque=dados.get('quantidade_estoque')
        descricao=dados.get('descricao')
        valor=dados.get('valor')

        if not somenteLetras(descricao):
            raise forms.ValidationError('Descricao inválida !')

        if not validarValor(valor):
            raise forms.ValidationError('Valor inválido !')

        if not validarQtd(quantidade_estoque):
            raise forms.ValidationError('Quantidade inválida !')
        
    
    class Meta:
        model = Material
        fields=['quantidade_estoque','descricao','valor']
