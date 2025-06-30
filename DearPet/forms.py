from django import forms
from .models import *



class PoliticasForm(forms.ModelForm):
    class Meta:
        model = Politicas
        fields = [ 'titulo','descripcion', 'url']

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = [ 'nombre', 'ubicacion']
class ImagenesBannerForm(forms.ModelForm):
    class Meta:
        model = ImagenesBanner
        fields = ['url', 'texto', 'id_banner']

class ImagenesForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = ['url', 'zona']

class PreguntasFrecuentesForm(forms.ModelForm):
    class Meta:
        model= PreguntasFrecuentes
        fields =['pregunta','respuesta']

class PromocionesForm(forms.ModelForm):
    class Meta:
        model=Promociones
        fields =['nombre','fechainicio','fechatermino','habilitado','url']

class QuienesSomosForm(forms.ModelForm):
    class Meta:
        model=QuienesSomos
        fields =['descripcion','url']        

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields =['nombre','descripcion','precio','stock','precio_promocion','promocion','precio_costo','caracteristicas']
class SuscripcionForm(forms.ModelForm):
    class Meta:
        model=Suscripciones
        fields =['email','habilitado']     

class TerminosForm(forms.ModelForm):
    class Meta:
        model=TerminoCondiciones
        fields =['titulo','termino']             

class tecnologiasForm(forms.ModelForm):
    class Meta:
        model=NuestraTecnologia
        fields =['titulo','parrafo','url']                     

class UsuariosForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields =['rut','nombre','primer_apellido','fono','direccion','email']   
        
class MascotasForm(forms.ModelForm):
    class Meta:
        model=Mascotas
        fields = [
            'nombre', 'raza_id_raza', 'genero', 'fchnacimiento', 'descripcion', 'extraviada',
            'edad', 'color', 'vacunada', 'esterilizada','alergias',
        ]        

class UsuariosContrasenaForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields =['contrasena']   
