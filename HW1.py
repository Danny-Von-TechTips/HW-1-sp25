import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection, execute_query, execute_read_query

# Establish database connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

def initial_greeting():
    print("Hi there! Welcome to the database management system.")
    
    query = "SELECT * FROM users"
    users = execute_read_query(conn, query)
    
    if users:
        print("Current Users:")
        for user in users:
            print(user["First_Name"], user["Last_Name"])
    else:
        print("No users found in the database.")
            
    
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

    query = "INSERT INTO users (First_Name, Last_Name) VALUES (%s, %s)"
    values = (first_name, last_name)

    try:
        execute_query(conn, query, values)  
        print(f"User '{first_name} {last_name}' added successfully!")
    except Exception as e:
        print(f"Error adding user: {e}")

def add_invoice():
    print("Great! Let's add a new invoice to the database.")
    invoice_number = input("Enter the invoice number: ").strip()
    amount = input("Enter the invoice amount: ").strip()

    query = "INSERT INTO invoices (Invoice_Number, Amount) VALUES (%s, %s)"
    values = (invoice_number, amount)

    try:
        execute_query(conn, query, values)
        print(f"Invoice '{invoice_number}' added successfully!")
    except Exception as e:
        print(f"Error adding invoice: {e}")

# Start program
initial_greeting()

