
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTorneo.models import Torneo, Torneo_Inscriptos, ListaJugadores, Partidos
from AppTorneo.forms import torneoFormulario


# Create your views here.

def inicio(request):
      #a = "Hola mundo - esta es la vista de INICIO"
      #return HttpResponse (a)
      return render(request, "AppTorneo/inicio.html")

def listaJugadores(request):
     # a = "Hola mundo - esta es la vista de los JUGADORES"
#      return HttpResponse (a)
      return render(request, "AppTorneo/listajugadores.html")

def partidos(request):
     # a = "Hola mundo - esta es la vista de los Partidos"
#      return HttpResponse (a)
      return render(request, "AppTorneo/partidos.html")

def torneos(request):
      #a = "Hola mundo - esta es la vista de los Torneos"
#      return HttpResponse (a)
      return render(request, "AppTorneo/torneo.html")

def torneoJugadores(request):
      #a = "Hola mundo - esta es la vista de los Jugadores anotados en un torneo"
#      return HttpResponse (a)
      return render(request, "AppTorneo/torneojugadores.html")

#
#   vistas para los formularios
#
def TORNEOformulario(request):
      if request.method == 'POST':

            MiFormulario = torneoFormulario(request.POST)
            print (MiFormulario)

            if MiFormulario.is_valid:
                  informacion = MiFormulario.cleaned_data
                  torneo = Torneo(numero=informacion["numero"], nombre= informacion["nombre"], 
                           categoria=informacion["categoria"], detalle=informacion["detalle"],
                           fecha_inicio = informacion["fecha_inicio"], fecha_fin=informacion["fecha_fin"],
                           tipo=informacion["tipo"])
                  torneo.save()
                  return render(request, "AppTorneo/inicio.html")
      else:
            MiFormulario = torneoFormulario()
      
      return render(request, "AppTorneo/torneoFormulario.html", {"MiFormulario": MiFormulario})


def torneoJugadoresFormulario(request):
      return render(request, "AppTorneo/torneoJugadoresFormulario.html")

def jugadoresFormulario (request):
      return render(request, "AppTorneo/jugadoresFormulario.html")

def partidosFormulario (request):
      return render(request, "AppTorneo/partidosFormulario.html")
