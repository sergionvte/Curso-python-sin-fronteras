import os

def agregarAlArchivo(texto):
    archivo = open('file.txt', 'a')
    archivo.write(texto)
    archivo.write('\n')
    archivo.close()

def reemplazarElArchivo(texto):
    archivo = open('file.txt', 'w')
    archivo.write(texto)
    archivo.write('\n')
    archivo.close()

def mostrarArchivo():
    archivo = open('file.txt', 'r')
    print(archivo.read())
    archivo.close()

def redaccion(opc):
    if opc == 1:
        os.system('cls')
        texto = input('Ingresa a continuación tu nota:\n')
        agregarAlArchivo(texto)
        os.system('cls')
        print('Tu nota es la siguiente: \n')
        mostrarArchivo()
    elif opc == 2:
        os.system('cls')
        texto = input('Ingresa a continuación tu nota:\n')
        reemplazarElArchivo(texto)
        os.system('cls')
        print('Tu nota es la siguiente: \n')
        mostrarArchivo()
    else:
        print('No elegiste ninguna de las opciones anteriores.')

def menu():
    os.system('cls')
    opc = input('1. Agregar texto al final del archivo.\n2. Cambiar todo el texto del archivo\nOpcion: ')
    try:
        opc = int(opc)
        redaccion(opc)
    except:
        print('La opción que elegiste no existe.')
        exit()

menu()