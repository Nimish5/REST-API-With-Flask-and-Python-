import sqlite3
connection = sqlite3.connect('nimish.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS Userss (id int, username text, password text)"
cursor.execute(create_table)

new_entry = (8, "Shubham", "Jain")
query = "INSERT INTO Userss VALUES (?, ?, ?)"
cursor.execute(query, new_entry)

create_table = "CREATE TABLE IF NOT EXISTS Items (Name text, Place text, Animal text, Price real)"
cursor.execute(create_table)

person = ("Anupam Tiwari", "Bangalore", "Dog", 10.9)
query = "INSERT INTO Items VALUES (?, ?, ?, ?)"
cursor.execute(query, person)

connection.commit()
connection.close()
