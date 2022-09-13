
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppTorneo.models import Torneo, Torneo_Inscriptos, ListaJugadores, Partidos
from AppTorneo.forms import torneoFormulario, jugadoresFormulario, torneoInscriptosFormulario, partidosFormulario, Registro_Usuario_Formulario, Editar_Perfil_Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
      #a = "Hola mundo - esta es la vista de INICIO"
      #return HttpResponse (a)
      return render(request, "AppTorneo/inicio.html")


#
#----------------------------------------------------------
#----------   vistas para los TORNEOS  --------------------
#----------------------------------------------------------
@login_required
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
                  todos_los_torneos = Torneo.objects.all() #trae todos los torneos     
                  contexto= {"Los_torneos":todos_los_torneos}
                  return render(request, "AppTorneo/leerTorneos.html",contexto)

      else:
            MiFormulario = torneoFormulario()
      
      return render(request, "AppTorneo/crear_torneo_Formulario.html", {"MiFormulario": MiFormulario})


@login_required
def busquedaTorneo(request): 
      return render(request, "AppTorneo/busquedaTorneo.html")

@login_required
def buscar(request):
      #respuesta = f"Estoy buscando el torneo nro: {request.GET['numero']}"
      if request.GET['numero']:
            numero = request.GET['numero']
            torneo_buscado = Torneo.objects.filter(numero__icontains=numero)
            return render(request, "AppTorneo/busquedaTorneoResultados.html", {"torneo_buscado": torneo_buscado, "numero": numero})

      else:
            respuesta = "No existen datos"
            return HttpResponse(respuesta)


@login_required
def leerTORNEOS(request):
      todos_los_torneos = Torneo.objects.all() #trae todos los torneos     
      contexto= {"Los_torneos":todos_los_torneos}
      return render(request, "AppTorneo/leerTorneos.html",contexto)

@login_required
def eliminarTORNEO(request, numero_torneo):
      torneo = Torneo.objects.get(numero=numero_torneo)
      torneo.delete()
      # vuelvo al menú
      todos_los_torneos = Torneo.objects.all() # trae todos los torneos
      contexto = {"Los_torneos": todos_los_torneos}
      return render(request, "AppTorneo/leerTorneos.html", contexto)

@login_required
def editarTORNEO(request, numero_torneo):
    torneo = Torneo.objects.get(numero=numero_torneo)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí me llega toda la información del html
        miFormulario = torneoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación 
            informacion = miFormulario.cleaned_data

            torneo.numero = informacion['numero']
            torneo.nombre = informacion['nombre']
            torneo.categoria = informacion['categoria']
            torneo.tipo = informacion['tipo']
            torneo.fecha_inicio = informacion['fecha_inicio']
            torneo.fecha_fin = informacion['fecha_fin']
            torneo.detalle = informacion['detalle']

            torneo.save()

            # Vuelvo a mostrar los datos completos de todos los torneos
            todos_los_torneos = Torneo.objects.all()
            contexto = {"Los_torneos": todos_los_torneos}
            return render(request, "AppTorneo/leerTorneos.html", contexto)

    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = torneoFormulario(initial={'nombre': torneo.nombre, 'numero': torneo.numero,
                                          'categoria': torneo.categoria,'tipo': torneo.tipo, 'detalle': torneo.detalle,
                                          'fecha_inicio': torneo.fecha_inicio, 'fecha_fin': torneo.fecha_fin})

    # Voy al html que me permite editar
    return render(request, "AppTorneo/editarTorneo.html", {"miFormulario": miFormulario, "numero_torneo": numero_torneo})




#---------------------------------------------------------------
#------------ Vistas para la lista de jugadores general---------
#---------------------------------------------------------------
@login_required
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

                  jugadores = ListaJugadores.objects.all() # trae todos los torneos
                  contexto = {"Los_jugadores": jugadores}
                  return render(request, "AppTorneo/leerListaJugadores.html", contexto)

      else:
            MiFormulario = jugadoresFormulario()
      
      return render(request, "AppTorneo/crear_jugadores_Formulario.html", {"MiFormulario": MiFormulario})

@login_required
def leerJUGADORES(request):
      todos_los_jugadores = ListaJugadores.objects.all() #trae todos los torneos
      contexto= {"Los_jugadores":todos_los_jugadores}
      return render(request, "AppTorneo/leerListaJugadores.html",contexto)

@login_required
def eliminarJUGADOR(request, dni):
      jugador = ListaJugadores.objects.get(dni=dni)
      jugador.delete()
      # vuelvo al menú
      jugadores = ListaJugadores.objects.all() # trae todos los torneos
      contexto = {"Los_jugadores": jugadores}
      return render(request, "AppTorneo/leerListaJugadores.html", contexto)

@login_required
def editarJUGADOR(request,  dni_editado):

    jugador = ListaJugadores.objects.get(dni=dni_editado)
    
    if request.method == 'POST':
        # aquí me llega toda la información del html
        miFormulario = jugadoresFormulario(request.POST)     

        print(miFormulario)
        
        if miFormulario.is_valid:  # Si pasó la validación 
            informacion = miFormulario.cleaned_data

            jugador.dni = informacion['dni']
            jugador.nombre = informacion['nombre']
            jugador.apellido = informacion['apellido']
            jugador.fecha_nacimiento = informacion['fecha_nacimiento']
            jugador.celular = informacion['celular']
            jugador.email = informacion['email']

            jugador.save()

            # Vuelvo a mostrar los datos completos de todos los torneos
            todos_los_jugadores = ListaJugadores.objects.all()
            contexto = {"Los_jugadores": todos_los_jugadores}
            return render(request, "AppTorneo/leerListaJugadores.html", contexto)

    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = jugadoresFormulario(initial={'nombre': jugador.nombre, 'dni': jugador.dni,
                                    'apellido': jugador.apellido,'fecha_nacimiento': jugador.fecha_nacimiento, 
                                    'celular': jugador.celular, 'email': jugador.email})

    # Voy al html que me permite editar
    return render(request, "AppTorneo/editar_jugadores.html", {"miFormulario": miFormulario, "dni": dni_editado})




#----------------------------------------------------------
#------------ Vistas para los jugadores de un Torneo --------------------------------------------------------
#----------------------------------------------------------
@login_required
def TORNEOJugadoresFormulario(request):
      if request.method == 'POST':

            MiFormulario = torneoInscriptosFormulario(request.POST)
            print (MiFormulario)

            if MiFormulario.is_valid:
                  informacion = MiFormulario.cleaned_data
                  torneo_jugadores = Torneo_Inscriptos(numero_torneo= informacion["numero_torneo"], dni_jugador=informacion["dni_jugador"])
                           
                  torneo_jugadores.save()
                  todos_los_jug_torneo = Torneo_Inscriptos.objects.all() #trae todos los jugadores de los torneos     
                  contexto= {"Los_jugadoresTorneos":todos_los_jug_torneo}
                  return render(request, "AppTorneo/leerJugadoresTorneo.html",contexto)
                  
      else:
            MiFormulario = torneoInscriptosFormulario()
      
      return render(request, "AppTorneo/crear_torneoJugadores_Formulario.html", {"MiFormulario": MiFormulario})
      
@login_required
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
@login_required
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

                  todos_los_partidos = Partidos.objects.all() #trae todos los partidos     
                  contexto= {"Los_partidos":todos_los_partidos}
                  return render(request, "AppTorneo/leerPartidos.html",contexto)

      else:
            MiFormulario = partidosFormulario()
      
      return render(request, "AppTorneo/crear_partidos_Formulario.html", {"MiFormulario": MiFormulario})
 
@login_required
def leerPARTIDOS(request):
      todos_los_partidos = Partidos.objects.all() #trae todos los torneos
      contexto= {"Los_partidos":todos_los_partidos}
      return render(request, "AppTorneo/leerPartidos.html",contexto)


#----------------------------------------------------------
#------------ LOGIN   -------------------------------------
#----------------------------------------------------------

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppTorneo/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppTorneo/login.html", {"mensaje":"Datos incorrectos"})
           
        else:
            return render(request, "AppTorneo/login.html", {"mensaje":"Usuario o Contraseña erroneo"})

    form = AuthenticationForm()
    return render(request, "AppTorneo/login.html", {"form": form})


def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)              # este UserCreationForm es una funcion de django que crea el user, pero sin ningun formato
            form = Registro_Usuario_Formulario(request.POST)    # en cambio aca me cree una clase en forms.py  para poder crear el usuario con un formato mas lindo

            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppTorneo/inicio.html" ,  {"mensaje":f"Usuario Creado: {username}"})

      else:
            #form = UserCreationForm()                 # asi estaba antes con la funcion default
            form = Registro_Usuario_Formulario()       # ahora es con la que creamos en forms.py

      return render(request,"AppTorneo/login_registro.html" ,  {"form":form})


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = Editar_Perfil_Usuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppTorneo/inicio.html")

    else:

        miFormulario = Editar_Perfil_Usuario(initial={'email': usuario.email})

    return render(request, "AppTorneo/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


