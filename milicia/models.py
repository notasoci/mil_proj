from django.db import models
from django.utils import timezone

class Miliciano(models.Model):
    cedula = models.CharField('Cédula', max_length=10)
    apellidos = models.CharField('Apellidos', max_length=30)
    nombres = models.CharField('Nombres', max_length=30)
    rango = models.CharField('Rango', max_length=20)
    fecha_nacimiento=models.DateTimeField('Fecha de Nacimiento', default=timezone.now)
    fecha_ingreso = models.DateTimeField('Fecha de Ingreso', default=timezone.now)
    cedula_pareja = models.CharField('Cédula de pareja', max_length=10)
    apellidos_pareja = models.CharField('Apellidos de su pareja', max_length=30)
    nombres_pareja = models.CharField('Nombres de su pareja', max_length=30)
    miliciana_pareja = models.BooleanField('Pareja milician@')
    uniforme_zamorano = models.BooleanField('Uniforme Zamorano', default=False)
    uniforme_miliciano = models.BooleanField('Uniforme Kaki', default=False)
    uniforme_camuflaje = models.BooleanField('Uniforme camuflado', default=False)
    activo = models.BooleanField('Activo', default=True)
    observaciones = models.CharField('Observaciones', default='', max_length=200)
    fecha_registro = models.DateTimeField(default=timezone.now)
    registrador = models.CharField(max_length=12) #user logged in

    def __str__(self):
        return self.apellidos+', '+self.nombres

    class Meta:
        indexes = [
            models.Index(fields=['cedula'], name='cedula_idx'),
            models.Index(fields=['apellidos'], name='apellidos_idx'),
            models.Index(fields=['cedula_pareja'], name='cedula_pareja_idx'),
            models.Index(fields=['apellidos_pareja'], name='apellidos_pareja_idx'),
        ]

