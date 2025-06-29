import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
