#   Escribir una función que encuentre el elemento menor de una lista
def elementoMenor(lista):
    menor = 0

    for elemento in lista:
        if elemento < menor:
            menor = elemento

    print('El elemento menor es {}'.format(menor))        

lista = [7, 2, -55, 4, -45]
elementoMenor(lista) 