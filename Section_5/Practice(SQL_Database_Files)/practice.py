import sqlite3

connection = sqlite3.connect('ravi.db')
cursor = connection.cursor()

create_table = "CREATE TABLE Users (id int, username text, password text)"
cursor.execute(create_table)

user = (10, "Nimish", "Sexynimish07")
query = "INSERT INTO Users VALUES (?, ?, ?)"
cursor.execute(query, user)

connection.commit()
connection.close()

