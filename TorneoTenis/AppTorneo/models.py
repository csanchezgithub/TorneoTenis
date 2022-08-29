from django.db import models

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
        return f"Numero de torneo: {self.numero} - Categoria: {self.categoria} - Nombre: {self.nombre}"



class ListaJugadores(models.Model):
    dni= models.IntegerField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fecha_nacimiento= models.DateField()  
    celular=models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f"Nombre jugador: {self.nombre} {self.apellido}- DNI: {self.dni} - Fecha Nacimiento: {self.fecha_nacimiento}"



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
    jugador1_ausente=models.BooleanField()
    jugador2_ausente=models.BooleanField()
    jugador1_set_1 = models.IntegerField()   
    jugador1_set_2 = models.IntegerField()   
    jugador2_set_1 = models.IntegerField()   
    jugador2_set_2 = models.IntegerField()   
    jugador1_Tiebreak = models.IntegerField()   
    jugador2_Toebreak = models.IntegerField()   
    dni_ganador = models.IntegerField() 

    def __str__(self):
        return f"Numero Torneo: {self.numero_torneo} - Numero Partido: {self.numero_partido} - Ronda: {self.ronda} - DNI ganador:  {self.dni_ganador}"


