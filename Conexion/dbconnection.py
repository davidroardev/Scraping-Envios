import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='selenium',
            user='postgres',
            password='postgres',
            port='5432'
        )
        return conn
    except Exception as e:
        print('No se pudo conectar a la base de datos')
        return None