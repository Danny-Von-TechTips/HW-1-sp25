import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# Establish database connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

def initial_greeting():
    print("Hi there! Welcome to the database management system.")
    
    input1 = input("Would you like to add a new user to the database? (y/n) ").strip().lower()
    if input1 == "y":
        add_user()
    else:
        print("Okay, let's move on.")

    input2 = input("Would you like to add a new invoice to the database? (y/n) ").strip().lower()
    if input2 == "y":
        add_invoice()
    else:
        print("Okay, let's move on.")
        
def add_user():
    print("Great! Let's add a new user to the database.")
    first_name = input("Enter the first name of the user: ").strip()
    last_name = input("Enter the last name of the user: ").strip()

    # Using parameterized query to prevent SQL injection
    query = "INSERT INTO users (First_Name, Last_Name) VALUES (%s, %s)"
    values = (first_name, last_name)

    try:
        execute_query(conn, query, values)
        print(f"User '{first_name} {last_name}' added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")

# Start program
initial_greeting()
