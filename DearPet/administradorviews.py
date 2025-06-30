from django.shortcuts import render, redirect
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib
import html
import json
import boto3
from botocore.exceptions import NoCredentialsError
from .models import *
from .forms import *
from .views import *
from datetime import *
import os
import time
import subprocess
import signal
#__url="http://3.15.180.186:8080/"
__url="http://localhost:8080/"

import subprocess
import os
import sys

def reiniciar_servidor():
    # Imprimir un mensaje antes de reiniciar el servidor
    print("Reiniciando el servidor...")

    try:
        # Ejecutar el comando para iniciar un nuevo servidor en el puerto 8000
        subprocess.Popen([sys.executable, "manage.py", "runserver", "8081", "--noreload"])

        # Salir directamente del proceso actual
        os._exit(0)

    except Exception as e:
        print(f"Error al reiniciar el servidor: {e}")

if __name__ == "__main__":
    reiniciar_servidor()





def politicas_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'poli_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'politicas', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'politicas', unique_filename)

def imagenesbanner_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'imgbnn_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'imagenesbanner', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'imagenesbanner', unique_filename)

def imagenes_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'img_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'tabla_imagenes', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'tabla_imagenes', unique_filename)

def promociones_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'pro_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'promociones', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'promociones', unique_filename)

def quienes_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'quienes_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'quienes_somos', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'quienes_somos', unique_filename)

def tecnologia_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'tecnologia_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'tecnologia', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'tecnologia'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'tecnologia', unique_filename)

def productos_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
    unique_filename = f'productos_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'productos', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # Retorna la URL de la imagen
    return os.path.join(settings.STATIC_URL, 'media', 'productos', unique_filename)

def trueadministrador(request):
    if request.session['id_perfil']!=3:
        return render(request,'html/404.html')

@login_required
def politicas_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = PoliticasForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar la imagen y obtener su URL
            imagen = request.FILES.get('imagen', None)
            print(imagen, "asdasd")
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = politicas_url(imagen)
            

                # Asignar la URL de la imagen al campo 'url' del modelo
            politicas = form.save(commit=False)
            politicas.url = image_url
            politicas.fchcreacion = datetime.now()
            politicas.eliminado = 0
            politicas.save()

            return redirect('vpoliticas') 
    else:
        form = PoliticasForm()

    return render(request, 'administrador/politicas.html', {'form': form})

@login_required
def politicas_actualizar(request, politica_id):
    politica = Politicas.objects.get(id=politica_id)

    if request.method == 'POST':
        form = PoliticasForm(request.POST, instance=politica)
        if form.is_valid():
            # Procesar la imagen y obtener su URL
            imagen = request.FILES.get('imagen', None)
            if imagen:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = politicas_url(imagen)
                politica.url = image_url
                politica.fchedicion = datetime.now()
                politica.eliminado = 0
                politica.save()

                return redirect('vpoliticas') 
    else:
        form = PoliticasForm(instance=politica)

    return render(request, 'administrador/politicas.html', {'form': form})

@login_required
def politicas_eliminar(request, politica_id):
    trueadministrador(request)
    politica = Politicas.objects.get(id=politica_id)
    politica.fcheliminacion = datetime.now()
    politica.eliminado = 1
    politica.save()
    return redirect('vpoliticas')    
    

@login_required
def mostrar_politicas(request):
    trueadministrador(request)
    politicas = Politicas.objects.all()

    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(politicas, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        politicas_pagina = paginator.page(page)
    except PageNotAnInteger:
        politicas_pagina = paginator.page(1)
    except EmptyPage:
        politicas_pagina = paginator.page(paginator.num_pages)
        
    return render(request, 'administrador/vpoliticas.html', {'politicas': politicas, 'page': politicas_pagina})
#banner
@login_required
def mostrar_banner(request):
    trueadministrador(request)
    banner = Banner.objects.all()
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(banner, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        banner_pagina = paginator.page(page)
    except PageNotAnInteger:
        banner_pagina = paginator.page(1)
    except EmptyPage:
        banner_pagina = paginator.page(paginator.num_pages)
        
    return render(request, 'administrador/vbanner.html', {'banner': banner, 'banner_pagina': banner_pagina})

@login_required
def banner_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            

            banner = form.save(commit=False)
            banner.fchcreacion = datetime.now()
            banner.eliminado = 0
            banner.save()

            return redirect('mostrar_banner') 
    else:
        form = BannerForm()

    return render(request, 'administrador/banner.html', {'form': form})

@login_required
def banner_actualizar(request, banner_id):
    trueadministrador(request)
    banner = Banner.objects.get(id=banner_id)

    if request.method == 'POST':
        form = BannerForm(request.POST, instance=banner)
        if form.is_valid():

            banner.fchedicion = datetime.now()
            banner.eliminado = 0
            banner.save()

            return redirect('mostrar_banner') 
    else:
        form = BannerForm(instance=banner)

    return render(request, 'administrador/banner.html', {'form': form})
@login_required
def banner_eliminar(request, banner_id):
    trueadministrador(request)
    banner = Banner.objects.get(id=banner_id)
    banner.fcheliminacion = datetime.now()
    banner.eliminado = 1
    banner.save()
    return redirect('mostrar_banner')   

#bannerimagenes
@login_required
def mostrar_imagenesbanner(request):
    trueadministrador(request)
    imagenesbanner = ImagenesBanner.objects.all()


    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(imagenesbanner, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        banner_pagina = paginator.page(page)
    except PageNotAnInteger:
        banner_pagina = paginator.page(1)
    except EmptyPage:
        banner_pagina = paginator.page(paginator.num_pages)
        
    return render(request, 'administrador/vimagenesbanner.html', {'imagenesbanner': imagenesbanner, 'banner_pagina': banner_pagina}) 



@login_required
def imagenesbanner_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = ImagenesBannerForm(request.POST, request.FILES)
        print(form.is_valid())
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            print(imagen, "asdasd")
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenesbanner_url(imagen)
                
            
            imagenesbanner = form.save(commit=False)
            imagenesbanner.url = image_url
            imagenesbanner.fchcreacion = datetime.now()
            imagenesbanner.eliminado = 0
            imagenesbanner.save()

            return redirect('vimagenes-banner') 
    else:
        form = ImagenesBannerForm()
    return render(request, 'administrador/imagenesbanner.html', {'form': form})

@login_required
def imagenesbanner_actualizar(request, imagenes_banner_id):
    trueadministrador(request)
    imagenesbanner = ImagenesBanner.objects.get(id=imagenes_banner_id)
    
    if request.method == 'POST':
        form = ImagenesBannerForm(request.POST, instance=imagenesbanner)
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            print(imagen, "asdasd")
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenesbanner_url(imagen)
            imagenesbanner = form.save(commit=False)
            imagenesbanner.url = image_url
            imagenesbanner.fchedicion = datetime.now()
            imagenesbanner.eliminado = 0
            imagenesbanner.save()

            return redirect('vimagenes-banner') 
    else:
        form = ImagenesBannerForm(instance=imagenesbanner)

    return render(request, 'administrador/imagenesbanner.html', {'form': form})

@login_required
def imagenesbanner_eliminar(request, imagenes_banner_id):
    trueadministrador(request)
    banner = ImagenesBanner.objects.get(id=imagenes_banner_id)
    banner.fcheliminacion = datetime.now()
    banner.eliminado = 1
    banner.save()
    return redirect('vimagenes-banner')  
    
#imagenes
@login_required
def mostrar_imagenes(request):
    trueadministrador(request)
    imagenes = Imagenes.objects.all()


    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(imagenes, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        imagenes_pagina = paginator.page(page)
    except PageNotAnInteger:
        imagenes_pagina = paginator.page(1)
    except EmptyPage:
        imagenes_pagina = paginator.page(paginator.num_pages)
        
    return render(request, 'administrador/vimagenes.html', {'imagenes': imagenes, 'imagenes_pagina': imagenes_pagina}) 

@login_required
def imagenes_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = ImagenesForm(request.POST, request.FILES)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenes_url(imagen)
                
            
            imagenes = form.save(commit=False)
            imagenes.url = image_url
            imagenes.fchcreacion = datetime.now()
            imagenes.eliminado = 0
            imagenes.save()

            return redirect('vimagenes') 
    else:
        form = ImagenesForm()
    return render(request, 'administrador/imagenes.html', {'form': form})

@login_required
def imagenes_actualizar(request, imagenes_id):
    trueadministrador(request)
    imagenes = Imagenes.objects.get(id=imagenes_id)
    print(imagenes.fchcreacion)
    
    if request.method == 'POST':
        form = ImagenesForm(request.POST, instance=imagenes)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenes_url(imagen)
            imagenes = form.save(commit=False)
            imagenes.url = image_url
            imagenes.fchedicion = datetime.now()
            imagenes.eliminado = 0
            imagenes.save()
            return redirect('vimagenes') 
    else:
        form = ImagenesForm(instance=imagenes)

    return render(request, 'administrador/imagenes.html', {'form': form})

@login_required
def imagenes_eliminar(request, imagenes_id):
    trueadministrador(request)
    imagenes = Imagenes.objects.get(id=imagenes_id)
    imagenes.fcheliminacion = datetime.now()
    imagenes.eliminado = 1
    imagenes.save()
    return redirect('vimagenes')  

#preguntas
@login_required
def mostrar_preguntas(request):
    trueadministrador(request)
    preguntas = PreguntasFrecuentes.objects.all()


    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(preguntas, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        preguntas_pagina = paginator.page(page)
    except PageNotAnInteger:
        preguntas_pagina = paginator.page(1)
    except EmptyPage:
        preguntas_pagina = paginator.page(paginator.num_pages)
        
    return render(request, 'administrador/vpreguntas.html', {'preguntas': preguntas, 'preguntas_pagina': preguntas_pagina}) 


@login_required
def preguntas_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = PreguntasFrecuentesForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            imagenes = form.save(commit=False)
            imagenes.fchcreacion = datetime.now()
            imagenes.eliminado = 0
            imagenes.save()

            return redirect('vpreguntas') 
    else:
        form = PreguntasFrecuentesForm()
    return render(request, 'administrador/preguntas.html', {'form': form})

@login_required
def preguntas_actualizar(request, preguntas_id):
    trueadministrador(request)
    preguntas = PreguntasFrecuentes.objects.get(id=preguntas_id)

    
    if request.method == 'POST':
        form = PreguntasFrecuentesForm(request.POST, instance=preguntas)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenes_url(imagen)

            
            preguntas = form.save(commit=False)
            preguntas.url = image_url
            preguntas.fchedicion = datetime.now()
            preguntas.eliminado = 0
            preguntas.save()
            return redirect('vpreguntas') 
    else:
        form = PreguntasFrecuentesForm(instance=preguntas)

    return render(request, 'administrador/preguntas.html', {'form': form})

@login_required
def preguntas_eliminar(request, preguntas_id):
    trueadministrador(request)
    preguntas = PreguntasFrecuentes.objects.get(id=preguntas_id)
    preguntas.fcheliminacion = datetime.now()
    preguntas.eliminado = 1
    preguntas.save()
    return redirect('vpreguntas')  



@login_required
def mostrar_promociones(request):
    trueadministrador(request)
    promociones = Promociones.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(promociones, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        promocion_pagina = paginator.page(page)
    except PageNotAnInteger:
        promocion_pagina = paginator.page(1)
    except EmptyPage:
        promocion_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vpromociones.html', {'form': promociones, 'promociones': promocion_pagina})

@login_required
def promociones_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = PromocionesForm(request.POST, request.FILES)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = promociones_url(imagen)

            promociones = form.save(commit=False)
            promociones.url=image_url
            promociones.fchcreacion = datetime.now()
            promociones.eliminado = 0
            promociones.save()

            return redirect('vpromociones') 
    else:
        form = PreguntasFrecuentesForm()
    return render(request, 'administrador/promociones.html', {'form': form})

@login_required
def promociones_actualizar(request, promocione_id):
    trueadministrador(request)
    promociones = Promociones.objects.get(id=promocione_id)

    
    if request.method == 'POST':
        form = PromocionesForm(request.POST, instance=promociones)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = promociones_url(imagen)

            
            promociones = form.save(commit=False)

            promociones.url = image_url
            promociones.fchedicion = datetime.now()
            promociones.eliminado = 0
            promociones.save()
            return redirect('vpromociones') 
    else:
        form = PromocionesForm(instance=promociones)

    return render(request, 'administrador/promociones.html', {'form': form})

@login_required
def promociones_eliminar(request, promocione_id):
    trueadministrador(request)
    promociones = Promociones.objects.get(id=promocione_id)
    promociones.fcheliminacion = datetime.now()
    promociones.eliminado = 1
    promociones.save()
    return redirect('vpromociones')  

@login_required
def mostrar_quienesomos(request):
    trueadministrador(request)
    quienes = QuienesSomos.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(quienes, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        quienes_pagina = paginator.page(page)
    except PageNotAnInteger:
        quienes_pagina = paginator.page(1)
    except EmptyPage:
        quienes_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vquienessomos.html', {'form': quienes, 'quienes_pagina': quienes_pagina})

@login_required
def quienessomos_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = QuienesSomosForm(request.POST, request.FILES)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = quienes_url(imagen)

            quienes = form.save(commit=False)
            quienes.url=image_url
            quienes.fchcreacion = datetime.now()
            quienes.eliminado = 0
            quienes.save()

            return redirect('vquienes') 
    else:
        form = PreguntasFrecuentesForm()
    return render(request, 'administrador/quienessomos.html', {'form': form})

@login_required
def quienes_actualizar(request, quienes_id):
    trueadministrador(request)
    quienes = QuienesSomos.objects.get(id=quienes_id)

    
    if request.method == 'POST':
        form = QuienesSomosForm(request.POST, instance=quienes)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = quienes_url(imagen)

            
            quienes = form.save(commit=False)

            quienes.url = image_url
            quienes.fchedicion = datetime.now()
            quienes.eliminado = 0
            quienes.save()
            return redirect('vquienes') 
    else:
        form = QuienesSomosForm(instance=quienes)

    return render(request, 'administrador/quienessomos.html', {'form': form})


@login_required
def quienes_eliminar(request, quienes_id):
    trueadministrador(request)
    quienes = QuienesSomos.objects.get(id=quienes_id)
    quienes.fcheliminacion = datetime.now()
    quienes.eliminado = 1
    quienes.save()
    return redirect('vquienes') 

@login_required
def mostrar_ventas(request):
    trueadministrador(request)
    ventas = Ventas.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(ventas, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        ventas_pagina = paginator.page(page)
    except PageNotAnInteger:
        ventas_pagina = paginator.page(1)
    except EmptyPage:
        ventas_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vventas.html', {'form': ventas, 'ventas_pagina': ventas_pagina})

@login_required
def mostrar_detalleventa(request):
    trueadministrador(request)
    detalle = DetalleVenta.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(detalle, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        ventas_pagina = paginator.page(page)
    except PageNotAnInteger:
        ventas_pagina = paginator.page(1)
    except EmptyPage:
        ventas_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vdetalleventas.html', {'form': detalle, 'ventas_pagina': ventas_pagina})

@login_required
def mostrar_productos(request):
    trueadministrador(request)
    productos = Productos.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(productos, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        productos_pagina = paginator.page(page)
    except PageNotAnInteger:
        productos_pagina = paginator.page(1)
    except EmptyPage:
        productos_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vproductos.html', {'form': productos, 'productos_pagina': productos_pagina})

@login_required
def productos_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = ProductosForm(request.POST, request.FILES)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = productos_url(imagen)

            productos = form.save(commit=False)
            productos.fchcreacion = datetime.now()
            productos.eliminado = 0
            productos.imagen=image_url
            productos.save()

            return redirect('vproductos') 
    else:
        form = ProductosForm()
    return render(request, 'administrador/productos.html', {'form': form})

@login_required
def productos_actualizar(request, productos_id):
    trueadministrador(request)
    productos = Productos.objects.get(id_productos=productos_id)

    
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=productos)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = productos_url(imagen)
            productos.imagen=image_url    
            productos = form.save(commit=False)
            productos.fchedicion = datetime.now()
            productos.eliminado = 0
            productos.save()
            reiniciar_servidor()
            return redirect('vproductos') 
    else:
        form = ProductosForm(instance=productos)

    return render(request, 'administrador/productos.html', {'form': form})


@login_required
def productos_eliminar(request, productos_id):
    trueadministrador(request)
    productos = Productos.objects.get(id_productos=productos_id)
    productos.fcheliminacion = datetime.now()
    productos.eliminado = 1
    productos.save()
    return redirect('vproductos') 


def mandar_informacion(request):
    if request.method == "POST":
        suscriptores = Suscripciones.objects.filter(eliminado=0, habilitado=1)
        emails = [suscriptor.email for suscriptor in suscriptores]
        asunto = request.POST.get('asunto')
        message = request.POST.get('mensaje')
        if asunto and message:
            send_mail(
                asunto,
                message + ' mensaje enviado automáticamente, no responder',
                'settings.EMAIL_HOST_USER',  
                emails,  
                fail_silently=False
            )
        return render(request, 'administrador/enviar-informacion.html')
    return render(request, 'administrador/enviar-informacion.html')

def habilitar_suscripcion(request):
    if request.method == "POST":
        form = SuscripcionForm(request.POST, request.FILES)
        
        if form.is_valid():

            suscripcion = form.save(commit=False)
            suscripcion.fchcreacion = datetime.now()
            suscripcion.eliminado = 0
            suscripcion.save()

            return redirect('') 
    else:
        form = SuscripcionForm()
    return render(request, '', {'form': form})


@login_required
def mostrar_terminos(request):
    trueadministrador(request)
    terminos = TerminoCondiciones.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(terminos, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        terminos_pagina = paginator.page(page)
    except PageNotAnInteger:
        terminos_pagina = paginator.page(1)
    except EmptyPage:
        terminos_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vterminos.html', {'form': terminos, 'terminos_pagina': terminos_pagina})

@login_required
def terminos_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = TerminosForm(request.POST, request.FILES)
        
        if form.is_valid():

            termino = form.save(commit=False)
            termino.fchcreacion = datetime.now()
            termino.eliminado = 0
            termino.save()

            return redirect('vterminos') 
    else:
        form = ProductosForm()
    return render(request, 'administrador/terminos.html', {'form': form})


@login_required
def termino_actualizar(request, id):
    trueadministrador(request)
    termino = TerminoCondiciones.objects.get(id=id)

    
    if request.method == 'POST':
        form = TerminosForm(request.POST, instance=termino)
        
        if form.is_valid():
           
            termino = form.save(commit=False)
            termino.fchedicion = datetime.now()
            termino.eliminado = 0
            termino.save()
            return redirect('vterminos') 
    else:
        form = TerminosForm(instance=termino)

    return render(request, 'administrador/terminos.html', {'form': form})

@login_required
def terminos_eliminar(request, id):
    trueadministrador(request)
    terminos = TerminoCondiciones.objects.get(id=id)
    terminos.fcheliminacion = datetime.now()
    terminos.eliminado = 1
    terminos.save()
    return redirect('vterminos') 


@login_required
def mostrar_tecnologia(request):
    trueadministrador(request)
    tecnologia = NuestraTecnologia.objects.all()
    
    
    # Paginar los resultados
    page = request.GET.get('page', 1)
    paginator = Paginator(tecnologia, 10)  # 10 preguntas por página, ajusta según lo necesites
    
    try:
        tecnologia_pagina = paginator.page(page)
    except PageNotAnInteger:
        tecnologia_pagina = paginator.page(1)
    except EmptyPage:
        tecnologia_pagina = paginator.page(paginator.num_pages)
    
    
    return render(request, 'administrador/vtecnologia.html', {'form': tecnologia, 'tecnologia_pagina': tecnologia_pagina})


@login_required
def tecnologia_crear(request):
    trueadministrador(request)

    if request.method == 'POST':
        form = tecnologiasForm(request.POST, request.FILES)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = tecnologia_url(imagen)
            tecnologia = form.save(commit=False)
            tecnologia.url=image_url
            tecnologia.fchcreacion = datetime.now()
            tecnologia.eliminado = 0
            tecnologia.save()

            return redirect('vtecnologia') 
    else:
        form = tecnologiasForm()
    return render(request, 'administrador/tecnologia.html', {'form': form})

@login_required
def tecnologia_actualizar(request, id):
    trueadministrador(request)
    tecnologia = NuestraTecnologia.objects.get(id=id)
    
    if request.method == 'POST':
        form = tecnologiasForm(request.POST, instance=tecnologia)
        
        if form.is_valid():
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                # Guardar la imagen física usando la función handle_uploaded_file
                image_url = imagenes_url(imagen)
            tecnologia = form.save(commit=False)
            tecnologia.url = image_url
            tecnologia.fchedicion = datetime.now()
            tecnologia.eliminado = 0
            tecnologia.save()
            return redirect('vtecnologia') 
    else:
        form = tecnologiasForm(instance=tecnologia)

    return render(request, 'administrador/tecnologia.html', {'form': form})


@login_required
def tecnologia_eliminar(request, id):
    trueadministrador(request)
    tecnologia = NuestraTecnologia.objects.get(id=id)
    tecnologia.fcheliminacion = datetime.now()
    tecnologia.eliminado = 1
    tecnologia.save()
    return redirect('vtecnologia') 

@login_required
def usuarios_actualizar(request, id):
    trueadministrador(request)
    usuario = Usuarios.objects.get(id_usuarios=id)

    
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        
        if form.is_valid():
           
            usuario = form.save(commit=False)
            usuario.fchedicion = datetime.now()
            usuario.eliminado = 0
            usuario.save()
            return redirect('vusuarios') 
    else:
        form = UsuariosForm(instance=usuario)

    return render(request, 'administrador/usuarios.html', {'form': form})
  
@login_required
def usuarios_eliminar(request, id):
    trueadministrador(request)
    usuario = Usuarios.objects.get(id_usuarios=id)
    usuario.fcheliminacion = datetime.now()
    usuario.eliminado = 1
    usuario.save()
    return redirect('vusuarios') 


@login_required
def mascotas_crear(request):
    trueadministrador(request)
    raza=Raza.objects.filter(eliminado=0)
    usuario=Usuarios.objects.filter(eliminado=0)
    if request.method == 'POST':
        form = MascotasForm(request.POST, request.FILES)
        
        if form.is_valid():
            usuarios_id_usuarios = request.POST.get('usuarios_id_usuarios')
            print(usuarios_id_usuarios)
            descripcion = request.POST.get('raza_id_raza')
            raza = Raza.objects.get(descripcion=descripcion)
            usu = Usuarios.objects.get(id_usuarios=usuarios_id_usuarios)
            mascota = form.save(commit=False)
            mascota.fchcreacion = datetime.now()
            mascota.eliminado = 0
            mascota.raza_id_raza=raza
            mascota.usuarios_id_usuarios=usu
            mascota.save()

            return redirect('vmascotas') 
    else:
        form = MascotasForm()
    return render(request, 'administrador/mascota.html', {'form': form,'raza':raza,'usuario':usuario })

@login_required
def mascota_actualizar(request, id):
    trueadministrador(request)
    mascota = Mascotas.objects.get(id_mascotas=id)
    raza=Raza.objects.filter(eliminado=0)
    usuario=Usuarios.objects.filter(eliminado=0)
    
    if request.method == 'POST':
        form = MascotasForm(request.POST, instance=mascota)
        
        if form.is_valid():
            usuarios_id_usuarios = request.POST.get('usuarios_id_usuarios')
            descripcion = request.POST.get('raza_id_raza')
            raza = Raza.objects.get(descripcion=descripcion)
            usu = Usuarios.objects.get(id_usuarios=usuarios_id_usuarios)
            mascota = form.save(commit=False)
            mascota.fchcreacion = datetime.now()
            mascota.eliminado = 0
            mascota.raza_id_raza=raza
            mascota.usuarios_id_usuarios=usu
            mascota.save()
            return redirect('vmascotas') 
    else:
        form = MascotasForm(instance=mascota)

    return render(request, 'administrador/mascota.html', {'form': form,'raza':raza,'usuario':usuario })


@login_required
def mascota_eliminar(request, id):
    trueadministrador(request)
    mascota = Mascotas.objects.get(id_mascotas=id)
    mascota.fcheliminacion = datetime.now()
    mascota.eliminado = 1
    mascota.save()
    return redirect('vmascotas') 




















@login_required
def administrador(request):
    trueadministrador(request)
    nickname = request.session.get('nickname', None)
    return render(request,'administrador/baseadministrador.html',{'nickname': nickname})

@login_required
def vusuarios(request):
    trueadministrador(request)
    usuario = []
    nickname = request.session.get('nickname', None)
    url_usuarios = f"{__url}usuarios/todos"
    response_usuarios = requests.get(url_usuarios, headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    usuario = response_usuarios.json()
    usuarios=[]
    for usu in usuario:
        if int(usu["id_perfiles"]) ==1:
            usuarios.append({
                'id_usuario': usu['id_usuario'],
                'nombre': usu['nombre'],
                'rut': usu['rut'],
                'primer_apellido': usu['primer_apellido'],
                'fono': usu['fono'],
                'direccion': usu['direccion'],
                'email': usu['email'],
                'nombre_comuna': usu['nombre_comuna'],
                'id_perfiles': usu['id_perfiles']
            })
    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.session.get('id_perfil', None) != 3:
        return render(request, 'html/404.html')
    return render(request, "administrador/vusuarios.html", {"usuarios": usuarios, 'nickname': nickname, "users": users})

@login_required
def vveterinarios(request):
    trueadministrador(request)
    usuario = []
    nickname = request.session.get('nickname', None)
    url_usuarios = f"{__url}usuarios/todos"
    response_usuarios = requests.get(url_usuarios, headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    usuario = response_usuarios.json()
    usuarios=[]
    for usu in usuario:
        if int(usu["id_perfiles"]) ==2:
            usuarios.append({
                'id_usuario': usu['id_usuario'],
                'nombre': usu['nombre'],
                'rut': usu['rut'],
                'primer_apellido': usu['primer_apellido'],
                'fono': usu['fono'],
                'direccion': usu['direccion'],
                'email': usu['email'],
                'nombre_comuna': usu['nombre_comuna'],
                'id_perfiles': usu['id_perfiles']
            })
    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.session.get('id_perfil', None) != 3:
        return render(request, 'html/404.html')
    return render(request, "administrador/vveterinario.html", {"usuarios": usuarios, 'nickname': nickname, "users": users})

@login_required
def vmascotas(request):
    trueadministrador(request)
    mascota = []
    nickname = request.session.get('nickname', None)
    url_mascotas = f"{__url}mascotas/todos"
    response_usuarios = requests.get(url_mascotas, headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    mascota = response_usuarios.json()
    mascotas=[]
    for mas in mascota:        
        mascotas.append({
            'id': mas['id'],
            'nombre': mas['nombre'],
            'fecha_nacimiento': mas['fecha_nacimiento'],
            'descripcion': mas['descripcion'],
            'extraviada': mas['extraviada'],
            'foto': mas['foto'],
            'raza': mas['raza'],
            'tipo_mascota': mas['tipo_mascota'],
            'dueno':mas['dueno'],

        })
    page = request.GET.get('page', 1)
    paginator = Paginator(mascotas, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.session.get('id_perfil', None) != 3:
        return render(request, 'html/404.html')
    return render(request, "administrador/vmascotas.html", {"mascotas": mascotas, 'nickname': nickname, "users": users})


@login_required
def cusuarios(request):
    trueadministrador(request)
    usuario = []
    nickname = request.session.get('nickname', None)
    url_usuarios = f"{__url}usuarios/todos"
    response_usuarios = requests.get(url_usuarios, headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    usuario = response_usuarios.json()
    usuarios=[]
    for usu in usuario:
        if int(usu["id_perfiles"]) ==1:
            usuarios.append({
                'id_usuario': usu['id_usuario'],
                'nombre': usu['nombre'],
                'rut': usu['rut'],
                'primer_apellido': usu['primer_apellido'],
                'fono': usu['fono'],
                'direccion': usu['direccion'],
                'email': usu['email'],
                'nombre_comuna': usu['nombre_comuna'],
                'id_perfiles': usu['id_perfiles']
            })            

    print(usuarios)
    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.session.get('id_perfil', None) != 3:
        return render(request, 'html/404.html')
    return render(request, "administrador/cusuarios.html", {"usuarios": usuarios, 'nickname': nickname, "users": users})

@login_required
def administradorve(request):
    trueadministrador(request)
    if request.method == 'POST':
        veterinarios = request.POST.get('veterinarios')
        usuario_id = request.POST.get('usuario_id')

        datos = {
            "usuario_id": usuario_id,
            "id_perfiles": '2' if veterinarios == 'on' else '1',
        }
        print(datos)

        url_usuarios = f"{__url}usuarios/actualizar/perfil"
        response_usuarios = requests.post(
            url_usuarios,
            headers={'Authorization': 'Bearer {token}'.format(
                token=request.session['token'])},
            json=datos
        )
    usuarios = []
    nickname = request.session.get('nickname', None)
    url_usuarios = f"{__url}usuarios/todos"
    response_usuarios = requests.get(url_usuarios, headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    usuarios = response_usuarios.json()

    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.session.get('id_perfil', None) != 3:
        return render(request, 'html/404.html')
    return render(request, "administrador/administrarveterinario.html", {"usuarios": usuarios, 'nickname': nickname, "users": users})