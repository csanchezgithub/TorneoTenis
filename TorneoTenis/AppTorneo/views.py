
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTorneo.models import Torneo, Torneo_Inscriptos, ListaJugadores, Partidos
from AppTorneo.forms import torneoFormulario, jugadoresFormulario, torneoInscriptosFormulario, partidosFormulario


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
#----------------------------------------------------------
#----------   vistas para los TORNEOS  --------------------
#----------------------------------------------------------
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
      
      return render(request, "AppTorneo/crear_torneo_Formulario.html", {"MiFormulario": MiFormulario})

def busquedaTorneo(request): 
      return render(request, "AppTorneo/busquedaTorneo.html")

def buscar(request):
      #respuesta = f"Estoy buscando el torneo nro: {request.GET['numero']}"
      if request.GET['numero']:
            numero = request.GET['numero']
            torneo_buscado = Torneo.objects.filter(numero__icontains=numero)
            return render(request, "AppTorneo/busquedaTorneoResultados.html", {"torneo_buscado": torneo_buscado, "numero": numero})

      else:
            respuesta = "No existen datos"
            return HttpResponse(respuesta)


def leerTORNEOS(request):
      todos_los_torneos = Torneo.objects.all() #trae todos los torneos     
      contexto= {"Los_torneos":todos_los_torneos}
      return render(request, "AppTorneo/leerTorneos.html",contexto)


#----------------------------------------------------------
#------------ Vistas para la lista de jugadores posibles  ---------------------------------------------------
#----------------------------------------------------------
def JUGADORESformulario (request):
      if request.method == 'POST':

            MiFormulario = jugadoresFormulario(request.POST)
            print (MiFormulario)

            if MiFormulario.is_valid:
                  informacion = MiFormulario.cleaned_data
                  jugadores = ListaJugadores(dni=informacion["dni"], nombre= informacion["nombre"], 
                           apellido=informacion["apellido"], fecha_nacimiento= informacion["fecha_nacimiento"],
                           celular = informacion["celular"], email= informacion["email"])
                  jugadores.save()
                  return render(request, "AppTorneo/inicio.html")
      else:
            MiFormulario = jugadoresFormulario()
      
      return render(request, "AppTorneo/crear_jugadores_Formulario.html", {"MiFormulario": MiFormulario})


def leerJUGADORES(request):
      todos_los_jugadores = ListaJugadores.objects.all() #trae todos los torneos
      contexto= {"Los_jugadores":todos_los_jugadores}
      return render(request, "AppTorneo/leerListaJugadores.html",contexto)


#----------------------------------------------------------
#------------ Vistas para los jugadores de un Torneo --------------------------------------------------------
#----------------------------------------------------------
def TORNEOJugadoresFormulario(request):
      if request.method == 'POST':

            MiFormulario = torneoInscriptosFormulario(request.POST)
            print (MiFormulario)

            if MiFormulario.is_valid:
                  informacion = MiFormulario.cleaned_data
                  torneo_jugadores = Torneo_Inscriptos(numero_torneo= informacion["numero_torneo"], dni_jugador=informacion["dni_jugador"])
                           
                  torneo_jugadores.save()
                  return render(request, "AppTorneo/inicio.html")
      else:
            MiFormulario = torneoInscriptosFormulario()
      
      return render(request, "AppTorneo/crear_torneoJugadores_Formulario.html", {"MiFormulario": MiFormulario})
      

def leerJUGADORES_TORNEOS(request):
#      numero_torneo = request.GET['numero']
#      torneo_buscado = Torneo_Inscriptos.objects.filter(numero_torneo__icontains=numero_torneo)
#      return render(request, "AppTorneo/leerJugadoresTorneo2.html", {"torneo_buscado": torneo_buscado, "numero": numero_torneo})
      jugadores_de_torneos = Torneo_Inscriptos.objects.all() #trae todos los torneos
      contexto= {"Los_jugadoresTorneos":jugadores_de_torneos}
      return render(request, "AppTorneo/leerJugadoresTorneo.html",contexto)


#----------------------------------------------------------
#------------ Vistas para Partidos --------------------------------------------------------
#----------------------------------------------------------
def PARTIDOSFormulario (request):
      if request.method == 'POST':

            MiFormulario = partidosFormulario(request.POST)
            print (MiFormulario)

            if MiFormulario.is_valid:
                  informacion = MiFormulario.cleaned_data
                  partidos = Partidos(numero_torneo= informacion["numero_torneo"], numero_partido=informacion["numero_partido"],
                       ronda = informacion["ronda"], dni_jugador_1 = informacion["dni_jugador_1"], 
                       dni_jugador_2 = informacion["dni_jugador_2"], fecha_partido= informacion["fecha_partido"],
                       jugador1_ausente = informacion["jugador1_ausente"], jugador2_ausente = informacion["jugador2_ausente"],
                       jugador1_set_1 = informacion["jugador1_set_1"],
                       jugador2_set_1 = informacion["jugador2_set_1"],
                       jugador1_set_2 = informacion["jugador1_set_2"],
                       jugador2_set_2 = informacion["jugador2_set_2"],
                       jugador1_Tiebreak = informacion["jugador1_Tiebreak"],
                       jugador2_Toebreak = informacion["jugador2_Tiebreak"],
                       dni_ganador = informacion["dni_ganador"] )
                           
                  partidos.save()
                  
                  return render(request, "AppTorneo/inicio.html")

      else:
            MiFormulario = partidosFormulario()
      
      return render(request, "AppTorneo/crear_partidos_Formulario.html", {"MiFormulario": MiFormulario})
 

def leerPARTIDOS(request):
      todos_los_partidos = Partidos.objects.all() #trae todos los torneos
      contexto= {"Los_partidos":todos_los_partidos}
      return render(request, "AppTorneo/leerPartidos.html",contexto)
