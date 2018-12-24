from django.db import models
from django.utils import timezone

class Miliciano(models.Model):
    cedula = models.IntegerField('Cédula: ')
    apellidos = models.CharField('Apellidos: ', max_length=30)
    nombres = models.CharField('Nombres: ', max_length=30)
    rango = models.CharField('Rango: ', max_length=20)
    fecha_nacimiento=models.DateTimeField('Fecha de Nacimiento: ', default=timezone.now)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso: ', default=timezone.now)
    cedula_pareja = models.IntegerField('Cédula de pareja: ')
    apellidos_pareja = models.CharField('Apellidos de su pareja: ', max_length=30)
    nombres_pareja = models.CharField('Nombres de su pareja: ', max_length=30)
    miliciana_pareja = models.BooleanField('Pareja milician@: ')
    uniforme_zamorano = models.BooleanField('Uniforme Zamorano: ', default=False)
    uniforme_miliciano = models.BooleanField('Uniforme Kaki: ', default=False)
    uniforme_camuflaje = models.BooleanField('Uniforme camuflado: ', default=False)
    activo = models.BooleanField('Activo: ', default=True)
    observaciones = models.CharField('Observaciones: ', max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)
    registrador = models.CharField(max_length=12) #user logged in

    class Meta:
        indexes = [
            models.Index(fields=['cedula', 'apellidos', 'cedula_pareja', 'apellidos_pareja']),
            models.Index(fields=['cedula'], name='cedula_idx'),
            models.Index(fields=['apellidos'], name='apellidos_idx'),
            models.Index(fields=['cedula_pareja'], name='cedula_pareja_idx'),
        ]


class Asistencia(models.Model):
    id2 = models.ForeignKey(Miliciano, on_delete=models.CASCADE)
    fecha_actividad = models.DateTimeField('Fecha de la Actividad')
    actividad = models.CharField('Nombre de la Actividad', max_length=200, default='Concentración Semanal')
    fecha_actividad = models.DateTimeField('Fecha de la Actividad', default=timezone.now)
    fecha_registro = models.DateTimeField(default=timezone.now)
    registrador = models.CharField(max_length=12)
