import datetime
from .models import Cliente,Empresa
def somenteLetras(campo):
    if not campo:
        return False
    bloqueado = '0123456789!@#$%¨&*()_+`{}^:><|\,.;~]´[=-"'
    for i in bloqueado:
        if i in campo:
            return False
    return True

def somenteNumeros(campo):
    if not campo or " " in str(campo):
        return False
    try:
        campo = removerSimbolo(campo)
        n=int(campo)
        return int(campo)>=0
    except:
        return False

def somenteNumerosFloat(campo):
    if not campo:
        return False
    try:
        campo = campo.replace(',','')
        n=float(campo)
        return True
    except:
        return False

def validarTamanho(campo,tamanho):
    if not tamanho or not campo:
        return False
    campo=campo.replace(' ','')
    return len(str(campo))==tamanho

def validarTelefone(tel):
    if not tel:
        return False
    tel = removerSimbolo(tel)
    print(len(tel))
    return somenteNumeros(tel) and (len(tel) in range(10,12))

def validarPlaca(placa):
    if not placa:
        return False
    placa=placa.replace('-','')
    bloqueado = '!@#$%¨&*()_+`{}^:><|\,.;~]´[=" '
    for i in bloqueado:
        if i in placa:
            return False
    if len(placa)< 7:
        return False
    return True

def validarModelo(modelo):
    if not modelo:
        return False
    bloqueado = '!@#$%¨&*()_+`{}^:><|\,;~]´[=-"'
    for i in bloqueado:
        if i in modelo:
            return False
    return True

def validarAno(ano):
    if not ano:
        return False
    try:
        a = int(ano)
    except:
        return False
    if len(ano)< 4 or len(ano) > 4:
        return False
    now=datetime.datetime.now().year
    return a<=int(now)+5

def validarQtd(campo):
    if not campo or not somenteNumeros(campo):
        return False
    return int(campo)>=0

def validarValor(campo):
    if not campo or not somenteNumerosFloat(campo):
        return False
    return float(campo)>=0

def validarDataObrigatoria(campo):
    if campo=='' or campo==None:
        return False
    campo=datetime.datetime.strptime(str(campo), "%Y-%m-%d").date()
    return type(campo)==datetime.date

def validarData(campo):
    if campo!='' and campo!=None:
        try:
            c=datetime.datetime.strptime(str(campo), "%Y-%m-%d").date()
            return type(c)==datetime.date
        except:
            return False
    return True

def removerSimbolo(campo):
    bloqueado = '!@#$%¨&*()_+`{}^:></ |\,;.~]´[=-"'
    for i in campo:
        if i in bloqueado:
            campo=campo.replace(i,'')
    return campo

def validarCpf(campo):
    d1 = 0
    f = 11
    campo = campo[:-2]
    for i in campo:
        i = int(i)
        f -= 1
        x = i*f
        d1 += x
    d1 *= 10
    d1 %= 11    
    if d1 == 10:
        d1 = 0
    return d1

def validarCpf2(campo):
    campo=campo.replace('.','')
    campo=campo.replace('-','')
    d1=validarCpf(campo)
    d2 = 0
    f = 12
    ult= campo[-2:]
    campo = campo[:-1]
    for i in campo:
        i = int(i)
        f -= 1
        x = i*f
        d2 += x
    d2 *= 10
    d2 %= 11    
    if d2 == 10:
        d2 = 0
    x = str(d1)+str(d2)
    if x == ult:
        return True
    return False

def validarCnpj(cnpj):
    
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    cnpj = cnpj.replace( '-', '' )
    cnpj = cnpj.replace( '.', '' )
    cnpj = cnpj.replace( '/', '' )

    verificadores = cnpj[-2:]
    

    if len( cnpj ) != 14:
        return False
    soma = 0
    id = 0
    for numero in cnpj:
        try:
            lista_validacao_um[id]
        except:
            break
        soma += int( numero ) * int( lista_validacao_um[id] )
        id += 1
    soma = soma % 11
    if soma < 2:
        digito_um = 0
    else:
        digito_um = 11 - soma

    digito_um = str( digito_um ) 
    soma = 0
    id = 0
    
    for numero in cnpj:
        
        try:
            lista_validacao_dois[id]
        except:
            break
        
        soma += int( numero ) * int( lista_validacao_dois[id] )
        id += 1
    
    soma = soma % 11
    if soma < 2:
        digito_dois = 0
    else:
        digito_dois = 11 - soma
    
    digito_dois = str( digito_dois )


    return bool( verificadores == digito_um + digito_dois )


def validarUniqueCNPJ(cnpj):
    return len(Empresa.objects.filter(cnpj=cnpj))==0

def validarUniqueCPF(cpf):
    return len(Cliente.objects.filter(cpf=cpf))==0

""" def validarUniquePlaca(placa):
    return len(OrdemDeServico.objects.filter(placa_veiculo=placa))==0 """