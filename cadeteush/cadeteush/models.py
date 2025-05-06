from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    vehiculo = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    disponibilidad = models.CharField(max_length=255)
    terminos_aceptados = models.BooleanField(default=False)  # Almacenamos si se aceptaron los términos y condiciones

    def __str__(self):
        return self.nombre
