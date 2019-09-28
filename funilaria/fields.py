from django import forms
from .validacao import *
import  datetime

class DataField(forms.DateField):
    def validar(self,campo):
        if campo!='' and campo!=None:
            try:
                c=datetime.datetime.strptime(str(campo), "%d/%m/%Y").date()
                return type(c)==datetime.date
            except:
                return False
        return True

    def clean(self,value):
        if value!='':
            if not self.validar(value):
                return 'vazio'
            return datetime.datetime.strptime(str(value), "%d/%m/%Y").date()
        return None
            
