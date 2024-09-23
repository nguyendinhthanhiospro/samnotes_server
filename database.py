import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root1',
    password='password!',
    database='mysql'
)
if connection.is_connected():
    print('Connected Successfully')
else:
    print('fail to connect')
connection.close()