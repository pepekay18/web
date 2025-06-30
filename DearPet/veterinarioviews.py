from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .forms import *
from datetime import datetime
from . import views
import os


__url="http://localhost:8080/"
def index(request):
    id_usuario = request.session['id_usuario']
    fastapi_usuario_url=f"{__url}profesionales/{id_usuario}"
    response = requests.get(fastapi_usuario_url,headers={
                                     'Authorization': 'Bearer {token}'.format(token=request.session['token'])})
    especialidad=""
    if response.status_code == 200:
            data = response.json()
            especialidad = data.get('nombre_titulo')   
            print("especialidad") 
    
    return render(request,'veterinario/home.html', {"nickname":request.session['nickname'], "especialidad":especialidad})

def veterinario(request):
    nickname=request.session['nickname']

    return render(request,'veterinario/inicio.html',{'nickname':nickname})