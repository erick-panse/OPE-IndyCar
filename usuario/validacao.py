def somenteLetras(campo):
    if not campo:
        return False
    bloqueado = '0123456789!@#$%¨&*()_+`{}^:><|\,.;~]´[=-"'
    for i in bloqueado:
        if i in campo:
            return False
    return True

def somenteEmail(campo):
    if not campo:
        return False
    campo=campo.replace(' ','')
    bloqueado = '!#$%¨&*()+`{}^:><|\,;~]´[="'
    for i in bloqueado:
        if i in campo:
            return False
    return True

