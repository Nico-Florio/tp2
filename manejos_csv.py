import csv
import os
import json
from geopy.geocoders import Nominatim


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
            infracciones[telefono] = {timestamp, telefono, latitud, longitud, ruta_foto, descripcion, ruta_audio}
    return infracciones


# Con la información leída del archivo CSV, se pide crear un nuevo archivo CSV que contenga los siguientes 
# campos: (Timestamp,Teléfono, Dirección de la infracción, Localidad, Provincia, patente, descripción texto, 
# descripción audio)
def crear_nuevo_csv(infracciones: dict):
    with open('multas_nuevo.csv', 'w') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=',')
        escritor.writerow(['Timestamp', 'Telefono', 'Direccion', 'Localidad', 'Provincia', 'Patente', 'Descripcion texto', 'Descripcion audio'])
        geolocator = Nominatim(user_agent="multas")
        for infraccion in infracciones:
            direccion = geolocator.reverse(infraccion[2] + ',' + infraccion[3])
            escritor.writerow([infraccion[0], infraccion[1], direccion['road'], direccion['city'], direccion['state']])
            print(f'''
            Fecha: {infraccion[0]}
            Telefono: {infraccion[1]}
            Direccion: {direccion['road']}
            Localidad: {direccion['city']}
            Provincia: {direccion['state']}
            ''')

diccionario = leer_archivo()    
crear_nuevo_csv(diccionario)