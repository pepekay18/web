# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alergias(models.Model):
    id_alergias = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alergias'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Banner(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    provincia_id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='provincia_id_provincia', blank=True, null=True)
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comuna'


class DatosProfesional(models.Model):
    id_datos_profesional = models.AutoField(primary_key=True)
    codigo_licencia = models.CharField(unique=True, max_length=50)
    ano_egreso = models.IntegerField()
    casa_estudio = models.CharField(max_length=50)
    nombre_titulo = models.CharField(max_length=50)
    usuarios_id_usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_id_usuarios', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_profesional'


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    ventas_id_ventas = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='ventas_id_ventas')
    productos_id_productos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_id_productos')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Diagnosticos(models.Model):
    id_diagnosticos = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=50)
    indicaciones = models.CharField(max_length=50)
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey('FichaMascotas', models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    veterinaria_id_veterinaria = models.ForeignKey('Veterinaria', models.DO_NOTHING, db_column='veterinaria_id_veterinaria', blank=True, null=True)
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'diagnosticos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentacion(models.Model):
    id_documentacion = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey('FichaMascotas', models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')

    class Meta:
        managed = False
        db_table = 'documentacion'


class Enfermedades(models.Model):
    id_enfermedades = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enfermedades'


class FichaMascotas(models.Model):
    id_ficha_mascotas = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    alergias = models.IntegerField()
    enfermedades_cronicas = models.IntegerField()
    medicacion = models.IntegerField()
    antecedentes_accidentes = models.IntegerField()
    proc_quirurgicos = models.IntegerField()
    mascotas_id_mascotas = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='mascotas_id_mascotas')

    class Meta:
        managed = False
        db_table = 'ficha_mascotas'


class FichaMascotasAlergias(models.Model):
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey(FichaMascotas, models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    alergias_id_alergias = models.ForeignKey(Alergias, models.DO_NOTHING, db_column='alergias_id_alergias')

    class Meta:
        managed = False
        db_table = 'ficha_mascotas_alergias'
        unique_together = (('ficha_mascotas_id_ficha_mascotas', 'alergias_id_alergias'),)


class FichaMascotasEnfermedades(models.Model):
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey(FichaMascotas, models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    enfermedades_id_enfermedades = models.ForeignKey(Enfermedades, models.DO_NOTHING, db_column='enfermedades_id_enfermedades')

    class Meta:
        managed = False
        db_table = 'ficha_mascotas_enfermedades'
        unique_together = (('ficha_mascotas_id_ficha_mascotas', 'enfermedades_id_enfermedades'),)


class FichaMascotasMedicamentos(models.Model):
    medicamentos_id_medicamentos = models.ForeignKey('Medicamentos', models.DO_NOTHING, db_column='medicamentos_id_medicamentos')
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey(FichaMascotas, models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ficha_mascotas_medicamentos'
        unique_together = (('medicamentos_id_medicamentos', 'ficha_mascotas_id_ficha_mascotas'),)


class FichaMascotasProcedimientos(models.Model):
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey(FichaMascotas, models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    procedimientos_id_procedimientos = models.ForeignKey('Procedimientos', models.DO_NOTHING, db_column='procedimientos_id_procedimientos')

    class Meta:
        managed = False
        db_table = 'ficha_mascotas_procedimientos'
        unique_together = (('ficha_mascotas_id_ficha_mascotas', 'procedimientos_id_procedimientos'),)


class FotoMascotas(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    imagen = models.CharField(max_length=300, blank=True, null=True)
    mascotas_id_mascotas = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='mascotas_id_mascotas')

    class Meta:
        managed = False
        db_table = 'foto_mascotas'


class Hora(models.Model):
    id = models.IntegerField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion', blank=True, null=True)  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    id_tipo_hora = models.ForeignKey('TipoHora', models.DO_NOTHING, db_column='id_tipo_hora', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hora'


class Imagenes(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    url = models.CharField(max_length=300, blank=True, null=True)
    zona = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'imagenes'


class ImagenesBanner(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    url = models.CharField(max_length=300)
    texto = models.CharField(max_length=100, blank=True, null=True)
    id_banner = models.ForeignKey(Banner, models.DO_NOTHING, db_column='id_banner', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes_banner'


class Mascotas(models.Model):
    id_mascotas = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fchnacimiento = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    extraviada = models.IntegerField()
    usuarios_id_usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_id_usuarios')
    raza_id_raza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='raza_id_raza', blank=True, null=True)
    edad = models.IntegerField()
    color = models.CharField(max_length=45)
    genero = models.IntegerField()
    foto = models.CharField(max_length=300)
    hijo_de = models.CharField(max_length=45, blank=True, null=True)
    padres = models.CharField(max_length=45, blank=True, null=True)
    certificado_pedigree = models.IntegerField()
    comprobante_certificado = models.CharField(max_length=45, blank=True, null=True)
    registro_nacional_mascota_compania = models.IntegerField()
    certificado_registro = models.CharField(max_length=45, blank=True, null=True)
    id_externo = models.CharField(max_length=300)
    vacunada = models.IntegerField()
    esterilizada = models.IntegerField()
    alergias = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mascotas'


class Medicamentos(models.Model):
    id_medicamentos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medicamentos'


class ModoObtencion(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'modo_obtencion'


class NuestraTecnologia(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    titulo = models.CharField(max_length=50)
    parrafo = models.CharField(max_length=1500)
    url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nuestra_tecnologia'


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pais'


class Perfiles(models.Model):
    id_perfiles = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfiles'


class Politicas(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'politicas'


class PreguntasFrecuentes(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    respuesta = models.CharField(max_length=1000)
    pregunta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'preguntas_frecuentes'


class Procedimientos(models.Model):
    id_procedimientos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procedimientos'


class Productos(models.Model):
    id_productos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1500)
    caracteristicas = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField()
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    precio_promocion = models.IntegerField(blank=True, null=True)
    promocion = models.IntegerField()
    precio_costo = models.IntegerField()
    imagen = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Promociones(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=100)
    fechainicio = models.DateTimeField()
    fechatermino = models.DateTimeField(blank=True, null=True)
    habilitado = models.IntegerField()
    url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promociones'


class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    fchcreaccion = models.DateTimeField(db_column='fchCreaccion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region', blank=True, null=True)
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'provincia'


class QuienesSomos(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quienes_somos'


class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    tipo_mascota_id_tipo_mascota = models.ForeignKey('TipoMascota', models.DO_NOTHING, db_column='tipo_mascota_id_tipo_mascota')

    class Meta:
        managed = False
        db_table = 'raza'


class RazonTenencia(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'razon_tenencia'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchediccion = models.DateTimeField(db_column='fchEdiccion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    nombregeo = models.CharField(max_length=100, blank=True, null=True)
    pais_id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais_id_pais')
    eliminado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class RegistroVacuna(models.Model):
    id_registro_vacunas = models.IntegerField(primary_key=True)
    fchcreaccion = models.DateTimeField(db_column='fchCreaccion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    fecha_vacunacion = models.DateTimeField()
    fecha_duracion = models.DateTimeField(blank=True, null=True)
    vacunas_id_vacunas = models.ForeignKey('Vacunas', models.DO_NOTHING, db_column='vacunas_id_vacunas')
    ficha_mascotas_id_ficha_mascotas = models.ForeignKey(FichaMascotas, models.DO_NOTHING, db_column='ficha_mascotas_id_ficha_mascotas')
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registro_vacuna'


class Servicios(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=255)
    tipo_servicios = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'


class Suscripciones(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    email = models.CharField(max_length=50)
    habilitado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'suscripciones'


class TerminoCondiciones(models.Model):
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    titulo = models.CharField(max_length=50)
    termino = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'termino_condiciones'


class TipoCuenta(models.Model):
    id_tipo_cuenta = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class TipoHora(models.Model):
    id = models.IntegerField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion', blank=True, null=True)  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_hora'


class TipoMascota(models.Model):
    id_tipo_mascota = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_mascota'


class Token(models.Model):
    token = models.CharField(max_length=255)
    mascotas_id_mascotas = models.ForeignKey(Mascotas, models.DO_NOTHING, db_column='mascotas_id_mascotas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'


class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    rut = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    fono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    activado = models.IntegerField()
    autorizado = models.IntegerField()
    recuperar = models.IntegerField()
    bloqueado = models.IntegerField()
    licencia = models.CharField(max_length=100, blank=True, null=True)
    cedula = models.CharField(max_length=100, blank=True, null=True)
    intentos_erroneos = models.IntegerField()
    perfiles_id_perfiles = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='perfiles_id_perfiles', blank=True, null=True)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna', blank=True, null=True)
    tipo_cuenta_id_tipo_cuenta = models.ForeignKey(TipoCuenta, models.DO_NOTHING, db_column='tipo_cuenta_id_tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vacunas(models.Model):
    id_vacunas = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vacunas'


class Ventas(models.Model):
    id_ventas = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField()
    monto = models.IntegerField()
    eliminado = models.IntegerField()
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    usuarios_id_usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='usuarios_id_usuarios')

    class Meta:
        managed = False
        db_table = 'ventas'


class Veterinaria(models.Model):
    id_veterinaria = models.AutoField(primary_key=True)
    fchcreacion = models.DateTimeField(db_column='fchCreacion')  # Field name made lowercase.
    fchedicion = models.DateTimeField(db_column='fchEdicion', blank=True, null=True)  # Field name made lowercase.
    fcheliminacion = models.DateTimeField(db_column='fchEliminacion', blank=True, null=True)  # Field name made lowercase.
    eliminado = models.IntegerField()
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fono = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veterinaria'
