import csv
from funciones import *


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
