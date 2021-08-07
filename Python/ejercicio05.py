#   Escribir una función que indique si el usuario es mayor de edad
def mayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(15)
usuario2 = Usuario(19)
print(mayor(usuario))
print(mayor(usuario2))