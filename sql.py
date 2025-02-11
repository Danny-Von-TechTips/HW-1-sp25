import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "cis2368database.cqp6i6kskj2h.us-east-1.rds.amazonaws.com",
            user = "admin",
            password = "cc6d71Nc0057b70+",
            database = "CIS2368DatabaseSpring2025"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error {e} ocurred.")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error {e} ocurred.")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error {e} ocurred.")