import os
from geopy.geocoders import Nominatim
from geopy import distance
from msvcrt import getch


# CLEAR SCREEN
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

    
# MENU PRINCIPAL
def menu():
    opciones_menu_principal = (
        "[1]Crear un nuevo archivo de multas",
        "[2]Listar las multas cercanas a los estadios",
        "[3]Listar las multas de microcentro",
        "[4]Emitir una alerta de vehiculos robados",
        "[5]Informacion a partir de dominio",
        "[6]Grafico a partir de las denuncias recibidas por mes",
        "[7]Salir")

    print("SISTEMA DE MULTAS DE LA CIUDAD DE BUENOS AIRES")
    print("=============================================")
    for opcion in opciones_menu_principal:
        print(opcion)

        
# MOSTRAR ESTADIOS DISPONIBLES        
def mostrar_estadios():
    print('Estadios Disponibles:')
    estadios: dict = {'RIVER': '-34.5479338,-58.4561614','BOCA': '-34.6353183,-58.3650225'}
    for estadio in estadios:
        print(estadio)
    cancha: bool = False
    while not cancha:
        try:
            estadio: str = input('Ingrese el estadio: ').upper()
            if estadio in estadios:
                cancha = True
            else:
                print('Estadio no valido')
        except ValueError:
            print('Estadio no valido')
    coordenadas_del_estadio: str = estadios[estadio]
    return coordenadas_del_estadio


# DIRECCION A PARTIR DE COORDENADAS
def obtener_direccion(coordenadas: str):
    geolocator = Nominatim(user_agent="manejo_csv")
    location = geolocator.reverse(coordenadas, language="es", exactly_one=True)
    direccion = location.raw['address']['road'] + " " + location.raw['address']['house_number']
    localidad = location.raw['address']['state']
    provincia = location.raw['address']['city']
    return direccion, localidad, provincia


# INFRACCIONES MICROCENTRO
def infracciones_microcentro(diccionario: dict):
    lista_impresa: bool = False
    while not lista_impresa:
    # CUADRANTE APROXIMADO A PARTIR DE COORDENADAS OPUESTAS (ALEM Y CORDOBA, RIVADAVIA Y CALLAO)
    # CORDOBA_Y_ALEM = '-34.5983795, -58.3725168'
    # ALEM_Y_RIVADAVIA = '-34.6091603, -58.3725168'
    # RIVADAVIA_Y_CALLAO = '-34.6091603, -58.3924939'
    # CALLAO_Y_CORDOBA = '-34.5983795, -58.3924939'

        tope_arriba_cuadrante: str = '-34.5983795'
        tope_abajo_cuadrante: str = '-34.6091603'
        tope_izquierdo_cuadrante: str = '-58.3924939'
        tope_derecho_cuadrante: str = '-58.3725168'
        # --------------------------------------------------------------------------------------------------------
        lista_infracciones_microcentro: list = []
        for telefono_de_infraccion in diccionario:
            latitud = diccionario[telefono_de_infraccion][2]
            longitud = diccionario[telefono_de_infraccion][3]
            if tope_arriba_cuadrante <= latitud <= tope_abajo_cuadrante and\
                    tope_derecho_cuadrante <= longitud <= tope_izquierdo_cuadrante:
                lista_infracciones_microcentro.append(diccionario[telefono_de_infraccion])
        print('Infracciones en microcentro: ', len(lista_infracciones_microcentro))
        for i in range(len(lista_infracciones_microcentro)):
            print(f"[{i}]  {lista_infracciones_microcentro[i]}")
        print("presione una tecla para continuar")
        getch()
        lista_impresa = True
    

# INFRACCIONES POR ESTADIO
def infracciones_estadio(infracciones: dict, coordenadas_estadio: str):
    lista_impresa: bool = False
    while not lista_impresa:
        lista_infracciones_estadio: list = []
        for telefono_de_infraccion in infracciones:
            latitud = infracciones[telefono_de_infraccion][2]
            longitud = infracciones[telefono_de_infraccion][3]
            coordenadas = latitud + ", " + longitud
            distancia: float = distance.distance(coordenadas_estadio, coordenadas).km
            if distancia <= 1:
                lista_infracciones_estadio.append(infracciones[telefono_de_infraccion])
        print(f'Infracciones cercanas a este estadio: ', len(lista_infracciones_estadio))
        for i in range(len(lista_infracciones_estadio)):
            print(f"[{i}]  {lista_infracciones_estadio[i]}")
        print("presione una tecla para continuar")
        getch()
        lista_impresa = True


