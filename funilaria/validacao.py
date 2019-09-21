import datetime
def somenteLetras(campo):
    if not campo:
        return False
    bloqueado = '0123456789!@#$%¨&*()_+`{}^:><|\,.;~]´[=-"'
    for i in bloqueado:
        if i in campo:
            return False
    return True

def somenteNumeros(campo):
    if not campo:
        return False
    try:
        campo=campo.replace(' ','')
        n=int(campo)
        return True
    except:
        return False

def somenteNumerosFloat(campo):
    if not campo:
        return False
    try:
        campo=campo.replace(' ','')
        n=float(campo)
        return True
    except:
        return False

def validarTamanho(campo,tamanho):
    if not tamanho or not campo:
        return False
    return len(str(campo))==tamanho

def validarTelefone(tel):
    if not tel:
        return False
    return somenteNumeros(tel) and (len(str(tel)) in range(10,12))

def validarPlaca(placa):
    if not placa:
        return False
    bloqueado = '!@#$%¨&*()_+`{}^:><|\,.;~]´[=-" '
    for i in bloqueado:
        if i in placa:
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
    now=datetime.datetime.now().year
    return a<=int(now)+5