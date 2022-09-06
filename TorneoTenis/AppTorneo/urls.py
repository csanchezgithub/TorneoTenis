from django.urls import path

from AppTorneo import views


urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('torneos', views.torneos, name="torneos"),
    path('listajugadores', views.listaJugadores, name="listaJugadores"),
    path('torneojugadores', views.torneoJugadores, name="torneojugadores"),
    path('partidos', views.partidos, name="partidos"),

    path('altatorneo', views.TORNEOformulario, name="torneoFormulario"),
    path('altajugadores', views.JUGADORESformulario, name="listaJugadoresFormulario"),
    path('altajugadorestorneo', views.TORNEOJugadoresFormulario, name="torneojugadoresFormulario"),
    path('altapartidos', views.PARTIDOSFormulario, name="partidosFormulario"),
    
    path('busquedaTorneo', views.busquedaTorneo, name="BusquedaTorneo"),
    path('buscar/', views.buscar),

    path('leerTorneos', views.leerTORNEOS, name="LeerTorneos"),
    path('leerJugadores', views.leerJUGADORES, name="LeerJugadores"),
    path('leerJugadoresTorneos', views.leerJUGADORES_TORNEOS, name="LeerJugadoresTorneos"),
    path('leerPartidos', views.leerPARTIDOS, name="LeerPartidos"),

]