import csv
import os
import json
from geopy.geocoders import Nominatim
import speech_recognition as sr


CORDOBA_Y_ALEM = '-34.5983795,-58.3725168'
ALEM_Y_RIVADAVIA = '-34.6072815,-58.372162'
RIVADAVIA_Y_CALLAO = '-34.6091603,-58.3924939'
CALLAO_Y_CORDOBA = '-34.5996235,-58.3951324'



def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def obtener_direccion(coordenadas: str):
    geolocator = Nominatim(user_agent="manejo_csv")
    location = geolocator.reverse(coordenadas, language="es", exactly_one=True)
    direccion = location.raw['address']['house_number'] + " " + location.raw['address']['road']
    localidad = location.raw['address']['city']
    provincia = location.raw['address']['state']
    return direccion, localidad, provincia
    

def leer_archivo():
    infracciones: dict = {}
    with open('multas.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=',')
        for linea in lector:
            timestamp = linea[0]
            telefono = linea[1]
            latitud = linea[2]
            longitud = linea[3]
            ruta_foto = linea[4]
            descripcion = linea[5]
            ruta_audio = linea[6]
            infracciones[telefono] = (timestamp, telefono, latitud, longitud, ruta_foto, descripcion, ruta_audio)
    return infracciones



# Con la información leída del archivo CSV, se pide crear un nuevo archivo CSV que contenga los siguientes 
# campos: (Timestamp,Teléfono, Dirección de la infracción, Localidad, Provincia, patente, descripción texto, 
# descripción audio)
def crear_archivo(infracciones: dict):
    for infraccion in infracciones:
        timestamp = infracciones[infraccion][0]
        telefono = infracciones[infraccion][1]
        latitud = infracciones[infraccion][2]
        longitud = infracciones[infraccion][3]
        coordenadas = latitud + ", " + longitud
        direccion, localidad, provincia = obtener_direccion(coordenadas)
        print("\n", direccion, "\n", localidad, "\n", provincia, "\n")
        






def menu():
    print(obtener_direccion(RIVADAVIA_Y_CALLAO))

    diccionario: dict = leer_archivo()
        
menu()