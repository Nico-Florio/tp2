import os
from geopy.geocoders import Nominatim


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    opciones_menu_principal = {
        "[1]Crear un nuevo archivo de multas",
        "[2]Listar las multas cercanas a los estadios",
        "[3]Listar las multas de microcentro",
        "[4]Emitir una alerta de vehiculos robados",
        "[5]Informacion a partir de dominio",
        "[6]Grafico a partir de las denuncias recibidas por mes",
        "[7]Salir"}

    print("SISTEMA DE MULTAS DE LA CIUDAD DE BUENOS AIRES")
    print("=============================================")
    for opcion in opciones_menu_principal:
        print(opcion)


def obtener_direccion(coordenadas: str):
    geolocator = Nominatim(user_agent="manejo_csv")
    location = geolocator.reverse(coordenadas, language="es", exactly_one=True)
    direccion = location.raw['address']['road'] + " " + location.raw['address']['house_number']
    localidad = location.raw['address']['state']
    provincia = location.raw['address']['city']
    return direccion, localidad, provincia
