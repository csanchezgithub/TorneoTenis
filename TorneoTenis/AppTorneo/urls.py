from django.urls import path
from django.contrib.auth.views import LogoutView

from AppTorneo import views


urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    
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

    path('eliminartorneo/<numero_torneo>/', views.eliminarTORNEO, name="EliminarTorneo"),
    path('eliminarjugador/<dni>/', views.eliminarJUGADOR, name="EliminarJugador"),

    path('editarTorneo/<numero_torneo>/', views.editarTORNEO, name="EditarTorneo"),
    path('editarJugador/<dni_editado>/', views.editarJUGADOR, name="EditarJugador"),

    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppTorneo/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    path('AcercaDeMI', views.acercaDeMi, name="AcercaDeMi"),
    path('Ayuda', views.ayuda, name="Ayuda"),
]