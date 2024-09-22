import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root1234',
            database='dbms_project'
        )
        if connection.is_connected():
            print('Successfully connected to the database')
            return connection
    except Error as e:
        print('Error while connecting to MySQL', e)
        return None
