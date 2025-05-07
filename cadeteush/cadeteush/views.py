from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Inscripcion, Solicitud

def home(request):
    return render(request, 'base.html') 

@csrf_protect
def inscripcion(request):
    message = " "
    if request.method == 'POST':
        # Capturamos los datos del formulario
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        domicilio = request.POST.get('domicilio')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        vehiculo = request.POST.get('vehiculo')
        disponibilidad = request.POST.get('disponibilidad')
        terminos_aceptados = 'terminos' in request.POST  # Verificamos si el checkbox fue marcado

        # Creamos una nueva inscripción y la guardamos
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
        
        message = "Tu solicitud ha sido enviada con éxito. Nos pondremos en contacto contigo pronto."
    else:
            # Si no hay cadetes disponibles, mostramos un mensaje de error
        message = "No hay cadetes disponibles en este momento. Por favor, intenta más tarde."
    
    return render(request, 'base.html', {'message': message})

@csrf_protect
def solicitar_servicio(request):
    message = " "
    if request.method == 'POST':
        # Capturar los datos del formulario
        nombre_solicitante = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        tramite = request.POST.get('tramite')
        terminos_aceptados = 'terminos' in request.POST  # Verifica si el checkbox fue marcado

        # Buscar un cadete disponible
        cadete = Inscripcion.objects.filter(disponibilidad__icontains='Disponible').first()

        if cadete:
            # Crear la solicitud de servicio y asociarla al cadete
            solicitud = Solicitud(
                nombre_solicitante=nombre_solicitante,
                telefono=telefono,
                email=email,
                tramite=tramite,
                terminos_aceptados=terminos_aceptados,
                cadete=cadete
            )
            solicitud.save()

            # Agregar un mensaje de éxito
            message = "Tu solicitud ha sido enviada con éxito. Nos pondremos en contacto contigo pronto."
        else:
            # Si no hay cadetes disponibles, mostramos un mensaje de error
            message = "No hay cadetes disponibles en este momento. Por favor, intenta más tarde."

                 
    return render(request, 'base.html', {'message': message})
