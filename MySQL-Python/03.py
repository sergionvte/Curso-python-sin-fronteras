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

# Var definiciones de tablas
# cursor.execute('show create table Usuario')

# Insertar datos
sql = 'insert into Usuario (email, username) values (%s, %s)'
values = ('micorreo@correo.com', 'Adicast')
cursor.execute(sql, values)
midb.commit()
print(cursor.rowcount)


