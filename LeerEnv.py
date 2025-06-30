def cargar_variables_de_entorno():
    # Cargar las variables de entorno desde el archivo .env
    with open('SECRET_KEY.env') as f:
        env_vars = f.readlines()

    # Crear un diccionario para almacenar las variables de entorno
    variables_de_entorno = {}

    # Extraer las variables de entorno del archivo .env
    for line in env_vars:
        key, value = line.strip().split('=')
        variables_de_entorno[key] = value

    return variables_de_entorno


def host(variables_entorno):
    return variables_entorno.get('host')


def user(variables_entorno):
    return variables_entorno.get('user')


def password(variables_entorno):
    return variables_entorno.get('password')
def name(variables_entorno):
    return variables_entorno.get('name')


variables_entorno = cargar_variables_de_entorno()

# Obtener las variables de entorno específicas
var1 = host(variables_entorno)
var2 = user(variables_entorno)
var3 = password(variables_entorno)
var4 = name(variables_entorno)
