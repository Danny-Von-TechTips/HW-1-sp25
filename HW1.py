import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection, execute_query, execute_read_query

# Establish database connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

def initial_greeting():
    print("Hi there! Welcome to the database management system.")
    
    query = "SELECT * FROM vaults"
    execute_read_query(conn, query)
    
    input1 = input("Would you like to add a new vault to the database? (y/n) ").strip().lower()
    if input1 == "y":
        add_vault()
    else:
        print("Okay, let's move on.")
    
    input2 = input("Would you like to retrieve your entry by ID and Code? (y/n) ").strip().lower()
    if input2 == "y":
        get_entry_by_code()

def add_vault():
    print("Great! Let's add a new vault to the database.")
    Number = input("Enter a number: ").strip()
    Code = input("Enter a code to the vault: ").strip()
    Content = input("Enter a description of the vault: ").strip()
    Owner = input("Enter the last name of the owner of the vault: ").strip()

    query = "INSERT INTO vaults (Number, Code, Content, Owner) VALUES (%s, %s, %s, %s)"
    values = (Number, Code, Content, Owner)

    try:
        execute_query(conn, query, values)  
        print(f"vault '{Owner}' added successfully!")
    except Exception as e:
        print(f"Error adding vault: {e}")

def get_entry_by_code():
    entry_code = input("Enter your Code: ").strip()

    query = "SELECT * FROM vaults WHERE Code = %s"
    values = (entry_code,)

    try:
        cursor = conn.cursor(dictionary=True)  # ✅ Create cursor manually
        cursor.execute(query, values)
        entry = cursor.fetchall()  # ✅ Fetch result
        cursor.close() 
        if entry:
            print("\nEntry Details:")
            print(f"ID: {entry[0]['ID']}")
            print(f"Number: {entry[0]['Number']}")
            print(f"Code: {entry[0]['Code']}")  # You can remove this line if the code shouldn't be shown
            print(f"Content: {entry[0]['Content']}")
            print(f"Owner: {entry[0]['Owner']}")
        else:
            print("No entry found with the given ID and Code. Please try again.")
    except Exception as e:
        print(f"Error retrieving entry: {e}")

# Start program
initial_greeting()

