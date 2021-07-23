# To SignUp/ Register a user directly into the database
import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

# This will create a Users table inside mydatabase.db file
# Here we are using INTEGER istead of int to create auto-incrementing coloumn for 'id'
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

connection.commit()

connection.close()

# Its better to run the files from the terminal/ Command Prompt instead directly from here. 
# Try both ways you will get to know why its better to run the programs as well as data.db files from the terminal.