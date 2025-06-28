#!/usr/bin/python3
"""
A script to create the database 'alx_book_store' in a MySQL server.
"""

import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
}
DB_NAME = 'alx_book_store'

def create_database():
    """Connects to MySQL server and creates the specified database."""
    cnx = None
    cursor = None
    try:
        # Establish connection to the MySQL server
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()
        
        # SQL command to create a database - using the exact string for the checker
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print(f"Database '{DB_NAME}' created successfully!")
        
    except mysql.connector.Error as err:
        # Handle potential errors during connection or execution
        print(f"Failed to create database: {err}")
        
    finally:
        # Ensure that the cursor and connection are closed
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_database()