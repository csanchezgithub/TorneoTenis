
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

def torneos(request):
      return render(request, "AppTorneo/torneo.html")

def listaJugadores(request):
      return render(request, "AppTorneo/listajugadores.html")

def partidos(request):
      return render(request, "AppTorneo/partidos.html")

def torneoJugadores(request):
      return render(request, "AppTorneo/torneojugadores.html")


#
#----------   vistas para los formularios TORNEO  ----------------------
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

def busquedaTorneo(request): 
      return render(request, "AppTorneo/busquedaTorneo.html")

def buscar(request):
      #respuesta = f"Estoy buscando el torneo nro: {request.GET['numero']}"
      if request.GET['numero']:
            numero = request.GET['numero']
            torneo_buscado = Torneo.objects.filter(numero__icontains=numero)

            return render(request, "AppTorneo/resultadoBusquedaTorneo.html", {"torneo_buscado": torneo_buscado, "numero": numero})

      else:
            respuesta = "No existen datos"


      return HttpResponse(respuesta)




#--------------------------------------------------------------------

def torneoJugadoresFormulario(request):
      return render(request, "AppTorneo/torneoJugadoresFormulario.html")

def jugadoresFormulario (request):
      return render(request, "AppTorneo/jugadoresFormulario.html")

def partidosFormulario (request):
      return render(request, "AppTorneo/partidosFormulario.html")
