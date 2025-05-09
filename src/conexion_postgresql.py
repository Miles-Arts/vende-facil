import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='VendeFacil'
    )
    
    print('...Conexión exitosa...')
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM asignaturas")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print((ex))    
    
    
finally:
    connection.close()  
    print("...Conexión Finalizada...")  