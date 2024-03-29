import msvcrt
from funciones import *
from manejos_csv import *



def main():
    cls()
    infracciones = leer_archivo()
    cerrar_programa = False
    while not cerrar_programa:
        cls()
        menu()
        print()
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
            cls()
            crear_archivo(infracciones)
        elif opcion == 2:
            cls()
            estadio = mostrar_estadios()
            infracciones_estadio(infracciones, estadio)
        elif opcion == 3:
            cls()
            infracciones_microcentro(infracciones)
        elif opcion == 4:
            patentes_robadas: list = leer_archivo_txt()
            print(robados(patentes_robadas))
        elif opcion == 5:
            pass
        elif opcion == 6:
            grafico(infracciones)
        elif opcion == 7:
            print("Gracias por utilizar el sistema")
            print("Presione cualquier tecla para salir")
            msvcrt.getch()
            cerrar_programa = True
            exit()

main()