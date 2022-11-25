import csv
from funciones import *
from utils import *


def leer_archivo():
    infracciones: dict = {}
    with open('multas.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=',')
        for linea in lector:
            timestamp: str = linea[0]
            telefono: str = linea[1]
            latitud: int = linea[2]
            longitud: int = linea[3]
            ruta_foto: str = linea[4]
            descripcion: str = linea[5]
            ruta_audio: str = linea[6]
            infracciones[telefono] = (timestamp, telefono, latitud, longitud, ruta_foto, descripcion, ruta_audio)
    return infracciones



# Con la información leída del archivo CSV, se pide crear un nuevo archivo CSV que contenga los siguientes 
# campos: (Timestamp,Teléfono, Dirección de la infracción, Localidad, Provincia, patente, descripción texto, 
# descripción audio)
def crear_archivo(infracciones: dict):
    for infraccion in infracciones:
        timestamp: str = infracciones[infraccion][0]
        telefono: str = infracciones[infraccion][1]
        latitud: int = infracciones[infraccion][2]
        longitud: int = infracciones[infraccion][3]
        ruta_foto: str = infracciones[infraccion][4]
        descripcion_texto: str = infracciones[infraccion][5] 
        coordenadas: str  = latitud + ", " + longitud
        direccion, localidad, provincia = obtener_direccion(coordenadas)
        patente: str = obtener_patente(ruta_foto)
        descripcion_audio: str = obtener_texto_audio(infracciones[infraccion][6])



a = leer_archivo()
for i in a:
    print(a[i])



def robados():
    pass