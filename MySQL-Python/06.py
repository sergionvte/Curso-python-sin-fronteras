import mysql.connector
midb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'sergionvte',
        database = 'prueba'
    )
cursor = midb.cursor()

# Listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall()
print(resultado)

# Var definiciones de tablas
# cursor.execute('show create table Usuario')

# Insertar datos
# sql = 'insert into Usuario (email, username) values (%s, %s)'
# values = ('micorreo@correo.com', 'Adicast')

# Actualizar datos
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo2@correo.com', 2)
# cursor.execute(sql, values)
# 
# midb.commit()
# print(cursor.rowcount)

# Eliminar datos
# sql = ('delete from Usuario where id = %s')
# values = (4, ) # Tenemos que poner la coma, de lo contrartio nos va a dar un error
# cursor.execute(sql, values)
# midb.commit()
