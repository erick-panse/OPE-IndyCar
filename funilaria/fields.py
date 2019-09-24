from django import forms
from .validacao import *
class DataField(forms.DateField):
    def to_python(self, value):
        if not value:
            return 
        try:
            validarData(value)
            return value
        except:
            raise ValidationError('Data de finalização inválida !')