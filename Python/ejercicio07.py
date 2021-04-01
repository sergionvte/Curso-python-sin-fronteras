#   Escribir una función que indique cuantas vocales tiene un String
def contarVocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    palabra = palabra.lower()
    for letra in palabra:
        if letra in vocales:
            contador = contador + 1
    print(contador)

contarVocales('Hola mUndo')