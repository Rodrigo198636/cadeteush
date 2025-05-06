from django.shortcuts import render, redirect
from .models import Inscripcion

def home(request):
    return render(request, 'base.html')

def inscripcion(request):
    if request.method == 'POST':
        # Capturar los datos del formulario
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        domicilio = request.POST.get('domicilio')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        vehiculo = request.POST.get('vehiculo')
        disponibilidad = request.POST.get('disponibilidad')
        terminos_aceptados = 'terminos' in request.POST  # Verifica si el checkbox fue marcado

        # Crear una nueva inscripción y guardar en la base de datos
        inscripcion = Inscripcion(
            nombre=nombre,
            edad=edad,
            domicilio=domicilio,
            email=email,
            telefono=telefono,
            vehiculo=vehiculo,
            disponibilidad=disponibilidad,
            terminos_aceptados=terminos_aceptados
        )
        inscripcion.save()
  # Redirige a una página de agradecimiento después de enviar el formulario

    return render(request, 'inscripcion.html')