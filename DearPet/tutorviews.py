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
from django.http import JsonResponse
from .models import *
from .forms import *
from datetime import datetime
from . import views
import os

# __url="http://3.15.180.186:8080/"
__url = "http://localhost:8080/"

def mascota_url(f):
    # Obtiene el nombre del archivo y su extensión
    file_name, file_extension = os.path.splitext(f.name)

    # Genera un nombre único basado en la estructura indicada
    current_datetime = datetime.now().strftime('%Y%m%d%H%M')
    unique_filename = f'mascota_{file_name}_{current_datetime}{file_extension}'

    # Define la ruta donde se almacenará la imagen
    upload_path = os.path.join(settings.STATIC_ROOT, 'media', 'mascota', unique_filename)

    # Si no existe, crea el directorio para almacenar la imagen
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    # Guarda la imagen en la carpeta 'politicas'
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    url = os.path.join(settings.STATIC_URL, 'media', 'mascota', unique_filename)
    # Retorna la URL de la imagen
    return url


def perfil(request):
    nickname=request.session['nickname']
    id= request.session['id_usuario']
    usuario =Usuarios.objects.get(id_usuarios=id)

    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():

            usuario.fchedicion = datetime.now()
            usuario.eliminado = 0
            request.session['nickname'] = usuario.nombre
            usuario.save()
            

            return redirect('perfil') 
    return render(request, 'tutor/mi_perfil.html',{'nickname':nickname,'usuario':usuario})

def actualizar_perfil(request):
    nickname=request.session['nickname']
    id= request.session['id_usuario']
    usuario =Usuarios.objects.get(id_usuarios=id)

    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():

            usuario.fchedicion = datetime.now()
            usuario.eliminado = 0
            request.session['nickname'] = usuario.nombre
            usuario.save()
            

            return redirect('perfil') 
    else:
        form = UsuariosForm(instance=usuario)

    return render(request, 'tutor/actualizar_perfil.html', {'form': form,'nickname':nickname})

def actualizar_contrasena(request):
    nickname=request.session['nickname']
    id= request.session['id_usuario']
    usuario =Usuarios.objects.get(id_usuarios=id)

    if request.method == 'POST':
        form = UsuariosContrasenaForm(request.POST, instance=usuario)
        if form.is_valid():
            contrasena = request.POST.get('contrasena')
            contrasena1 = request.POST.get('contrasena1')
            if contrasena ==contrasena1:
                encriptada= views.sha256(contrasena)
            else:
                return redirect('actualizar_contrasena')    
            usuario.contrasena=encriptada
            usuario.fchedicion = datetime.now()
            usuario.eliminado = 0
            usuario.save()

            return redirect('logout') 
    else:
        form = UsuariosContrasenaForm(instance=usuario)

    return render(request, 'tutor/actualizar_contrasena.html', {'form': form,'nickname':nickname})

#mascota CRUD

def mostrar_mascotas(request):
    nickname=request.session['nickname']
    id= request.session['id_usuario']
    mascotas = Mascotas.objects.filter(eliminado=0, usuarios_id_usuarios=id).select_related('raza_id_raza__tipo_mascota_id_tipo_mascota')

    return render(request,'tutor/mis_mascotas.html',{'nickname':nickname,'mascotas':mascotas})

def mascotas_crear(request):
    tipo = TipoMascota.objects.filter(eliminado=0)
    id_usuario = request.session['id_usuario']
    nickname = request.session['nickname']
    token = request.session.get('token', '')
    rutas = request.POST.get('PetPhoto', '')
    id_externo = request.GET.get('id_externo')
    id_mascotas = request.GET.get('id_mascotas', None)
    mascota = None
    id_tipo_mascota = None
    if id_mascotas:
            mascota = Mascotas.objects.filter(id_mascotas=id_mascotas, eliminado=0).first()
            id_tipo_mascota = mascota.raza_id_raza.tipo_mascota_id_tipo_mascota

            print('idtipo', id_tipo_mascota)

    if request.method == 'POST':
        id_mascota_post = request.POST.get('id_mascota', None)
        payload = {
            'id': id_mascota_post,
            'nombre': request.POST.get('PetName'),
            'id_usuarios': id_usuario,  # ✅ usás el de sesión
            'fecha_nacimiento': request.POST.get('BirthDate'),
            'descripcion': request.POST.get('descripcion'),
            'genero': request.POST.get('genero'),
            'extraviada': request.POST.get('extraviada', 0),
            'foto': rutas ,  # manejar archivos luego
            'id_raza': request.POST.get('raza_id_raza'),
            'id_externo': request.POST.get('id_externo'),
            'vacunada': request.POST.get('vacunada', 0),
            'esterilizada': request.POST.get('sterilization', 0),
            'alergias': request.POST.get('alergia', 0),
            'origen': 0,
        }

        print("Payload:", payload)  # para debug

        try:
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            if id_mascota_post:
                url = f"{__url}/mascotas/actualizar"
            else:
                url = f"{__url}/mascotas/crear"

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                return redirect('mascotas')
            else:
                return JsonResponse({'error': 'Error al crear mascota', 'detalle': response.text}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Excepción en la solicitud', 'detalle': str(e)}, status=500)

    return render(request, 'tutor/crear_mascotas.html', {
        'nickname': nickname,
        'tipo': tipo,
        'token': token,
        'id_externo': id_externo,
        'mascota': mascota,
        'id_tipo_mascota': id_tipo_mascota
    })

def actualizar_mascota(request):
    nickname=request.session['nickname']
    raza=Raza.objects.filter(eliminado=0)
    id = request.GET.get('id_mascotas')
    mascota = Mascotas.objects.get(id_mascotas=id)
    raza_mascota = Raza.objects.filter(id_raza = mascota.raza_id_raza, eliminado=0).first()
    id_tipo_mascota = raza_mascota.tipo_mascota_id_tipo_mascota
    print(mascota)
    if request.method == 'POST':
        form = MascotasForm(request.POST, instance=mascota)
        
        if form.is_valid():
            
            imagen = request.FILES.get('imagen', None)
            image_url=""
            if not imagen == None:
                image_url = mascota_url(imagen)
            descripcion = request.POST.get('raza_id_raza')
            print(descripcion)
            raza = Raza.objects.get(id_raza=descripcion)
            usu = Usuarios.objects.get(id_usuarios=request.session['id_usuario'])
            mascota = form.save(commit=False)
            mascota.fchcreacion = datetime.now()
            mascota.eliminado = 0
            mascota.raza_id_raza=raza
            mascota.usuarios_id_usuarios=usu
            mascota.save()
            return redirect('mascotas') 
    else:
        form = MascotasForm(instance=mascota)

    return render(request, 'tutor/actualizar_mascota.html', {'nickname':nickname,'form': form,'raza':raza ,'raza_db':mascota.raza_id_raza})

def mascota_eliminar(request, id):
    mascota = Mascotas.objects.get(id_mascotas=id)
    mascota.fcheliminacion = datetime.now()
    mascota.eliminado = 1
    mascota.save()
    return redirect('mascotas')  


def MascotaSOS(request,url):
    nickname=request.session['nickname']
    mascota=Mascotas.objects.filter(id_mascotas=url)
    return render(request,'tutor/mascota_SOS.html',{'mascota':mascota})
