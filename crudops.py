'''
import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# Creating connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

# Create entry and add to table
query = "INSERT INTO users (First_Name, Last_Name) VALUES ('Thomas', 'Edison')"

execute_query(conn, query)

# Select all users
select_users = "SELECT * FROM users"
users = execute_read_query(conn, select_users)

for user in users:
    print(user["First_Name"] + " has the last name: " + user["Last_Name"])
'''
