import mysql.connector
midb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'sergionvte',
        database = 'prueba'
    )
cursor = midb.cursor()

cursor.execute('select * from Usuario')

resultado = cursor.fetchone()

print(resultado)
