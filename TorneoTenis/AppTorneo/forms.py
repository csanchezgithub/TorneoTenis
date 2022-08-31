#from sre_constants import CATEGORY_UNI_SPACE
from asyncio.windows_events import NULL
from django import forms

class torneoFormulario(forms.Form):
    numero = forms.IntegerField()
    nombre = forms.CharField()
    categoria= forms.CharField()
    detalle= forms.CharField()
    tipo= forms.CharField()
    fecha_inicio = forms.DateField()
    fecha_fin= forms.DateField()
    
class jugadoresFormulario(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    celular = forms.IntegerField()
    email = forms.EmailField()

class torneoInscriptosFormulario (forms.Form):
    numero_torneo = forms.IntegerField()
    dni_jugador = forms.IntegerField()

class partidosFormulario (forms.Form):
    numero_torneo = forms.IntegerField()
    numero_partido = forms.IntegerField()
    ronda = forms.IntegerField()
    dni_jugador_1 = forms.IntegerField()
    dni_jugador_2 = forms.IntegerField()
    fecha_partido = forms.DateField()
    jugador1_ausente = forms.BooleanField(required=False)
    jugador2_ausente = forms.BooleanField(required=False)
    jugador1_set_1 = forms.IntegerField()
    jugador2_set_1 = forms.IntegerField()
    jugador1_set_2 = forms.IntegerField()
    jugador2_set_2 = forms.IntegerField()
    jugador2_Tiebreak = forms.IntegerField(required=False)
    jugador1_Tiebreak = forms.IntegerField(required=False)
    dni_ganador = forms.IntegerField()


