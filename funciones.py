import os
from geopy.geocoders import Nominatim
from geopy import distance
from msvcrt import getch
from matplotlib import pyplot as plt

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
    print(coordenadas_del_estadio)
    return coordenadas_del_estadio


def fecha_a_partir_de_timestamp(timestamp: str):
    fecha = timestamp.split(' ')[0]
    dia = fecha.split('-')[2]
    mes = fecha.split('-')[1]
    if mes == '01':
        mes = 'Enero'
    elif mes == '02':
        mes = 'Febrero'
    elif mes == '03':
        mes = 'Marzo'
    elif mes == '04':
        mes = 'Abril'
    elif mes == '05':
        mes = 'Mayo'
    elif mes == '06':
        mes = 'Junio'
    elif mes == '07':
        mes = 'Julio'
    elif mes == '08':
        mes = 'Agosto'
    elif mes == '09':
        mes = 'Septiembre'
    elif mes == '10':
        mes = 'Octubre'
    elif mes == '11':
        mes = 'Noviembre'
    elif mes == '12':
        mes = 'Diciembre'
    anio = fecha.split('-')[0]
    fecha = f'{dia} de {mes} de {anio}'
    return fecha


# DIRECCION A PARTIR DE COORDENADAS
def obtener_direccion(coordenadas: str):
    direccion = ""
    localidad = ""
    provincia = ""
    try:
        geolocator = Nominatim(user_agent="manejo_csv")
        location = geolocator.reverse(coordenadas, language="es", exactly_one=True)
        direccion = location.raw['address']['road'] + " " + location.raw['address']['house_number']
        localidad = location.raw['address']['state']
        provincia = location.raw['address']['city']
    except:
        pass
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
            print(f"[{i+1}]  {lista_infracciones_microcentro[i]}")
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
            direccion,localidad,provincia = obtener_direccion(coordenadas)
            fecha = fecha_a_partir_de_timestamp(infracciones[telefono_de_infraccion][0])
            distancia: float = distance.distance(coordenadas_estadio, coordenadas).km
            print(distancia)
            if distancia <= 1:
                lista_infracciones_estadio.append(infracciones[telefono_de_infraccion])
        print(f'Infracciones cercanas a este estadio: ', len(lista_infracciones_estadio))
        for i in range(len(lista_infracciones_estadio)):
            print(f'''[{i+1}] {lista_infracciones_estadio[i][5]}
En {direccion}, {localidad}, {provincia}
El dia {fecha}
''')
        print("presione una tecla para continuar")
        getch()
        lista_impresa = True

# funcion que se encarga de armar un grafico de barras con las infracciones por mes    
def grafico(infracciones:dict):
    infracciones_enero: int = 0
    infracciones_febrero: int = 0
    infracciones_marzo: int = 0
    infracciones_abril: int = 0
    infracciones_mayo : int = 0
    infracciones_junio : int = 0
    infracciones_julio: int = 0
    infracciones_agosto: int = 0
    infracciones_septiembre: int = 0
    infracciones_octubre: int = 0
    infracciones_noviembre: int = 0
    infracciones_diciembre: int = 0
    for telefono_de_infraccion in infracciones:
       if infracciones[telefono_de_infraccion][0][5:7] == '01':
           infracciones_enero += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '02':
           infracciones_febrero += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '03':
           infracciones_marzo += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '04':
           infracciones_abril += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '05':
           infracciones_mayo += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '06':
           infracciones_junio += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '07':
           infracciones_julio += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '08':
           infracciones_agosto += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '09':
           infracciones_septiembre += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '10':
           infracciones_octubre += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '11':
           infracciones_noviembre += 1
       elif infracciones[telefono_de_infraccion][0][5:7] == '12':
           infracciones_diciembre += 1
    infracciones_por_mes: list = [infracciones_enero, infracciones_febrero, infracciones_marzo, infracciones_abril, infracciones_mayo, infracciones_junio, infracciones_julio, infracciones_agosto, infracciones_septiembre, infracciones_octubre, infracciones_noviembre, infracciones_diciembre]
    meses: list = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    plt.bar(meses, infracciones_por_mes)
    plt.title('Infracciones por mes')
    plt.xlabel('Meses')
    plt.ylabel('Infracciones')
    plt.show()

    

