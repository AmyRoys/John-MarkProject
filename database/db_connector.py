import psycopg2 

def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="test_user",
        password="amydb",  
        host="localhost",
        port="5432"
    )
    return conn

