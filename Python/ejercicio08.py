#   Escribir una aplicación que reciba una cantidad infinita de números hasta
#   decir basta, luego que devuelva la suma de los números ingresados
lista = []
suma = 0
while True:
    dato = input('Ingresa un dato -> ')
    if dato != 'basta':
        try:
            dato = int(dato)
            lista.append(dato)
        except:
            print('El dato que ingresado no es válido')
            exit()
    else:
        break
for elemento in lista:
    suma = suma + elemento
print(suma)