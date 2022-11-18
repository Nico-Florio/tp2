import os
import msvcrt


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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
    


def main():
    cls()
    cerrar_programa = False
    while not cerrar_programa:
        menu()
        opcion_ok: bool = False
        while not opcion_ok:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion in range(1, 8):
                    opcion_ok = True
                else:
                    raise ValueError
            except ValueError:
                print("Opcion invalida")
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("Gracias por utilizar el sistema")
            print("Presione cualquier tecla para salir")
            msvcrt.getch()
            cerrar_programa = True
            exit()        