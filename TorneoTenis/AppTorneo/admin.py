from django.contrib import admin

from  .models import *

# Register your models here.

admin.site.register(Torneo)
admin.site.register(ListaJugadores)
admin.site.register(Partidos)
admin.site.register(Torneo_Inscriptos)
admin.site.register(Avatar)

