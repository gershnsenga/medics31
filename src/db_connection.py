import mysql.connector

connection = None

def connect_to_database():
    global connection

    if not connection:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="12345670",
            database="metrics31"
        )
    
    return  connection

def close_db_connection():
    global connection
    if connection:
        connection.close
        connection = None

print ("Connected to database successfully")
