from conexion import conectar
from crud_libros import agregar_libro, ver_libros, eliminar_libro
from crud_prestamos import prestar_libro, ver_prestamos
from menu import mostrar_menu

def main():
    conexion = conectar()

    if conexion is None:
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro(conexion)
        elif opcion == "2":
            ver_libros(conexion)
        elif opcion == "3":
            eliminar_libro(conexion)
        elif opcion == "4":
            prestar_libro(conexion)
        elif opcion == "5":
            ver_prestamos(conexion)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

    conexion.close()

if __name__ == "__main__":
    main()