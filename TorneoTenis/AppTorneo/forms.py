#from sre_constants import CATEGORY_UNI_SPACE
from asyncio.windows_events import NULL
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class Registro_Usuario_Formulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class Editar_Perfil_Usuario(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']


