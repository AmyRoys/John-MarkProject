import psycopg2 

def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="test_user",
        password="amydb",  
        host="localhost",
        port="5432"
    )
