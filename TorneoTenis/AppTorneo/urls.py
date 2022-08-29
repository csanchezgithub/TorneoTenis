from django.urls import path

from AppTorneo import views


urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('torneos', views.torneos, name="torneos"),
    path('listajugadores', views.listaJugadores, name="listaJugadores"),
    path('torneojugadores', views.torneoJugadores, name="torneojugadores"),
    path('partidos', views.partidos, name="partidos"),

    path('torneoFormulario', views.TORNEOformulario, name="torneoFormulario"),
    path('listajugadoresFormulario', views.jugadoresFormulario, name="listaJugadoresFormulario"),
    path('torneojugadoresFormulario', views.torneoJugadoresFormulario, name="torneojugadoresFormulario"),
    path('partidosFormulario', views.partidosFormulario, name="partidosFormulario"),
    path('busquedaTorneo', views.busquedaTorneo, name="BusquedaTorneo"),
    path('buscar/', views.buscar),

]