# Section5: Storing Resouces in a SQL Database
# Video-79
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# If you try to add a user into Users table/ database, it will through an error.(Try tob fix this)
# user = ("Nimish", "ravimotu")
# query = "INSERT INTO Users VALUES (NULL, ?, ?)"
# cursor.execute(query, user)

create_table = "CREATE TABLE IF NOT EXISTS Peoples (Name text, Money text, Luxury_Item text, Price real)"
cursor.execute(create_table)

people = ("Neha Pathak Rajvaidya", "All the money in the World!", "Home and Car", 100)
query = "INSERT INTO Peoples VALUES (?, ?, ?, ?)"
cursor.execute(query, people)

connection.commit()
connection.close()