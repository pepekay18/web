import base64
import os
from io import BytesIO
from tkinter import Image
from uuid import uuid4

from PIL import Image, UnidentifiedImageError
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
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import quote, urlparse

from .models import *
from django.views.defaults import server_error
import traceback
import sys
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# __url="http://3.15.180.186:8080/"
__url = "http://localhost:8080/"


def sha256(variable):
    variable_str = str(variable)

    sha256_hash = hashlib.sha256(variable_str.encode()).hexdigest()

    # Retorna el hash SHA-256
    return sha256_hash


# region login_usuario

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        login_status = request.session.get('token')
        if login_status is None:
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return _wrapped_view


def django_prelogin_view(request):
    return render(request, 'html/prelogin.html')


def django_login_view(request):
    t = request.GET.get("t", "t1")
    if request.method == 'POST':
        fastapi_login_url = f"{__url}login"

        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        encriptada = sha256(contrasena)

        response = requests.post(
            fastapi_login_url,
            json={"email": email, "contrasena": encriptada, "tipo": t}
        )

        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            nickname = data.get('nickname')
            autorizado = data.get('autorizado')
            id_perfil = data.get('id_perfil')
            id_usuario = data.get('id_usuario')

            if token and nickname:

                request.session['token'] = token
                request.session['nickname'] = nickname
                request.session['autorizado'] = autorizado
                request.session['id_perfil'] = id_perfil
                request.session['id_usuario'] = id_usuario
                if request.session["id_perfil"] == 3:
                    return redirect('administrador')
                elif request.session["id_perfil"] == 1:
                    return redirect("mascotas")
                else:
                    return redirect('veterinario')
        respuesta = response.text
        respuesta_detail = json.loads(respuesta)

        fallo = respuesta_detail['detail']
        print(fallo)
        # Manejo de inicio de sesión fallido
        return render(request, 'html/inicio.html', {'error_message': fallo, 't': t, 'nickname': nickname})

    return render(request, 'html/login.html', {'t': t})


def login_recuperar(request):
    if request.method == 'POST':
        fastapi_login_url = f"{__url}login"

        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        contrasena_nueva = request.POST.get("contrasena_nueva")
        encriptada1 = sha256(contrasena)
        encriptada2 = sha256(contrasena_nueva)

        response = requests.post(
            fastapi_login_url,
            json={"email": email, "contrasena": encriptada1,
                  "contrasena_nueva": encriptada2}
        )

        if response.status_code == 200:
            mensage = 'Cambio de contraseña exitoso.'
            return render(request, "html/recuperar.html", {"mensaje": mensage})
        else:
            mensage = "Algo salió mal. Intentelo otra vez."
            return render(request, "html/recuperar.html", {"mensaje": mensage})

    return render(request, "html/recuperar.html")


def recuperar(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        activar_url = f"{__url}usuarios/recuperar/{email}"
        response = requests.get(activar_url)

        if response.status_code == 200:
            return redirect('login_recuperar')
    return render(request, "html/validar.html")


# endregion


def nosotros(request):
    nickname = request.session.get('nickname', None)
    nosotros = QuienesSomos.objects.filter(eliminado=0)
    return render(request, 'html/nosotros.html', {'nosotros': nosotros, 'nickname': nickname})


def validar_rut(rut):
    rut = rut.replace(".", "").replace(" ", "").upper()

    if "-" not in rut or len(rut) < 3:
        return False

    partes = rut.split("-")
    numero = partes[0]
    digito_verificador = partes[1]

    if not numero.isdigit():
        return False

    suma = 0
    multiplicador = 2

    for i in range(len(numero) - 1, -1, -1):
        suma += int(numero[i]) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_esperado = 11 - resto

    if digito_esperado == 11:
        digito_esperado = 0
    elif digito_esperado == 10:
        digito_esperado = 'K'

    return str(digito_esperado) == digito_verificador


def crearUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        rut = request.POST.get('rut')
        primer_apellido = request.POST.get('primer_apellido')

        fono = request.POST.get('fono')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')
        contrasena1 = request.POST.get('contrasena1')
        email = request.POST.get('email')
        nombre_comuna = request.POST.get('nombre_comuna')
        nombre_region = request.POST.get('nombre_region')
        nombre_pais = request.POST.get('nombre_pais')
        print(nombre_pais)
        print(rut == '')
        rutvalido = True
        message = ""

        if rut == '':
            rut = ''
        else:
            rutvalido = validar_rut(rut)

        if nombre_pais == 'Chile':
            if rutvalido == False:
                message = "rut no valido"

                return JsonResponse({"message": message})
        if contrasena != contrasena1:
            message = "las claves tiene que ser iguales"
            return JsonResponse({"message": message})
        encriptada = sha256(contrasena)
        payload = {
            "nombre": nombre,
            "rut": rut,
            "primer_apellido": primer_apellido,
            "fono": fono,
            "direccion": direccion,
            "contrasena": encriptada,
            "email": email,
            "nombre_comuna": nombre_comuna,
            "nombre_region": nombre_region,
            "id_perfiles": 1,
            "id_tipo_cuenta": 1,
            "licencia": "",
        }
        print(payload)
        # URL del endpoint de creación en FastAPI
        url = f"{__url}usuarios/crear"
        print(url)

        # Realizar la solicitud POST
        response = requests.post(url, json=payload)
        print("Respuesta de la API:", response.text)
        if response.status_code == 200:
            print("200")
            mensaje = response.text
            return JsonResponse(json.loads(mensaje))
        else:
            print("NO200")
            return JsonResponse({"message": "Error al crear usuario. Ingrese datos válidos."})

    return render(request, "html/crearusuario.html")


def crearveterinario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        rut = request.POST.get('rut')
        primer_apellido = request.POST.get('primer_apellido')

        fono = request.POST.get('fono')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')
        contrasena1 = request.POST.get('contrasena1')
        email = request.POST.get('email')
        nombre_comuna = request.POST.get('nombre_comuna')
        nombre_region = request.POST.get('nombre_region')
        nombre_pais = request.POST.get('nombre_pais')
        cedula = request.FILES["cedula"]
        licencia = request.POST["licencia"]

        rutvalido = validar_rut(rut)
        if rut == '':
            rut = None

        if nombre_pais == 'Chile':
            if rutvalido == False:
                mensage = "rut invalido"
                print(mensage)

                return render(request, "html/crearveterinario.html", {"mensage": mensage})
        if contrasena != contrasena1:
            mensage = "las claves tiene que ser iguales"
            print(mensage)
            return render(request, "html/crearveterinario.html", {"mensage": mensage})
        incriptada = sha256(contrasena)
        payload = {
            "nombre": nombre,
            "rut": rut,
            "primer_apellido": primer_apellido,
            "fono": fono,
            "direccion": direccion,
            "contrasena": incriptada,
            "email": email,
            "nombre_comuna": nombre_comuna,
            "nombre_region": nombre_region,
            "licencia": licencia,
            "id_perfiles": 2,
            "id_tipo_cuenta": 1
        }
        # URL del endpoint de creación en FastAPI
        url = f"{__url}usuarios/crear"
        print(url)

        # Realizar la solicitud POST
        response = requests.post(url, json=payload)
        print("Respuesta de la API:", response.text)
        if response.status_code == 200:

            mensaje = response.text
            mensaje_decodificado = html.unescape(mensaje)
            respuesta_detail = json.loads(mensaje)
            if respuesta_detail["id"] != 0:
                url_archivos3 = ""
                id = respuesta_detail["id"]
                try:
                    s3 = boto3.client("s3", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

                    url_archivos3 = cedula.name

                    s3.upload_fileobj(cedula, settings.AWS_STORAGE_BUCKET_NAME, f"usuarios/{id}/{url_archivos3}")

                    url_archivos3 = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/usuarios/{id}/{url_archivos3}"
                    url = f"{__url}usuarios/actualizar_cedula"
                    payload = {
                        "cedula": url_archivos3,
                        "id": id
                    }
                    # Realizar la solicitud POST
                    response = requests.post(url, json=payload)
                    print(response)

                except NoCredentialsError as ex:
                    print(ex)
                return render(request, "html/login.html", {"mensaje": mensaje_decodificado, "datos": payload})
            else:
                return render(request, "html/crearveterinario.html",
                              {"mensaje": mensaje_decodificado, "datos": payload})
        else:
            mensaje = "Error al crear veterinario. Ingrese datos válidos."

    return render(request, "html/crearveterinario.html")


def preregistro(request):
    return render(request, 'html/preregistro.html')


@login_required
def crear_mascota(request):
    tipo_mascota = []
    url_tipo_mascota = f"{__url}tipo_mascota/todas"

    response_tipo_mascota = requests.get(url_tipo_mascota, headers={
        'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    tipo_mascota = response_tipo_mascota.json()
    print(tipo_mascota)
    if request.method == 'POST':

        raza = []
        url_raza = f"{__url}raza/todas/{tipo_mascota_id}"
        response_raza = requests.get(url_tipo_mascota)
        raza = response_raza.json()
        if request.method == 'POST':
            nombre = request.POST.get('nombre')

    return render(request, "html/crearmascota.html", {'tipo_mascota': tipo_mascota})


def activar_usuario(request, id_usuario):
    # Construye la URL de activación del usuario utilizando el ID proporcionado
    activar_url = f"{__url}usuarios/activar/{id_usuario}"

    # Realiza una solicitud GET a la URL de activación
    response = requests.get(activar_url)

    # Si la solicitud fue exitosa, puedes redirigir al usuario a la página de inicio
    if response.status_code == 200:
        return redirect('inicio')


def desbloquear(request, id_usuario):
    # Construye la URL de activación del usuario utilizando el ID proporcionado
    activar_url = f"{__url}usuarios/desbloquear/{id_usuario}"

    # Realiza una solicitud GET a la URL de activación
    response = requests.get(activar_url)

    # Si la solicitud fue exitosa, puedes redirigir al usuario a la página de inicio
    if response.status_code == 200:
        return redirect('inicio')


def error_404(request, exception):
    return render(request, 'html/404.html')


def handler500(request):
    # Captura la traza de pila (stack trace) para obtener información sobre el error
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_message = f"Error 500: {str(exc_type)} - {str(exc_value)}"
    traceback_message = '\n'.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(error_message)
    print(traceback_message)

    return server_error(request, template_name='html/500.html')


@login_required
def personal(request):
    nickname = request.session.get('nickname', None)
    mascotas = []
    id_usuario = request.session.get('id_usuario', None)

    url_mascotas = f"{__url}mascotas/todos/{id_usuario}"

    response_mascotas = requests.get(url_mascotas, headers={
        'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    mascotas = response_mascotas.json()
    print(mascotas)
    page = request.GET.get('page', 1)
    # paginator = Paginator(mascotas, 8)
    # try:
    # masco = paginator.page(page)
    # except PageNotAnInteger:
    # masco = paginator.page(1)
    # except EmptyPage:
    # masco = paginator.page(paginator.num_pages)

    return render(request, "html/personal.html", {'nickname': nickname, "mascotas": mascotas})  # , "masco": masco})


def logout(request):
    request.session.clear()
    return redirect('login')


def demos3(request):
    if request.method == "POST" and request.FILES["foto"]:
        foto = request.FILES["foto"]

        try:
            s3 = boto3.client("s3", aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

            nombre = foto.name

            s3.upload_fileobj(foto, settings.AWS_STORAGE_BUCKET_NAME, nombre)

            url_archivos3 = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{nombre}"
            print(url_archivos3)
        except NoCredentialsError as ex:
            print(ex)
    return render(request, "html/demo.html")


def funcionamiento(request):
    nickname = request.session.get('nickname', None)
    funcion = NuestraTecnologia.objects.filter(eliminado=0)
    return render(request, "html/funcionamiento.html", {'nickname': nickname, 'funcion': funcion})


def politicas(request):
    politicas = Politicas.objects.filter(eliminado=0)
    return render(request, "html/politicas.html", {'politicas': politicas})


def preguntas(request):
    preguntas = PreguntasFrecuentes.objects.filter(eliminado=0)
    return render(request, "html/preguntas.html", {'preguntas': preguntas})


def terminos(request):
    terminos = TerminoCondiciones.objects.filter(eliminado=0)
    return render(request, "html/terminos.html", {'terminos': terminos})


def nuestra(request):
    nuestra = NuestraTecnologia.objects.filter(eliminado=0)
    return render(request, "html/nuestra.html", {'nuestra': nuestra})


def productos(request, number):
    nickname = request.session.get('nickname', None)
    productos = Productos.objects.filter(id_productos=number)

    return render(request, 'html/productos.html', {'productos': productos, "nickname": nickname})


def inicio(request):
    nickname = request.session.get('nickname', None)
    productos = Productos.objects.filter(eliminado=0)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        mensaje = request.POST.get('mensaje')
        email = request.POST.get('email')
        print(nombre)
        send_mail(
            'Contacto',
            f'''{mensaje} mensaje enviado por: {nombre} correo: {email}''',
            'settings.EMAIL_HOST_USER',
            ['dearpetc@gmail.com'],
            fail_silently=False
        )
    return render(request, 'html/inicio.html', {'nickname': nickname, "productos": productos})


def mascotaSOS_1(request, id_externo):
    latitud = request.GET.get('lat', 0.0)
    longitud = request.GET.get('lon', 0.0)
    print(latitud)
    payload = {
        "id_externo": id_externo,
        "latitud": latitud,
        "longitud": longitud
    }

    # La URL de la API a la que enviarás la notificación
    notificacion_url = f"{__url}usuarios/create_notification"

    # Realizar la solicitud POST para crear la notificación
    response = requests.post(notificacion_url, json=payload)
    print("Respuesta de la API:", response.text)

    # Verificar la respuesta de la API
    if response.status_code == 200:
        print("Notificación creada correctamente.")
        return render(request, 'html/search_id.html', {'id_externo': id_externo})
    else:
        print("Error al crear la notificación.")
        return JsonResponse({"message": "Error al crear notificación."}, status=400)


def mascotaSOS(request, id_externo):
    id_externo = id_externo
    mascota = Mascotas.objects.filter(eliminado=0, id_externo=id_externo).first()

    return render(request, 'html/search_id.html', {
        'id_externo': id_externo,
        'mascota': mascota,
        'url': __url,
        'img_url': mascota.foto
    })


def SendNotification(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id_mascotas = data.get('id_mascotas')
            latitud = data.get('lat', 0.0)
            longitud = data.get('lon', 0.0)

            # Imprime las coordenadas para ver si se están recibiendo correctamente
            print(f"Latitud: {latitud}, Longitud: {longitud}, mascota: {id_mascotas}")

            payload = {
                "id_mascotas": id_mascotas,
                "latitud": latitud,
                "longitud": longitud
            }

            # La URL de la API a la que enviarás la notificación
            notificacion_url = f"{__url}/usuarios/create_notification"

            # Realizar la solicitud POST para crear la notificación
            response = requests.post(notificacion_url, json=payload)
            print("Respuesta de la API:", response.text)

            # Verificar la respuesta de la API
            if response.status_code == 200:
                print("Notificación Enviada correctamente.")
                # Enviar latitud y longitud al contexto
                return JsonResponse({"message": "Notificación Enviada correctamente."}, status=200)
            else:
                print("Error al crear la notificación.")
                return JsonResponse({"message": "Error al crear notificación."}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON mal formado"}, status=400)
    return None

def allRazasTipoMascota(request, tipoId):
   if request.method == "GET":
       try:
        razaPorTipo_Url = f"{__url}/raza/todas/{tipoId}"
        response = requests.get(razaPorTipo_Url, headers={
        'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
        print("Respuesta de la API:", response.text)

        # Verificar la respuesta de la API
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data, safe=False)
       except json.JSONDecodeError:
           return JsonResponse({"error": "JSON mal formado"}, status=400)
       return None


def MyProfile(request, id_externo):
    mascota = Mascotas.objects.filter(eliminado=0, id_externo=id_externo).first()
    # usuario = Usuarios.objects.filter(eliminado=0, id_usuarios=mascota.usuarios_id_usuarios.id_usuarios).first()

    return render(request, 'html/tag_SOS.html', {
        'id_externo': id_externo,
        'mascota': mascota})

#@csrf_exempt  # solo si no enviás CSRF desde JS
def upload_images(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            img_base64 = data.get('img')
            tipo = data.get('type')
            # print("🧪 Base64 recibido (corte):", img_base64[:100])
            if not img_base64:
                return HttpResponseBadRequest("Imagen vacía.")

            if "," in img_base64:
                img_base64 = img_base64.split(",")[1]

            print("🧪 sin cabecera):", img_base64[:100])

            image_data = base64.b64decode(img_base64)
            print("🧪 antes open")
            try:
                image = Image.open(BytesIO(image_data))
                image = image.convert('RGB')
            except Exception as e:
                print("🧪 no se pudo abrir la imagen" )
                return JsonResponse({'error': f'No se pudo abrir imagen: {str(e)}'}, status=400)

            imagen_nombre = f"{uuid4()}.png"
            print(imagen_nombre)
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'mascota')
            os.makedirs(upload_dir, exist_ok=True)
            upload_path = os.path.join(upload_dir, imagen_nombre)
            print(upload_path)
            image.save(upload_path)

            url_imagen = f"{settings.MEDIA_URL}mascota/{imagen_nombre}"
            return JsonResponse({'url': url_imagen})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return HttpResponseBadRequest("Método no permitido.")

def delete_img_path(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ruta_relativa = data.get('path')

            if not ruta_relativa:
                return JsonResponse({'error': 'Parámetro "path" requerido'}, status=400)

            print(ruta_relativa)
            ruta_relativa = ruta_relativa.lstrip('/')
            # Prevenir intentos de acceso fuera del directorio permitido
            if '..' in ruta_relativa or ruta_relativa.startswith('/'):
                return JsonResponse({'error': 'Ruta inválida'}, status=400)

            # Construir ruta absoluta
            ruta_absoluta = os.path.join(settings.MEDIA_ROOT, ruta_relativa.replace('media/', '', 1))

            if os.path.exists(ruta_absoluta):
                os.remove(ruta_absoluta)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': 'Archivo no encontrado'}, status=404)

        except Exception as e:
            return JsonResponse({'error': f'Error al eliminar archivo: {str(e)}'}, status=500)

    return HttpResponseBadRequest("Método no permitido.")

def validarQR(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            qrData = data["qr"]

            exist_url = f"{__url}/mascotas/exist/{qrData}"

            response = requests.get(exist_url, headers={
                'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
            print("Respuesta de la API:", response.text)

            # Verificar la respuesta de la API
            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data, safe=False)

        except Exception as e:
            return JsonResponse({'error': f'Error al validar QR: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido.'}, status=400)

