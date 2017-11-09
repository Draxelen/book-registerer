"""
    Programa diseñado para automatizar el registro de libros nuevos dentro de un archivo txt
    Un simple script para practicar Python
"""
import os


def menu_principal():
    """Muestra el menu principal del programa"""

    dirlibros = r""  # Directorios donde se encuentran los libros
    dirarchivo = r""  # Archivo en donde se registran libros nuevos

    print("Buenos dias, estimado usuario.")

    while True:

        os.chdir(dirlibros) # Cambia a la carpeta indicada
        print("Por favor, elija una de las siguientes opciones")
        print("Registrar nuevo libro: 1")
        print("Salir del menu: 0")

        respuesta = int(input("Su opcion es?: "))

        if respuesta == 0:
            break
        elif respuesta == 1:
            registrar_libro(dirlibros, dirarchivo)
        else:
            print("\n Respuesta invalida \n")


def registrar_libro(dirlibros, dirarchivo):
    """Permite el registro del libro dentro del archivo encargado de la administracion de libros 
        Tiene dos argumentos: la direccion de la carpeta en donde almacena los libros
        Y la direccion del archivo txt
    """

    directorio_local = dirlibros
    print("\nDirectorio actual {} \n".format(directorio_local))

    while True:
        print("\nDIRECTORIO ACTUALIZADO: {} \n".format(directorio_local))

        # Se almacenan los nombres de los directorios y archivos en una list
        struc_dir = os.listdir(os.curdir)

        print("Mostrando estructura del directorio actual...")

        # mostrar todas las capetas y archivos del dir actual
        for i, elemento in enumerate(struc_dir):    # prev: for i in range(len(struc_dir))
            print("{}. {}".format(str(i + 1), elemento))

        res = input("\nAhora, elija la carpeta para seguir buscando el archivo, el archivo a registrar, \
        , up si desea subir un nivel o escriba 'cancelar' para terminar la operacion del programa: ")

        if res == "cancelar":
            break
        elif res == "up":
            if directorio_local == dirlibros:
                print("Ud. se encuentra en el nivel superior maximo, no es posible subir un nivel")
                print("Presione cualquier tecla para continuar")
            else:
                os.chdir("..")
                print("El directorio ha subido un nivel\n")
                input("Presione cualquier tecla para continuar")
                directorio_local = os.getcwd()
        else:
            try:
                elemento_seleccionado = struc_dir[int(res) - 1]
            except (IndexError, ValueError, TypeError):
                print("ERROR: Opcion invalida, las opciones deben ser las mostradas y en un valor decimal")
                input("Presione cualquier tecla para continuar")
                continue

            if os.path.isdir(elemento_seleccionado):                # si el elemento seleccionado es una carpeta...
                directorio_local += "\\" + elemento_seleccionado    # ...entonces continua la busqueda y se cambia de dir
                os.chdir(directorio_local)
            elif os.path.isfile(elemento_seleccionado):             # Si es un archivo...

                nombre_registro = directorio_local + "\\" + elemento_seleccionado    # ...entonces se tomara su nombre
                confirmacion_registro = confirmar_registro(nombre_registro)          # y se le pedira confirmacion al usuario

                # si el usuario acepto registrar el libro
                if confirmacion_registro:
                    try:
                        with open(dirarchivo, "r") as archivo_registro_read, open(dirarchivo, "a+") as archivo_registro_append:
                            
                            # si el archivo se encuentra vacio (0 bytes)
                            if os.stat(dirarchivo).st_size < 4:
                                print("El archivo se encuentra vacio, creando primera entrada...")
                                archivo_registro_append.write("{0}. {1}".format("1", nombre_registro))
                            else:
                                print("Registrando libro...")
                                contenido_archivo = archivo_registro_read.read()
                                libro_numero = len(contenido_archivo.split("\n\n"))
                                archivo_registro_append.write("\n\n{0}. {1}".format(str(libro_numero + 1), nombre_registro))

                            print("\n Exito, el libro ha sido registrado!!!")
                            break
                    except OSError as oserr:
                        print("Error OS: {0}".format(oserr))
                else:
                    print("El usuario ha declinado, registro cancelado")
        # endif


def confirmar_registro(nombre_registro):
    """Le permite al usuario confirmar si la seleccion es la correcta"""

    print("\n ¿Esta seguro de que desea registrar el siguiente documento en la hoja de \
     registro de libros? (" + nombre_registro + ")")
    print("Use si o no para su respuesta")

    while True:
        respuesta = input("Respuesta: ")

        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Respuesta invalida, intente de nuevo")


if __name__ == "__main__":
    menu_principal()
    input("Programa finalizado con exito, presione cualquier tecla para continuar...")
