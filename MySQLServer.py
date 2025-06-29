import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals() and cursor.is_connected() is False:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
