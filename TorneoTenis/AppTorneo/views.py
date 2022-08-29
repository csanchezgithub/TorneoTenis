
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTorneo.models import Torneo, Torneo_Inscriptos, ListaJugadores, Partidos
#from AppTorneo.forms import TorneoFormulario, Torneo_InscriptosFormulario, ListaJugadoresFormulario, PartidosFormulario


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
