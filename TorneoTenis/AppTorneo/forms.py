#from sre_constants import CATEGORY_UNI_SPACE
from django import forms

class torneoFormulario(forms.Form):
    numero = forms.IntegerField()
    nombre = forms.CharField()
    categoria= forms.CharField()
    detalle= forms.CharField()
    tipo= forms.CharField()
    fecha_inicio = forms.DateField()
    fecha_fin= forms.DateField()
    
