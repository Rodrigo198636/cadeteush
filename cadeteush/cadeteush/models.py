from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    domicilio = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    vehiculo = models.CharField(max_length=3, choices=[('Sí', 'Sí'), ('No', 'No')])
    disponibilidad = models.CharField(max_length=255)
    terminos_aceptados = models.BooleanField(default=False)  # Almacenamos si se aceptaron los términosycondiciones

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    nombre_solicitante = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    tramite = models.TextField()
    terminos_aceptados = models.BooleanField(default=False)
    cadete = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)  # Relaciona con un cadete
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.nombre_solicitante} para {self.cadete.nombre}"
