#   Escribir una función que reciba nombre y apellido y los agregue a un archivo
def agregarNombreAArchivo(nombre, apellido):
    archivo = open('ejercicio09.txt', 'a')
    archivo.write(nombre + ' ' + apellido + '\n')
    archivo.close()
agregarNombreAArchivo('Claudia', 'Castillo')



