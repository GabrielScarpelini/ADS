import mysql.connector

#arquivo somente para conectar no banco de dados sqlite

def mySQL_conection():
    config = {
        'user': 'gabriel',
        'password': 'Mudar1234!',
        'host': 'localhost',  # Ou o endereço do servidor MySQL
        'database': 'Labs',
    }
    conn = mysql.connector.connect(**config)
    return conn