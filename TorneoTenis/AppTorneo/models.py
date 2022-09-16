from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Torneo(models.Model):
    numero= models.IntegerField()
    categoria= models.CharField(max_length=2)     # ej B1, B2, C...
    nombre= models.CharField(max_length=30)       # nombre que quieran dar al torneo
    tipo= models.CharField(max_length=30)         # ej juegan y se eliminan  // grupos // ...
    fecha_inicio= models.DateField()  
    fecha_fin= models.DateField()  
    detalle= models.CharField(max_length=300)     #texto libre de lo que quieran escribir

    def __str__(self):
        return f"NUMERO: {self.numero} - CATEGORIA: {self.categoria} - INICIO/FIN: {self.fecha_inicio} al {self.fecha_fin} - TIPO: {self.tipo} - NOMBRE: {self.nombre}  - DETALLE: {self.detalle}"



class ListaJugadores(models.Model):
    dni= models.IntegerField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fecha_nacimiento= models.DateField()  
    celular=models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f"Nombre jugador: {self.nombre} {self.apellido} - DNI: {self.dni} - Fecha Nacimiento: {self.fecha_nacimiento} - Celular: {self.celular} - Mail: {self.email}"



class Torneo_Inscriptos(models.Model):
    numero_torneo= models.IntegerField()   
    dni_jugador= models.IntegerField()   

    def __str__(self):
        return f"Numero Torneo: {self.numero_torneo} - DNI Jugador: {self.dni_jugador}"


class Partidos(models.Model):
    numero_torneo= models.IntegerField()   
    numero_partido= models.IntegerField()   
    ronda=models.IntegerField()   
    dni_jugador_1= models.IntegerField()   
    dni_jugador_2= models.IntegerField()   
    fecha_partido= models.DateField()  
    jugador1_ausente=models.BooleanField(null=True)
    jugador2_ausente=models.BooleanField(null=True)
    jugador1_set_1 = models.IntegerField()   
    jugador1_set_2 = models.IntegerField()   
    jugador2_set_1 = models.IntegerField()   
    jugador2_set_2 = models.IntegerField()   
    jugador1_Tiebreak = models.IntegerField(null=True)   
    jugador2_Toebreak = models.IntegerField(null=True)   
    dni_ganador = models.IntegerField() 

    def __str__(self):
        return f"Nro_Torneo: {self.numero_torneo} - Nro_Partido: {self.numero_partido} - Ronda: {self.ronda} - DNI ganador:  {self.dni_ganador} - FECHA: {self.fecha_partido} - RESULTADO: {self.jugador1_set_1}-{self.jugador2_set_1}  {self.jugador1_set_2}-{self.jugador2_set_2} Tiebreak: {self.jugador1_Tiebreak}-{self.jugador2_Toebreak} Jugador 1: {self.dni_jugador_1} Jugador 2: {self.dni_jugador_2} Ausente_Jug_1: {self.jugador1_ausente} Ausente_Jug_2: {self.jugador2_ausente}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"