import msvcrt
from funciones import *
from manejos_csv import *


def main():
    cls()
    infracciones = leer_archivo()
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
            crear_archivo(infracciones)
        elif opcion == 2:
            infracciones_estadio(infracciones)
        elif opcion == 3:
            infracciones_cuadrante(infracciones)
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

main()