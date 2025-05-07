# cadeteush/admin.py
from django.contrib import admin
from .models import Inscripcion, Solicitud

admin.site.register(Inscripcion)
admin.site.register(Solicitud)  
